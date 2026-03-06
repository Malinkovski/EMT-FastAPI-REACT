from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse

from service import accommodation_service

router = APIRouter(prefix="/api/accommodations", tags=["Accommodations"])

# list all
# find by id
