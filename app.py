from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/airline"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    """List flights for booking."""
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get name input value
    name = request.form.get("name")

    # Validate name value
    if name == None or len(name) < 3:
        return render_template("error.html", message="Name value must be more than 2 characters.")

    return "book a flight"


@app.route("/flights")
def flights():
    """List all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about single flight."""

    # Check flight is exist
    flight = Flight.query.filter_by(id=flight_id).first()

    # Get passengers list
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()

    return render_template("flight.html", flight=flight, passengers=passengers)
