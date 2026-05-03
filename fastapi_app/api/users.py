from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_app.database import get_db
from fastapi_app.models import User
from fastapi_app.schemas import UserBase

router = APIRouter(prefix="/fastapi/users", tags=["users"])

@router.get("/", response_model=list[UserBase])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()