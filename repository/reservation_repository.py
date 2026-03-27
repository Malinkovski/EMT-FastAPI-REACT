# Креирајте repository/reservation_repository.py
# Имплементирајте ги следните функции (сите примаат db: Session како прв аргумент):
#
# get_list_by_user(db, user_id) - ја враќа листата на резервации на корисникот
# create_list(db, user_id) - создава нова листа на резервации за корисникот
# add_item(db, list_id, item_data) - додава ново ReservationItem во листата
# remove_item(db, list_id, item_id) - ја брише ставката само ако припаѓа на таа листа
# clear_list(db, list_id) - ги брише сите ставки од листата
# get_items(db, list_id) - ги враќа сите ставки
# confirm_reservations(db, list_id) - за секоја ставка проверете дали сместувањето е достапно (is_available); ако не е фрлете ValueError; ако е означете го сместувањето како недостапно (is_available = False) и испразнете ја листата; целата операција мора да биде во еден db.commit()
# Напомена: За confirm_reservations да работи, моделот Accommodation треба да има поле is_available: bool. Додајте го ако го немате.
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
