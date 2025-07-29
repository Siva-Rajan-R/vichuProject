from operations.students_crud import StudentCrud


student_obj=StudentCrud(
    student_name="rahuluhh",
    student_age=20,
    student_dob="2009-09-09",
    parents_number="1234567890,097654321"
)

is_added=student_obj.fetch_student_by_name("r")

print(is_added)