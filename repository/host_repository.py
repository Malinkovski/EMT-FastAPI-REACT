from model.schemas import Host
from repository import country_repository

hosts = [
    Host(id=1, name="Mario", surname="Rossi", country=country_repository.find_by_id(1)),
    Host(id=2, name="Kenji", surname="Tanaka", country=country_repository.find_by_id(2)),
    Host(id=3, name="John", surname="Smith", country=country_repository.find_by_id(3))
]


def list_all():
    return hosts


def find_by_id(host_id: int):
    for host in hosts:
        if host.id == host_id:
            return host
    raise ValueError(f"Host with id {host_id} not found")
    # return None
