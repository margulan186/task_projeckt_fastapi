
from fastapi import  FastAPI
from contextlib import asynccontextmanager

from database import create_table, delate_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delate_tables()
    print("База очищена")
    await create_table()
    print("База готова к работе")
    yield
    print("Выключение")
    
    
app = FastAPI(lifespan=lifespan)
app.include_router(task_router)


    
    
