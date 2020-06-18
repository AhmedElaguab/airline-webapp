from flask import Flask, render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/airline"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    """This script is used to create your 'SQL' tables"""
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()
