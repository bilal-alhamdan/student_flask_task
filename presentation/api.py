from flask import Flask, jsonify, request

from domain.student import Student
from infrastructure.student_repo import StudentRepository

app = Flask(__name__)
repo = StudentRepository()


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([student.to_dict() for student in repo.get_all()])


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = repo.get_by_id(student_id)
    return jsonify(student.to_dict()) if student else ('', 404)


@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student = Student(name=data['name'], age=data['age'], grade=data['grade'])
    added_student = repo.add(student)
    return jsonify(added_student.to_dict()), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    updated_student = repo.update(student_id, data)
    return jsonify(updated_student.to_dict()) if updated_student else ('', 404)


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    deleted_student = repo.delete(student_id)
    return jsonify(deleted_student.to_dict()) if deleted_student else ('', 404)
