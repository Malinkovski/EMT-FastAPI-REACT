from fastapi import FastAPI

from database.seed import seed
from web import accommodation_router

from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import engine
from model.models import Base

Base.metadata.create_all(bind=engine)
seed()

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     seed()
#     yield

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

app.include_router(accommodation_router.router)

