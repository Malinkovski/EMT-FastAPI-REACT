# from repository import country_repository
#
#
# def list_all():
#     return country_repository.list_all()
#
#
# def find_by_id(country_id: int):
#     return country_repository.find_by_id(country_id)
#
from sqlalchemy.orm import Session

from repository import country_repository


def list_all(db: Session):
    return country_repository.list_all(db)


def find_by_id(db:Session, country_id: int):
    return country_repository.find_by_id(db, country_id)
