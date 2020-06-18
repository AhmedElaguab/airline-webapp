from flask import Flask
import csv
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/airline"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def import_flights():
    """This function is used to import flights into database."""
    f = open("data/flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination,
                        duration=duration)
        db.session.add(flight)
    db.session.commit()


def main():
    """This script is used to create your 'SQL' tables."""
    db.create_all()

    # Uncomment the function call bellow to import flights into database
    # import_flights()


if __name__ == "__main__":
    with app.app_context():
        main()
