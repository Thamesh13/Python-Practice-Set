import sqlite3
from app import app
from models.student_model import student
from flask import render_template
import requests



calling_student=student()

@app.route('/')
def home():
    response = requests.get("http://127.0.0.1:5000/Student")
    # response.raise_for_status()
    student_data = response.json()['Student Data']
    # print(student_data)
    return render_template('index.html',Student=student_data,title="Student Data Information")
    

@app.route('/Student')
def get_student():
    return calling_student.Get_Student_data() 
 


@app.route('/Student',methods=["POST"])
def post_student():
    return calling_student.post_Student_data()

@app.route('/Student/<id>',methods=["PUT"])
def update_student(id):
    return calling_student.update_student_data(id)

@app.route('/Student/<id>',methods=["DELETE"])
def del_student(id):
    return calling_student.delete_student_data(id)

@app.route('/Student/<id>',methods=["GET"])
def fil_student(id):
    return calling_student.Get_fillter_data(id)

