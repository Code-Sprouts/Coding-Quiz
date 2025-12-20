# End-points live here

from flask import Blueprint, jsonify
from models import Subject, Topic, Subtopic, Quiz, Question

code_sprout = Blueprint("code_sprout", __name__)

@code_sprout.route("/code-sprout/subjects")
def get_subjects():
    subjects = Subject.query.all()

    return jsonify([
        {
            "id": s.id,
            "name": s.name,
            "description": s.description
        }
        for s in subjects
    ])


@code_sprout.route("/code-sprout/subjects/<int:subject_id>/topics")
def get_topics(subject_id):
    topics = Topic.query.filter_by(subject_id=subject_id).all()

    return jsonify([
        {
            "id": t.id,
            "name": t.name,
            "description": t.description
        }
        for t in topics
    ])

@code_sprout.route("/code-sprout/topics/<int:topic_id>/subtopics")
def get_subtopics(topic_id):
    subtopics = Subtopic.query.filter_by(topic_id=topic_id).all()

    return jsonify([
        {
            "id": s.id,
            "name": s.name,
            "content": s.content
        }
        for s in subtopics
    ])

@code_sprout.route("/code-sprout/subtopics/<int:subtopic_id>/quiz")
def get_quiz(subtopic_id):
    quiz = Quiz.query.filter_by(subtopic_id=subtopic_id).first()

    if not quiz:
        return jsonify({"message": "No quiz found"}), 404

    return jsonify({
        "id": quiz.id,
        "title": quiz.title
    })

@code_sprout.route("/code-sprout/quizzes/<int:quiz_id>/questions")
def get_questions(quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()

    return jsonify([
        {
            "id": q.id,
            "question": q.question_text,
            "options": {
                "A": q.option_a,
                "B": q.option_b,
                "C": q.option_c,
                "D": q.option_d
            }
        }
        for q in questions
    ])