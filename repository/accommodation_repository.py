from sqlalchemy.orm import Session
from model.models import Accommodation
from model.schemas import AccommodationCreateDTO, AccommodationUpdateDTO


def list_all(db: Session):
    return db.query(Accommodation).all()


def find_by_id(db: Session, accommodation_id: int):
    return db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()


def save(db: Session, accommodation_create: AccommodationCreateDTO):
    new_accommodation = Accommodation(
        name=accommodation_create.name,
        category=accommodation_create.category,
        host_id=accommodation_create.host_id,
        numRooms=accommodation_create.numRooms,
        is_available=accommodation_create.is_available
    )
    db.add(new_accommodation)
    db.commit()
    db.refresh(new_accommodation)
    return new_accommodation


def update(db: Session, accommodation_update: AccommodationUpdateDTO, accommodation_id: int):
    accommodation = find_by_id(db, accommodation_id)

    if not accommodation:
        return None

    for key, value in accommodation_update.model_dump(exclude_unset=True).items():
        setattr(accommodation, key, value)

    db.commit()
    db.refresh(accommodation)
    return accommodation


def delete_by_id(db: Session, accommodation_id: int):
    accommodation = find_by_id(db, accommodation_id)

    if accommodation:
        db.delete(accommodation)
        db.commit()
        return True

    return False
