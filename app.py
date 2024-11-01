# Import necessary modules from Flask
from flask import Flask, jsonify, request, abort

# Initialize the Flask app
app = Flask(__name__)

# In-memory "database" of students
students = [
    {"id": 1, "name": "Alice Smith", "grade": "A", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Johnson", "grade": "B", "email": "bob@example.com"},
]

# Route to retrieve all students (GET)
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# Route to retrieve a single student by ID (GET)
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)  # Return 404 if student not found
    return jsonify(student), 200

# Route to add a new student (POST)
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or 'name' not in request.json or 'grade' not in request.json or 'email' not in request.json:
        abort(400)  # Return 400 if required data is missing

    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    students.append(new_student)
    return jsonify(new_student), 201

# Route to update an existing student by ID (PUT)
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)  # Return 404 if student not found

    if not request.json:
        abort(400)  # Return 400 if request body is missing

    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    return jsonify(student), 200

# Route to delete a student by ID (DELETE)
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student['id'] != student_id]
    return '', 204  # Return 204 for successful deletion

# Entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
