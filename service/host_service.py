# from repository import host_repository
#
#
# def list_all():
#     return host_repository.list_all()
#
#
# def find_by_id(country_id: int):
#     return host_repository.find_by_id(country_id)

from sqlalchemy.orm import Session

from repository import host_repository


def list_all(db: Session):
    return host_repository.list_all(db)


def find_by_id(db: Session, host_id: int):
    return host_repository.find_by_id(db, host_id)
