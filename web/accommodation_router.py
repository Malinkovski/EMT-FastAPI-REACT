from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database.database import get_db
from model.schemas import AccommodationShema, AccommodationCreateDTO, AccommodationUpdateDTO
from service import accommodation_service

router = APIRouter(prefix="/api/accommodations", tags=["Accommodation"])


@router.get("", response_model=list[AccommodationShema])
async def list_accommodations(db: Session = Depends(get_db)):
    return accommodation_service.list_all(db)


@router.get("/{accommodation_id}", response_model=AccommodationShema)
async def find_accommodation(accommodation_id: int, db: Session = Depends(get_db)):
    accommodation = accommodation_service.find_by_id(db, accommodation_id)
    if accommodation is not None:
        return accommodation
    return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accommodation_id} not found"})


@router.post("", response_model=AccommodationShema)
async def create_accommodation(
        accommodation_create: AccommodationCreateDTO,
        db: Session = Depends(get_db)):
    return accommodation_service.save(db, accommodation_create)


@router.put("/{accommodation_id}", response_model=AccommodationShema)
async def update_accommodation(
        accommodation_id: int,
        accommodation_update: AccommodationUpdateDTO, db: Session = Depends(get_db)):
    accommodation = accommodation_service.find_by_id(db, accommodation_id)
    if accommodation is not None:
        return accommodation_service.update(db, accommodation_update, accommodation_id)
    return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accommodation_id} not found"})


@router.delete("/{accommodation_id}")
async def delete_accommodation(
        accommodation_id: int,
        db: Session = Depends(get_db)):
    accommodation = accommodation_service.find_by_id(db, accommodation_id)
    if accommodation is not None:
        accommodation_service.delete(db, accommodation_id)
        return JSONResponse(status_code=200,
                            content={"message": f"Accommodation with id {accommodation_id} deleted successfully"})
    else:
        return JSONResponse(status_code=404, content={"message": f"Accommodation with id {accommodation_id} not found"})
