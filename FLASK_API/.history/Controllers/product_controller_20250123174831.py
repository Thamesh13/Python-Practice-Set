from app import app
from Model.student_model import Student
from flask import render_template, request
import requests

calling_student = Student()

@app.route("/")
def Home():
    response = requests.get("http://127.0.0.1:5000/students")
    student_data = response.json()["Student_data"]
    print(student_data)
    # Assuming student_data is the response from an API call
    return render_template("index.html", Students=student_data, title="Student Dashboard")

    # return render_template("index.html")


@app.route("/submitform", methods=['GET', 'POST'])
def add_data():
    if request.method == "POST":
        Student_Name = request.form['Student_Name']
        Student_Age = request.form['Student_Age']
        Student_Contact_Email = request.form['Student_Contact_Email']
        Student_Contact_Number = request.form['Student_Contact_Number']

        student_data = {
            "Student": Student_Name,
            "Student_Age": Student_Age,
            "Student_Contact_Email": Student_Contact_Email,
            "Student_Contact_Number": Student_Contact_Number
        }
        response = requests.post(
            "http://127.0.0.1:5000/students", json=student_data)
        if response.status_code == 200:
            return render_template('message.html', title='Data Added Successsfully')
        else:
            return render_template('message.html', title='Failed to add student data')
    return render_template('form.html', title='Add Submit Details')


@app.route("/students")
def get_student():
    return calling_student.get_student_data()


@app.route('/students', methods=["POST"])
def post_student():
    return calling_student.post_student_data()


@app.route('/students/<id>', methods=["PUT"])
def update_student(id):
    return calling_student.update_student_data(id)


@app.route('/students/<id>', methods=["DELETE"])
def delete_student(id):
    return calling_student.delete_student_data(id)


@app.route('/students/<id>')
def get_student_id(id):
    return calling_student.get_Student_data_By_id(id)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'GET':
        student_data_dict = calling_student.get_Student_data_By_id(id)
        if student_data_dict.status_code == 200:
            return render_template('edit_form.html', student=student_data_dict['Student Data'])
        else:
            return render_template('message.html', title='Error', message='Student not found')

    elif request.method == 'POST':
        updated_data = {
            "Student_Name": request.form['Student_Name'],
            "Student_Age": request.form['Student_Age'],
            "Student_Contact_Number": request.form['Student_Contact_Number'],
            "Student_Contact_Email": request.form['Student_Contact_Email']
        }
        response = requests.put(
            f'http://127.0.0.1:5000/students/{id}', json=updated_data)
        if response.status_code == 200:
            return render_template('message.html', title='Success', message='Student updated successfully')
        else:
            return render_template('message.html', title='Error', message='Failed to update student')


@app.route('/delete/<int:id>', methods=['GET'])
def Delete_student(id):
    response = requests.delete(f'http://127.0.0.1:5000/students/{id}')
    if response.status_code == 200:
        return render_template('message.html', title='Success', message='Student deleted successfully')
    else:
        return render_template('message.html', title='Error', message='Failed to delete student')
