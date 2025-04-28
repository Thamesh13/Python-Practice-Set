import sqlite3
from flask import request,make_response
conectionstring = sqlite3.connect("College.db",check_same_thread=False)
conectionstring.row_factory=sqlite3.Row
query = conectionstring.cursor()


class student:
    def post_Student_data(Self):
        data = request.json
       
        try:
            query.execute("insert into student(Student_NAME,Student_Age,Student_Contact_number,Student_Contact_EMail) values(?,?,?,?)",tuple(data.values()))
            conectionstring.commit()
            return make_response({"Success":"Student Data added Successfully"},200)
        except Exception as e:
            return make_response({"error":f"Student Data not added Successfully and Error is {e}"},400)
    def Get_Student_data(Self):
        try:
            query.execute("Select * from student")
            
            student_data = [dict(data) for data in query.fetchall()]
            return make_response({"Success":"Data Retrived Successfully !!","Student Data":student_data},200)
        except Exception as e:
            return make_response({"Error":f"Data Retrived UnSuccessfully as {e} "},400)
    def delete_student_data(Self,id):
        if int(id)==0 or int(id)<0:
            return make_response({"error": "Invalid student ID."}, 400)

        try:
            query.execute(f"delete from Student where ID={id}")
            conectionstring.commit()
            return make_response({"Success":"Data Delete Successfully !!"},200)
        except Exception as e:
            return make_response({"Error":f"Data deleted UnSuccessfully as {e}"},400)
    def update_student_data(Self,id):
        if int(id)==0 or int(id)<0:
            return make_response({"error": "Invalid student ID."}, 400)

        data = request.json
        try:
            query.execute("Update Student set Student_Age=?,Student_Contact_EMail=?,Student_Contact_number=?,Student_NAME=? where ID=?",(data["Student_Age"], data["Student_Contact_EMail"], data["Student_Contact_number"], data["Student_NAME"], id)
            )
            conectionstring.commit()
            return make_response({"Success":"Data Update Successfully !!"},200)
        except Exception as e:
               return make_response({"Error":f"Data Update UnSuccessfully as {e}"},400)
    def Get_fillter_data(Self,id):
        try:
            query.execute(f"Select * from student where ID={id}")
            
            student_datas = [dict(data) for data in query.fetchall()]
            if student_datas==[]:
                return make_response({"Error":"Data Not Found Successfully !!","Student Data":id},400)
                
            return make_response({"Success":"Data Retrived Successfully !!","Student Data":student_datas},200)
        except Exception as e:
            return make_response({"Error":f"Data Retrived UnSuccessfully as {e} "},400)

        

                
        # try:
        #     query.execute("""
        #                     delete from Student where id={id}
        #                   """)
        #     return make_response({"Success":"Data Delete Successfully !!"},200)
        # except Exception as e:
        #     return make_response({"Error":f"Data deleted UnSuccessfully as {e}"},400)

# query.execute("""Create Table Student(
    
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     Student_NAME Varchar(50),
#     Student_Age INTEGER,
#     Student_Contact_number Varchar(50),
#     Student_Contact_EMail Varchar(50) 
#         )
#   """)


# print("Table is create successfully!!")

