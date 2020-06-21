from flask import Flask, render_template
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
    return render_template("flight.html", flight=flight)
