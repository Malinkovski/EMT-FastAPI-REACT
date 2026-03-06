from repository import accommodation_repository


def list_all():
    return accommodation_repository.list_all()


def find_by_id(accommodation_id: int):
    return accommodation_repository.find_by_id(accommodation_id)

# save

# delete

# update
