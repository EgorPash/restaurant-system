from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_app.database import get_db
from fastapi_app.models import Table
from fastapi_app.schemas import TableBase

router = APIRouter(prefix="/fastapi/tables", tags=["tables"])

@router.get("/", response_model=list[TableBase])
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()