from flask import Flask, render_template, request, jsonify
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

    # Get flight id value
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    # Make sure the flight exists
    flight = Flight.query.get(flight_id)

    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # Add passenger
    flight.add_passenger(name=name)

    return render_template("success.html")


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
    passengers = flight.passengers

    return render_template("flight.html", flight=flight, passengers=passengers)


@app.route("/api/flights")
def api_flights():

    # Get all flights
    flights = Flight.query.all()
    data = []
    for flight in flights:
        data.append({"id": flight.id, "origin": flight.origin,
                     "destination": flight.destination, "duration": flight.duration})

    # Return data
    return jsonify({"flights": data})


@app.route("/api/flights/<int:flight_id>")
def api_flight(flight_id):

    # Get flight by id
    flight = Flight.query.get(flight_id)

    # Make sure that flight exists
    if flight is None:
        return jsonify({"error": "Invalid flight_id."}), 422

    # Get passengers list by flight
    passengers = flight.passengers
    passengers_list = []
    for passenger in passengers:
        passengers_list.append({"name": passenger.name, "id": passenger.id})

    # Return data
    return jsonify({"id": flight.id, "origin": flight.origin, "destination": flight.destination, "duration": flight.duration, "passengers": passengers_list})
