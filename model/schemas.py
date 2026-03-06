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

class Accommodation(BaseModel):
    id: int

class Category(Enum):
    ROOM = "Room",
    HOUSE = "House",
    FLAT = "Flat",
    APARTMENT = "Apartment",
    HOTEL = "Hotel",
    MOTEL = "Motel"
