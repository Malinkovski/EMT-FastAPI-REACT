from database.database import SessionLocal, engine
from model.models import Base, Country, Host, Accommodation, User, ReservationList
from model.schemas import CategoryShema


def seed():
    Base.metadata.create_all(engine)
    db = SessionLocal()

    try:
        # no dupes
        if db.query(Country).count() > 0 or db.query(User).count() > 0:
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
            ),
            Accommodation(
                name="Luxury Beach Hotel",
                category=CategoryShema.HOTEL,
                host_id=hosts[0].id,
                numRooms=12,
                is_available=True
            ),
            Accommodation(
                name="Skyline Penthouse",
                category=CategoryShema.FLAT,
                host_id=hosts[1].id,
                numRooms=4,
                is_available=True
            ),
            Accommodation(
                name="Forest Cabin Retreat",
                category=CategoryShema.HOUSE,
                host_id=hosts[2].id,
                numRooms=2,
                is_available=True
            ),
            Accommodation(
                name="City Budget Motel",
                category=CategoryShema.MOTEL,
                host_id=hosts[0].id,
                numRooms=8,
                is_available=False
            ),
            Accommodation(
                name="Modern Apartment Loft",
                category=CategoryShema.APARTMENT,
                host_id=hosts[1].id,
                numRooms=2,
                is_available=True
            ),
            Accommodation(
                name="Traditional Kyoto Stay",
                category=CategoryShema.ROOM,
                host_id=hosts[1].id,
                numRooms=1,
                is_available=True
            ),
            Accommodation(
                name="Grand Palace Hotel",
                category=CategoryShema.HOTEL,
                host_id=hosts[2].id,
                numRooms=20,
                is_available=True
            )
        ]
        db.add_all(accommodations)
        db.flush()

        # users
        users = [
            User(username="Ivan", email="Ivan@example.com", password="password1"),
            User(username="Ana", email="ana@example.com", password="password2")
        ]
        db.add_all(users)
        db.flush()

        # reservation lists
        lists = [
            ReservationList(user_id=users[0].id),
            ReservationList(user_id=users[1].id)
        ]
        db.add_all(lists)

        db.commit()
        print("Database seeded successfully.")

    except Exception as e:
        db.rollback()
        print("Seeding failed.", e)
    finally:
        db.close()


if __name__ == "__main__":
    seed()