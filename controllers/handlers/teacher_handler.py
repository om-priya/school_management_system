"""This contains teacher handler functionality"""


from tabulate import tabulate
from constants.teacher_queries import (
    APPROVE_TEACHER,
    DELETE_TEACHER,
    GET_ALL_TEACHER,
    GET_TEACHER_BY_ID,
    UPDATE_TEACHER,
)
from database.database_access import DatabaseAccess
from utils import validate


class TeacherHandler:
    """This is an class for principal responsible for CRUD in teacher"""

    @staticmethod
    def approve_teacher(user_id):
        """Approve Teacher"""
        teacher_id = input("Enter the id of Teacher: ")
        dao = DatabaseAccess()

        dao.execute_non_returning_query(APPROVE_TEACHER, (teacher_id,))

    @staticmethod
    def get_all_teacher(user_id):
        """Get All Teachers"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_ALL_TEACHER)

        if len(res_data) == 0:
            print("No Teacher Found")

        print(tabulate(res_data))

    @staticmethod
    def get_teacher_by_id(user_id):
        """Get Specific Teacher"""
        teacher_id = input("Enter the id of Teacher: ")
        dao = DatabaseAccess()

        res_data = dao.execute_returning_query(GET_TEACHER_BY_ID, (teacher_id,))

        if len(res_data) == 0:
            print("No Teacher Found")

        print(tabulate(res_data))

    @staticmethod
    def update_teacher(user_id):
        """Update Teacher"""
        teacher_id = input("Enter the id of teacher: ")
        field_to_update = input("Enter the field you want to update: ")
        options = ["name", "phone", "email", "experience", "designation"]

        if field_to_update not in options:
            print("Wrong Field Name")
            return

        if field_to_update in options[:3]:
            table_name = "user"
            if field_to_update == "name":
                updated_value = validate.name_validator()
            elif field_to_update == "phone":
                updated_value = validate.phone_validator()
            else:
                updated_value = validate.email_validator()
        else:
            table_name = "teacher"
            if field_to_update == "experience":
                updated_value = validate.experience_validator()
            else:
                updated_value = validate.name_validator()

        dao = DatabaseAccess()
        dao.execute_non_returning_query(
            UPDATE_TEACHER.format(table_name, field_to_update),
            (updated_value, teacher_id),
        )

        print("Updated Successfully")

    @staticmethod
    def delete_teacher(user_id):
        """Delete Teacher of principal"""
        teacher_id = input("Enter the id of Teacher: ")
        dao = DatabaseAccess()

        dao.execute_non_returning_query(DELETE_TEACHER, (teacher_id,))
