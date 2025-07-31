from utils.uid_creation import create_unique_id
from pydantic import BaseModel
from enums.dayenum import DayEnum
from typing import TypedDict,List
from database.main import connection,cursor
import json

class FoodItems(TypedDict):
    food_name:str
    timing:str

class __FoodMenusCrudInputs(BaseModel):
    food_items:List[FoodItems]
    for_which_day:DayEnum
    

class FoodMenusCrud(__FoodMenusCrudInputs):
    def add_menu(self):
        converted_food_itm=json.dumps(self.food_items)
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS hosteL_food_menus(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    food_items TEXT,
                    day TEXT
                )
                """
            )

            cursor.execute(
                """
                INSERT INTO hostel_food_menus (food_items,day) VALUES (?,?)
                """,(converted_food_itm,self.for_which_day.value)
            )
            connection.commit()

            return "successfully hostel food menu added"
        
        except Exception as e:
            print(f"something went wrong while add hostel food menus {e}")
    

    def update_menu(self,menu_id:int):
        try:
            converted_food_itm=json.dumps(self.food_items)
            cursor.execute(
                """
                UPDATE hostel_food_menus SET food_items=?, day=? WHERE id==?
                """,(converted_food_itm,self.for_which_day.value,menu_id)
            )
            
            connection.commit()

            return "food menus updated successfully"
        
        except Exception as e:
            print(f"something went wrong while updating food menu {e}")

    def delete_menu(self,menu_id:int):
        try:
            cursor.execute(
                """
                DELETE FROM hostel_food_menus WHERE id==?
                """,(menu_id,)
            )

            connection.commit()

            return "food menu deleted successfully"
        except Exception as e:
            print(f"something went wrong while deleting food menu {e}")

    def fetch_all_menus(self):
        try:
            food_menus=cursor.execute(
                """
                SELECT * FROM hostel_food_menus
                """
            )

            return food_menus.fetchall()
        except Exception as e:
            print(f"something went wrong while fetching all menus {e}")
    
    def fetch_menus_by_day(self,day:DayEnum):
        try:
            food_menu=cursor.execute(
                """
                SELECT * FROM hostel_food_menus WHERE day==?
                """,(day.value,)
            )

            return food_menu.fetchone()
        except Exception as e:
            print(f"something went wrong while fetching menus by day {e}")
    
