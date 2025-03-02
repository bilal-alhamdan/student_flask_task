from typing import Any, Dict, Optional, Tuple

from flask import Flask, Response, jsonify, request

from domain.student import Student
from infrastructure.student_repo import StudentRepository

app = Flask(__name__)
repo = StudentRepository()


@app.route('/students', methods=['GET'])
def get_students() -> Response:
    students = [student.to_dict() for student in repo.get_all()]
    return jsonify(students)


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id: int) -> Tuple[Response, int]:
    student = repo.get_by_id(student_id)
    return (jsonify(student.to_dict()),
            200) if student else (jsonify({"error": "Student not found"}), 404)


@app.route('/students', methods=['POST'])
def add_student() -> Tuple[Response, int]:
    data: Optional[Dict[str, Any]] = request.get_json()

    if not isinstance(data, dict) or 'name' not in data or 'age' not in data or 'grade' not in data:
        return jsonify({"error": "Invalid input"}), 400

    student = Student(name=str(data['name']), age=int(data['age']), grade=str(data['grade']))
    added_student = repo.add(student)
    return jsonify(added_student.to_dict()), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id: int) -> Tuple[Response, int]:
    data: Optional[Dict[str, Any]] = request.get_json()

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400

    updated_student = repo.update(student_id, data)
    return (jsonify(updated_student.to_dict()), 200) if updated_student else (
        jsonify({"error": "Student not found"}), 404)


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id: int) -> Tuple[Response, int]:
    deleted_student = repo.delete(student_id)
    return (jsonify(deleted_student.to_dict()), 200) if deleted_student else (
        jsonify({"error": "Student not found"}), 404)
