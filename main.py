from fastapi import FastAPI
from web import accommodation_router

from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.database import engine
from model.models import Base

Base.metadata.create_all(bind=engine)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     seed()
#     yield

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

app.include_router(accommodation_router.router)

