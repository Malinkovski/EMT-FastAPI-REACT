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
    #category = Column(String)
    category = Column(Enum(CategoryShema))
    host_id = Column(Integer, ForeignKey("hosts.id"))
    numRooms = Column(Integer)
    is_available = Column(Boolean)

    host = relationship("Host", back_populates="accommodations")
