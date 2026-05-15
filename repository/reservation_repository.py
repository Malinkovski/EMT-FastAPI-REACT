from sqlalchemy.orm import Session

from model.models import ReservationList, ReservationItem, Accommodation
from model.schemas import ReservationItemDTO


def get_list_by_user(db: Session, user_id: int):
    return db.query(ReservationList).filter(ReservationList.user_id == user_id).first()


def create_list(db: Session, user_id: int):
    reservation_list = ReservationList(user_id=user_id)
    db.add(reservation_list)
    db.commit()
    db.refresh(reservation_list)
    return reservation_list


def add_item(db: Session, list_id: int, item_data: ReservationItemDTO):
    item = ReservationItem(
        reservation_list_id=list_id,
        accommodation_id=item_data.accommodation_id,
        num_nights=item_data.num_nights
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def remove_item(db: Session, list_id: int, item_id: int):
    item = db.query(ReservationItem).filter(
        ReservationItem.id == item_id,
        ReservationItem.reservation_list_id == list_id
    ).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False


def clear_list(db: Session, list_id: int):
    db.query(ReservationItem).filter(
        ReservationItem.reservation_list_id == list_id
    ).delete()
    db.commit()


def get_items(db: Session, list_id: int):
    return db.query(ReservationItem).filter(
        ReservationItem.reservation_list_id == list_id
    ).all()


def confirm_reservations(db: Session, list_id: int):
    items = db.query(ReservationItem).filter(
        ReservationItem.reservation_list_id == list_id
    ).all()

    for item in items:
        accommodation = db.query(Accommodation).filter(
            Accommodation.id == item.accommodation_id
        ).first()

        if not accommodation or not accommodation.is_available:
            raise ValueError(f"Accommodation {item.accommodation_id} is not available")

        accommodation.is_available = False

    db.query(ReservationItem).filter(
        ReservationItem.reservation_list_id == list_id
    ).delete()

    db.commit()
