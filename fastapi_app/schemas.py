from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class TimeSectionBase(BaseModel):
    id: int
    time_section: str

class TableBase(BaseModel):
    id: int
    number: int
    seats: int
    image: Optional[str] = None

class UserBase(BaseModel):
    id: int
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class OrderBase(BaseModel):
    id: int
    user: Optional[UserBase] = None
    table: Optional[TableBase] = None
    reservation_date: Optional[date] = None
    order_confirm: bool = False
    order_time: List[TimeSectionBase] = []

class OrderCreate(BaseModel):
    table_id: int
    reservation_date: date
    order_time_ids: List[int]  # список ID временных интервалов

class OrderUpdate(BaseModel):
    order_confirm: Optional[bool] = None
