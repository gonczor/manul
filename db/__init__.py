from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db(database):
    database.create_all()
