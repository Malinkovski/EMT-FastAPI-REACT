# from model.schemas import Accommodation
# from repository import country_repository, host_repository
# from model.schemas import Category
#
# accommodations = [
#     Accommodation(
#         id=1,
#         name="Sea View Apartment",
#         category=Category.APARTMENT,
#         host=host_repository.find_by_id(1),
#         numRooms=3,
#         is_available=True
#     ),
#     Accommodation(
#         id=2,
#         name="Tokyo Central Room",
#         category=Category.ROOM,
#         host=host_repository.find_by_id(2),
#         numRooms=1,
#         is_available=True
#     ),
#     Accommodation(
#         id=3,
#         name="Mountain House Retreat",
#         category=Category.HOUSE,
#         host=host_repository.find_by_id(3),
#         numRooms=5,
#         is_available=False
#     ),
#     Accommodation(
#         id=4,
#         name="Luxury City Flat",
#         category=Category.FLAT,
#         host=host_repository.find_by_id(2),
#         numRooms=2,
#         is_available=True
#     ),
#     Accommodation(
#         id=5,
#         name="Roadside Motel Stay",
#         category=Category.MOTEL,
#         host=host_repository.find_by_id(1),
#         numRooms=10,
#         is_available=True
#     ),
# ]
#
#
# def list_all():
#     return accommodations
#
#
# def find_by_id(accommodation_id: int):
#     for accommodation in accommodations:
#         if accommodation.id == accommodation_id:
#             return accommodation
#     raise ValueError(f"Accommodation with id {accommodation_id} not found")
#     # return None
#
#
# def save(accommodation: Accommodation):
#     accommodations.append(accommodation)
#     return accommodation
#
#
# def delete_by_id(accommodation_id: int):
#     for accommodation in accommodations:
#         if accommodation.id == accommodation_id:
#             accommodations.remove(accommodation)
#             return True
#     return False
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
