from repository import host_repository


def list_all():
    return host_repository.list_all()


def find_by_id(country_id: int):
    return host_repository.find_by_id(country_id)
