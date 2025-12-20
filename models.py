#SQL Lite sits here
from extension import db

class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)


class Topic(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    subject = db.relationship("Subject", backref="topics")


class Subtopic(db.Model):
    __tablename__ = "subtopics"

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topics.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)

    topic = db.relationship("Topic", backref="subtopics")


class Quiz(db.Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)
    subtopic_id = db.Column(db.Integer, db.ForeignKey("subtopics.id"), nullable=False)
    title = db.Column(db.String(100))

    subtopic = db.relationship("Subtopic", backref="quizzes")


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)

    question_text = db.Column(db.Text, nullable=False)

    option_a = db.Column(db.String(200))
    option_b = db.Column(db.String(200))
    option_c = db.Column(db.String(200))
    option_d = db.Column(db.String(200))

    correct_answer = db.Column(db.String(1))
    explanation = db.Column(db.Text)

    quiz = db.relationship("Quiz", backref="questions")


