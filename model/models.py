from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base

from model.schemas import CategoryShema

Base = declarative_base()


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    continent = Column(String)

    hosts = relationship("Host", back_populates="country")


class Host(Base):
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="hosts")
    accommodations = relationship("Accommodation", back_populates="host")


class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # category = Column(String)
    category = Column(Enum(CategoryShema))
    host_id = Column(Integer, ForeignKey("hosts.id"))
    numRooms = Column(Integer)
    is_available = Column(Boolean)

    host = relationship("Host", back_populates="accommodations")
    reservation_items = relationship("ReservationItem", back_populates="accommodation")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    reservation_lists = relationship("ReservationList", back_populates="user")

class ReservationList(Base):
    __tablename__ = "reservation_lists"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="reservation_lists")
    items = relationship("ReservationItem", back_populates="reservation_list")

class ReservationItem(Base):
    __tablename__ = "reservation_items"

    id = Column(Integer, primary_key=True)
    num_nights = Column(Integer)
    reservation_list_id = Column(Integer, ForeignKey("reservation_lists.id"))
    accommodation_id = Column(Integer, ForeignKey("accommodations.id"))

    reservation_list = relationship("ReservationList", back_populates="items")
    accommodation = relationship("Accommodation", back_populates="reservation_items")