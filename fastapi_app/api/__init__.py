from fastapi_app.api.tables import router as tables_router
from fastapi_app.api.orders import router as orders_router
from fastapi_app.api.users import router as users_router

routers = [tables_router, orders_router, users_router]
