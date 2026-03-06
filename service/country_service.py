from repository import country_repository


def list_all():
    return country_repository.list_all()


def find_by_id(country_id: int):
    return country_repository.find_by_id(country_id)
