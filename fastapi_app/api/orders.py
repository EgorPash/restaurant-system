from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi_app.database import get_db
from fastapi_app.models import Order, Table, TimeSection, User
from fastapi_app.schemas import OrderBase, OrderCreate, OrderUpdate

router = APIRouter(prefix="/fastapi/orders", tags=["orders"])

@router.get("/", response_model=list[OrderBase])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderBase)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.post("/", response_model=OrderBase)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Проверка, что столик существует
    table = db.query(Table).filter(Table.id == order.table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")

    # Проверка, что временные интервалы существуют
    times = db.query(TimeSection).filter(TimeSection.id.in_(order.order_time_ids)).all()
    if len(times) != len(order.order_time_ids):
        raise HTTPException(status_code=400, detail="One or more time sections not found")

    # Проверка на конфликт бронирования
    existing = db.query(Order).filter(
        Order.table_id == order.table_id,
        Order.reservation_date == order.reservation_date,
        Order.order_time.any(TimeSection.id.in_(order.order_time_ids))
    ).first()
    if existing:
        raise HTTPException(status_code=409, detail="Conflict: This table is already booked for selected time")

    # Создание заказа
    db_order = Order(
        table_id=order.table_id,
        reservation_date=order.reservation_date,
        order_confirm=False
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Привязка временных интервалов
    for ts in times:
        db.execute(
            "INSERT INTO service_order_order_time (order_id, timesection_id) VALUES (:order_id, :ts_id)",
            {"order_id": db_order.id, "ts_id": ts.id}
        )
    db.commit()
    db.refresh(db_order)
    return db_order

@router.patch("/{order_id}", response_model=OrderBase)
def update_order(order_id: int, update: OrderUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if update.order_confirm is not None:
        order.order_confirm = update.order_confirm
    db.commit()
    db.refresh(order)
    return order