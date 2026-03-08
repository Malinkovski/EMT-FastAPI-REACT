from repository import accommodation_repository, host_repository
from model.schemas import Accommodation, Category, AccommodationDTO


def list_all():
    return accommodation_repository.list_all()


def find_by_id(accommodation_id: int):
    return accommodation_repository.find_by_id(accommodation_id)


def save(accommodation_dto: AccommodationDTO):
    host = host_repository.find_by_id(accommodation_dto.host_id)

    accommodation = Accommodation(
        id=accommodation_dto.id,
        name=accommodation_dto.name,
        category=Category[accommodation_dto.category],
        host=host,
        numRooms=accommodation_dto.numRooms,
        is_available=accommodation_dto.is_available
    )

    return accommodation_repository.save(accommodation)


def delete_by_id(accommodation_id: int):
    accommodation_repository.delete_by_id(accommodation_id)


def update(accommodation_dto: AccommodationDTO):
    accommodation = accommodation_repository.find_by_id(accommodation_dto.id)
    host = host_repository.find_by_id(accommodation_dto.host_id)

    accommodation.name = accommodation_dto.name
    accommodation.category = Category[accommodation_dto.category]
    accommodation.host = host
    accommodation.numRooms = accommodation_dto.numRooms
    accommodation.is_available = accommodation_dto.is_available

    return accommodation
