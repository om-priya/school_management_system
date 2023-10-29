"""Staff Handler File"""

from tabulate import tabulate
import shortuuid
from constants.insert_queries import INSERT_INTO_STAFF_MEMBER
from constants.staff_queries import GET_SCHOOL_ID_STAFF, VIEW_ALL_STAFF
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
        expertise = validate.name_validator()
        name = validate.name_validator()
        phone = validate.phone_validator()
        address = validate.name_validator()
        gender = validate.gender_validator()
        status = "active"

        school_id = dao.execute_returning_query(GET_SCHOOL_ID_STAFF, (user_id,))[0][0]

        dao.execute_non_returning_query(
            INSERT_INTO_STAFF_MEMBER,
            (staff_id, expertise, name, phone, address, gender, status, school_id),
        )

        print("Staff Added SuccessFully")

    @staticmethod
    def update_staff(user_id):
        """Update staff"""
        print("updates", user_id)

    @staticmethod
    def delete_staff(user_id):
        """Delete staff"""
        print("deleted", user_id)
