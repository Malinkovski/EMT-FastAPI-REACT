from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from service import reservation_service
from model.schemas import ReservationItemDTO, ReservationListSchema, ReservationItemSchema

router = APIRouter(prefix="/api/reservations", tags=["Reservation"])


@router.get("/user/{user_id}", response_model=ReservationListSchema)
def get_user_reservation_list(user_id: int, db: Session = Depends(get_db)):
    reservation_list = reservation_service.get_list_by_user(db, user_id)
    if not reservation_list:
        raise HTTPException(status_code=404, detail="Reservation list not found")
    return reservation_list


@router.post("/user/{user_id}", response_model=ReservationListSchema)
def create_user_reservation_list(user_id: int, db: Session = Depends(get_db)):
    return reservation_service.create_list(db, user_id)


@router.post("/{list_id}/add-item", response_model=ReservationItemSchema)
def add_item_to_list(list_id: int, item_data: ReservationItemDTO, db: Session = Depends(get_db)):
    return reservation_service.add_item(db, list_id, item_data)


@router.delete("/{list_id}/items/{item_id}")
def remove_item_from_list(list_id: int, item_id: int, db: Session = Depends(get_db)):
    success = reservation_service.remove_item(db, list_id, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found in this list")
    return {"detail": "Item removed successfully"}


@router.post("/{list_id}/confirm")
def confirm_reservation_list(list_id: int, db: Session = Depends(get_db)):
    try:
        reservation_service.confirm_reservations(db, list_id)
        return {"detail": "Reservations confirmed successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{list_id}/items", response_model=list[ReservationItemSchema])
def get_reservation_items(list_id: int, db: Session = Depends(get_db)):
    return reservation_service.get_items(db, list_id)
