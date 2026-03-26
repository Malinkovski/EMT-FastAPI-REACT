from database.database import SessionLocal, engine
from model.models import Base, Country, Host, Accommodation
from model.schemas import CategoryShema


def seed():
    Base.metadata.create_all(engine)
    db = SessionLocal()

    try:
        # no dupes
        if db.query(Country).count() > 0:
            print("Database already seeded. Skipping.")
            return

        # countries
        countries = [
            Country(name="Italy", continent="Europe"),
            Country(name="Japan", continent="Asia"),
            Country(name="United States", continent="North America")
        ]

        db.add_all(countries)
        db.flush()

        # hosts
        hosts = [
            Host(name="Mario", surname="Rossi", country_id=countries[0].id),
            Host(name="Kenji", surname="Tanaka", country_id=countries[1].id),
            Host(name="John", surname="Smith", country_id=countries[2].id)
        ]

        db.add_all(hosts)
        db.flush()

        # accommodations
        accommodations = [
            Accommodation(
                name="Apartments Top",
                category=CategoryShema.APARTMENT,
                host_id=hosts[0].id,
                numRooms=3,
                is_available=True,
            ),
            Accommodation(
                name="Tokyo Central Room",
                category=CategoryShema.ROOM,
                host_id=hosts[1].id,
                numRooms=1,
                is_available=True
            ),
            Accommodation(
                name="Mountain House",
                category=CategoryShema.HOUSE,
                host_id=hosts[2].id,
                numRooms=5,
                is_available=False
            )
        ]

        db.add_all(accommodations)
        db.commit()

        print("Database seeded successfully.")

    except Exception:
        db.rollback()
        print("Seeding failed.", Exception)
    finally:
        db.close()