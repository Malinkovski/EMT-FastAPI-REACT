from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from database.database import get_db
from service import country_service
from model.schemas import CountryShema


router = APIRouter(prefix="/api/countries", tags=["Countries"])


@router.get("", response_model=list[CountryShema])
async def list_countries(db: Session = Depends(get_db)):
    return country_service.list_all(db)


@router.get("/{country_id}", response_model=CountryShema)
async def find_country(country_id: int, db: Session = Depends(get_db)):
    country = country_service.find_by_id(db, country_id)
    if country is not None:
        return country

    return JSONResponse(
        status_code=404,
        content={"message": f"Country with id {country_id} not found"}
    )