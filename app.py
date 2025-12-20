from flask import Flask
from extension import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///codesprout.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app


app = create_app()

# TEMPORARY: create tables
with app.app_context():
    from models import Subject, Topic, Subtopic, Quiz, Question
    db.create_all()