"""Staff Handler File"""

from tabulate import tabulate
import shortuuid
from constants.insert_queries import INSERT_INTO_STAFF_MEMBER
from constants.staff_queries import (
    DELETE_STAFF,
    GET_SCHOOL_ID_STAFF,
    UPDATE_STAFF,
    VIEW_ALL_STAFF,
)
from database.database_access import DatabaseAccess
from utils import validate


class StaffHandler:
    """This class contains all the functions related to staff"""

    @staticmethod
    def view_staff(user_id):
        """View Staff Members"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(VIEW_ALL_STAFF, (user_id,))

        if len(res_data) == 0:
            print("No Staff Members Found")
            return

        headers = [
            "Staff_Id",
            "expertise",
            "name",
            "phone",
            "address",
            "gender",
            "status",
            "school_id",
        ]

        print(tabulate(res_data, headers=headers, tablefmt="grid"))

    @staticmethod
    def create_staff(user_id):
        """Create Staff Members"""
        dao = DatabaseAccess()
        staff_id = shortuuid.ShortUUID().random(length=6)
        name = validate.name_validator()
        expertise = input("Enter Your Expertise Area: ")
        phone = validate.phone_validator()
        address = input("Enter Your Address: ")
        gender = validate.gender_validator()
        status = "active"

        school_id = dao.execute_returning_query(GET_SCHOOL_ID_STAFF, (user_id,))[0][0]

        dao.execute_non_returning_query(
            INSERT_INTO_STAFF_MEMBER,
            (staff_id, expertise, name, gender, address, phone, status, school_id),
        )

        print("Staff Added SuccessFully")

    @staticmethod
    def update_staff(user_id):
        """Update staff"""
        staff_id = input("Enter the Id of the staff: ")
        field_to_update = input("Enter the name of the field: ").lower()
        options = [
            "expertise",
            "name",
            "phone",
            "address",
            "gender",
        ]
        if field_to_update not in options:
            print("Wrong Input")
            return

        if field_to_update == "gender":
            updated_value = validate.gender_validator()
        elif field_to_update == "phone":
            updated_value = validate.phone_validator()
        else:
            updated_value = validate.name_validator()

        dao = DatabaseAccess()
        dao.execute_non_returning_query(
            UPDATE_STAFF.format(field_to_update), (updated_value, staff_id)
        )

    @staticmethod
    def delete_staff(user_id):
        """Delete staff"""
        staff_id = input("Enter the Id of the staff: ")
        dao = DatabaseAccess()
        dao.execute_non_returning_query(DELETE_STAFF, (staff_id,))
