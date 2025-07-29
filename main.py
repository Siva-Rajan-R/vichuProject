from operations.students_crud import StudentCrud
from operations.food_menus_crud import FoodMenusCrud,FoodItems
from enums.dayenum import DayEnum


student_obj=StudentCrud(
    student_name="rahuluhh",
    student_age=20,
    student_dob="2009-09-09",
    parents_number="1234567890,097654321"
)

is_added=student_obj.add_student()

print(is_added)

# obj=FoodMenusCrud(
#     food_items=[
#         FoodItems(
#             food_name="sambar satham",
#             timing="12:60 PM"
#         )
#     ],
#     for_which_day=DayEnum.MONDAY
# )

# a=obj.add_menu()

# print(a)