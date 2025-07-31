from operations.students_crud import StudentCrud

obj=StudentCrud(
    student_name="vichu",
    student_age=12,
    student_dob="2005-04-09",
    parents_number="13244"
)

print(obj.add_student())