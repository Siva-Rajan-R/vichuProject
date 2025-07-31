from utils.uid_creation import create_unique_id
from datetime import date
from database.main import cursor,connection
from pydantic import BaseModel

class __StudentCrudInput(BaseModel):
    student_name:str
    student_age:int
    student_dob:date
    parents_number:str

class StudentCrud(__StudentCrudInput):

    def add_student(self):
        try:
            cur=cursor
            print(self.student_name,self.student_age,self.student_dob,self.parents_number)
            print(type(self.student_name),type(self.student_age),type(self.student_dob),type(self.parents_number))
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS students(
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    dob DATE,
                    parent_number TEXT
                )
                """
            )
            print("table executed")
            std_id=create_unique_id(data=self.student_name)
            cur.execute(
                """
                INSERT INTO students (id,name,age,dob,parent_number) VALUES (?,?,?,?,?)
                """,(std_id,self.student_name,self.student_age,self.student_dob,self.parents_number)
            )

            connection.commit()
            print("student added successfully")
            return "student added successfully"
        
        except Exception as e:
            print(f"something went wrong while adding student {e}")
    
    def update_student(self,student_id:str):
        try:
            cursor.execute(
                """
                UPDATE students SET name=?, age=?, dob=?, parent_number=? WHERE id==? 
                """,(self.student_name,self.student_age,self.student_dob,self.parents_number,student_id)
            )
            connection.commit()
            return "student updated successfully"
        
        except Exception as e:
            print(f"somethig went wrong while update students {e}")
    
    def delete_student(self,student_id:str):
        try:
            cursor.execute(
                """
                DELETE FROM students WHERE id==?
                """,(student_id,)
            )

            connection.commit()

            return "student deleted successfully"
        
        except Exception as e:
            print(f"something went wrong while deleting students {e}")
    
    def fetch_all_students(self):
        try:
            students=cursor.execute(
                """
                SELECT * FROM students
                """
            )

            return students.fetchall()
        except Exception as e:
            print(f"something went wrong while fetching all students {e}")
    
    def fetch_student_by_id(self,student_id:str):
        try:
            student=cursor.execute(
                """
                SELECT * FROM students WHERE id==?
                """,(student_id,)
            )

            return student.fetchone()
        except Exception as e:
            print(f"something went wrong while fetching particular student {e}")
    
    def fetch_student_by_name(self,student_name:str):
        try:
            student=cursor.execute(
                """
                SELECT * FROM students WHERE name LIKE ?
                """,("%" + student_name + "%",)
            )

            return student.fetchall()
        
        except Exception as e:
            print(f"something went wrong while fetching particular student {e}")


