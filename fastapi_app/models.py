from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from fastapi_app.database import Base

# Модель Order (связь ManyToMany через промежуточную таблицу)
order_time_association = Table(
    "service_order_order_time",
    Base.metadata,
    Column("order_id", ForeignKey("service_order.id"), primary_key=True),
    Column("timesection_id", ForeignKey("service_timesection.id"), primary_key=True),
)

# Модель TimeSection
class TimeSection(Base):
    __tablename__ = "service_timesection"
    id = Column(Integer, primary_key=True, index=True)
    time_section = Column(String, index=True)

# Модель Table
class Table(Base):
    __tablename__ = "service_table"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    seats = Column(Integer)
    image = Column(String, nullable=True)

# Модель User (из Django)
class User(Base):
    __tablename__ = "users_user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

class Order(Base):
    __tablename__ = "service_order"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users_user.id"), nullable=True)
    table_id = Column(Integer, ForeignKey("service_table.id"), nullable=True)
    reservation_date = Column(Date, nullable=True)
    order_confirm = Column(Boolean, default=False)

    user = relationship("User", backref="orders")
    table = relationship("Table", backref="orders")
    order_time = relationship("TimeSection", secondary=order_time_association, backref="orders")