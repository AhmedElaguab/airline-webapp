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
