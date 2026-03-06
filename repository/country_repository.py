from model.schemas import Country

countries = [
    Country(id=1, name="Italy", continent="Europe"),
    Country(id=2, name="Japan", continent="Asia"),
    Country(id=3, name="USA", continent="North America")
]

def list_all():
    return countries


def find_by_id(country_id: int):
    for country in countries:
        if country.id == country_id:
            return country
    return None
