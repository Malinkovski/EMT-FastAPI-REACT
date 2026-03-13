from typing import Optional

from pydantic import BaseModel
from enum import Enum


class CountryShema(BaseModel):
    id: int
    name: str
    continent: str

    class Config:
        from_attributes = True


class HostShema(BaseModel):
    id: int
    name: str
    surname: str
    country: CountryShema

    class Config:
        from_attributes = True


class CategoryShema(Enum):
    ROOM = "Room"
    HOUSE = "House"
    FLAT = "Flat"
    APARTMENT = "Apartment"
    HOTEL = "Hotel"
    MOTEL = "Motel"

    class Config:
        from_attributes = True


class AccommodationShema(BaseModel):
    id: int
    name: str
    category: CategoryShema
    host: HostShema
    numRooms: int
    is_available: bool

    class Config:
        from_attributes = True


# class AccommodationDTO(BaseModel):
#     id: int
#     name: str
#     category: str
#     host_id: int
#     numRooms: int
#     is_available: bool
#
#     class Config:
#         from_attributes = True


class AccommodationCreateDTO(BaseModel):
    name: str
    category: str
    host_id: int
    numRooms: int
    is_available: bool


class AccommodationUpdateDTO(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    host_id: Optional[int] = None
    numRooms: Optional[int] = None
    is_available: Optional[bool] = None
