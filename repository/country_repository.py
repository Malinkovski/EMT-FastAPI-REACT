# from model.schemas import Country
#
# countries = [
#     Country(id=1, name="Italy", continent="Europe"),
#     Country(id=2, name="Japan", continent="Asia"),
#     Country(id=3, name="USA", continent="North America")
# ]
#
#
# def list_all():
#     return countries
#
#
# def find_by_id(country_id: int):
#     for country in countries:
#         if country.id == country_id:
#             return country
#     raise ValueError(f"Country with id {country_id} not found")
#     # return None

from sqlalchemy.orm import Session
from model.models import Country


def list_all(db: Session):
    return db.query(Country).all()


def find_by_id(db: Session, country_id: int):
    return db.query(Country).filter(Country.id == country_id).first()
