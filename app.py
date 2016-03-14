#!venv/bin/python
from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    phone = db.Column(db.Text)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Person, methods=['GET', 'POST', 'DELETE', 'PUT'])

if __name__ == "__main__":
    app.run()
