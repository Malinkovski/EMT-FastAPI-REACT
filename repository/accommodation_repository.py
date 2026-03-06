from model.schemas import Accommodation
from repository import country_repository, host_repository
from model.schemas import Category

accommodations = [
    Accommodation(
        id=1,
        name="Sea View Apartment",
        category=Category.APARTMENT,
        host=host_repository.find_by_id(1),
        numRooms=3,
        is_available=True
    ),
    Accommodation(
        id=2,
        name="Tokyo Central Room",
        category=Category.ROOM,
        host=host_repository.find_by_id(2),
        numRooms=1,
        is_available=True
    ),
    Accommodation(
        id=3,
        name="Mountain House Retreat",
        category=Category.HOUSE,
        host=host_repository.find_by_id(3),
        numRooms=5,
        is_available=False
    ),
    Accommodation(
        id=4,
        name="Luxury City Flat",
        category=Category.FLAT,
        host=host_repository.find_by_id(2),
        numRooms=2,
        is_available=True
    ),
    Accommodation(
        id=5,
        name="Roadside Motel Stay",
        category=Category.MOTEL,
        host=host_repository.find_by_id(1),
        numRooms=10,
        is_available=True
    ),
]


def list_all():
    return accommodations


def find_by_id(accommodation_id: int):
    for accommodation in accommodations:
        if accommodation.id == accommodation_id:
            return accommodation
    return None


def save(accommodation: Accommodation):
    accommodations.append(accommodation)
    return accommodation


def delete_by_id(accommodation_id: int):
    for accommodation in accommodations:
        if accommodation.id == accommodation_id:
            accommodations.remove(accommodation)
            return True
    return False
