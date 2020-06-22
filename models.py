from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def add_passenger(self, name):
        passenger = Passenger(name=name, flight_id=self.id)
        db.session.add(passenger)
        db.session.commit()

    @property
    def format(self):
        return f"{self.origin} to {self.destination}, {self.duration} minutes."

    def print_info(self):
        print()
        print(f"Flight info #({self.id})")
        print(f"→ origin: {self.origin}")
        print(f"→ destination: {self.destination}")
        print(f"→ duration: {self.duration}")


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey(
        "flights.id"), nullable=False)

    def print_info(self):
        print()
        print(f"Passenger info #({self.id})")
        print(f"→ name: {self.name}")
        print(f"→ flight id: {self.flight_id}")
