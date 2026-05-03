from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_app.api import routers
from fastapi_app.database import engine
from fastapi_app.models import Base

# Создаем таблицы (если их нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Синьор Помидор FastAPI", version="1.0")

# CORS — разрешаем Django-фронтенд
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене ограничьте!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
for router in routers:
    app.include_router(router)

@app.get("/")
def root():
    return {"message": "FastAPI for Синьор Помидор is running!"}