from sqlalchemy.orm import Session

from model.schemas import ReservationItemDTO
from repository import reservation_repository


def get_list_by_user(db: Session, user_id: int):
    return reservation_repository.get_list_by_user(db, user_id)


def create_list(db: Session, user_id: int):
    return reservation_repository.create_list(db, user_id)


def add_item(db: Session, list_id: int, item_data: ReservationItemDTO):
    return reservation_repository.add_item(db, list_id, item_data)


def remove_item(db: Session, list_id: int, item_id: int):
    return reservation_repository.remove_item(db, list_id, item_id)


def clear_list(db: Session, list_id: int):
    return reservation_repository.clear_list(db, list_id)


def get_items(db: Session, list_id: int):
    return reservation_repository.get_items(db, list_id)


def confirm_reservations(db: Session, list_id: int):
    return reservation_repository.confirm_reservations(db, list_id)