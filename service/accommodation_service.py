from sqlalchemy.orm import Session
from model.schemas import AccommodationCreateDTO, AccommodationUpdateDTO
from repository import accommodation_repository


def list_all(db: Session):
    return accommodation_repository.list_all(db)


def find_by_id(db: Session, accommodation_id: int):
    return accommodation_repository.find_by_id(db, accommodation_id)


def save(db: Session, accommodation_create: AccommodationCreateDTO):
    return accommodation_repository.save(db, accommodation_create)


def update(db: Session, accommodation_update: AccommodationUpdateDTO, accommodation_id: int):
    return accommodation_repository.update(db, accommodation_update, accommodation_id)


def delete(db: Session, accommodation_id: int):
    return accommodation_repository.delete_by_id(db, accommodation_id)
