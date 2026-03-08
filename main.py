from fastapi import FastAPI
from web import accommodation_router

app = FastAPI()

app.include_router(accommodation_router.router)

