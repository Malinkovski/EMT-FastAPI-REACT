from pydantic import BaseModel
from enum import Enum

class Country(BaseModel):
    id: int
    name: str
    continent: str

class Host(BaseModel):
    id: int
    name: str
    surname: str
    country: Country

class Category(Enum):
    ROOM = "Room"
    HOUSE = "House"
    FLAT = "Flat"
    APARTMENT = "Apartment"
    HOTEL = "Hotel"
    MOTEL = "Motel"

class Accommodation(BaseModel):
    id: int
    name: str
    category: Category
    host: Host
    numRooms: int
    is_available: bool

class AccommodationDTO(BaseModel):
    id: int
    name: str
    category: str
    host_id: int
    numRooms: int
    is_available: bool