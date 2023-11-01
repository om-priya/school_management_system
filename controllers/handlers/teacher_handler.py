"""This contains teacher handler functionality"""

from constants.teacher_queries import (
    APPROVE_TEACHER,
    DELETE_TEACHER,
    FETCH_TEACHER_STATUS,
    GET_ALL_TEACHER,
    GET_TEACHER_BY_ID,
    UPDATE_TEACHER,
)
from database.database_access import DatabaseAccess
from utils.pretty_print import pretty_print
from utils import validate


def get_status(teacher_id):
    """This Function Will be responsible for fetching status"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_TEACHER_STATUS, (teacher_id,))

    return res_data


def approve_teacher():
    """Approve Teacher"""
    teacher_id = validate.uuid_validator("Enter the id of Teacher: ")

    # fetching status of teacher with teacher_id
    status = get_status(teacher_id)

    # checks to handle edge cases
    if len(status) == 0:
        print("No Teacher Present with this Id")
        return
    elif status[0][0] != "pending":
        print("Teacher Can't be Approved")
        return
    else:
        # executing the query
        dao = DatabaseAccess()
        dao.execute_non_returning_query(APPROVE_TEACHER, (teacher_id,))

    print("Teacher Approved SuccessFully")


def get_all_teacher():
    """Get All Teachers"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_ALL_TEACHER)

    if len(res_data) == 0:
        print("No Teacher Found")
        return

    headers = ["Id", "Name", "phone", "email", "status"]
    pretty_print(res_data, headers)


def get_teacher_by_id():
    """Get Specific Teacher"""
    teacher_id = validate.uuid_validator("Enter the id of Teacher: ")

    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_TEACHER_BY_ID, (teacher_id,))

    if len(res_data) == 0:
        print("No Teacher Found")
        return

    headers = ["Id", "Name", "phone", "email", "status"]
    pretty_print(res_data, headers)


def update_teacher():
    """Update Teacher"""
    teacher_id = validate.uuid_validator("Enter the id of Teacher: ")
    field_to_update = input("Enter the field you want to update: ")
    options = ["name", "phone", "email", "experience", "designation"]

    # checking whether entered field is correct or not
    if field_to_update not in options:
        print("Wrong Field Name")
        return

    # fetching status for edge cases
    teacher_status = get_status(teacher_id)

    if len(teacher_status) == 0:
        print("No Such Teacher Present")
        return

    if teacher_status[0][0] != "active":
        print("Can't perform update action on entered user_id")

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
            updated_value = validate.name_validator("Enter Your Designation: ")

    dao = DatabaseAccess()
    dao.execute_non_returning_query(
        UPDATE_TEACHER.format(table_name, field_to_update),
        (updated_value, teacher_id),
    )

    print("Updated Successfully")


def delete_teacher():
    """Delete Teacher of principal"""
    teacher_id = validate.uuid_validator("Enter the id of Teacher: ")

    dao = DatabaseAccess()
    dao.execute_non_returning_query(DELETE_TEACHER, (teacher_id,))
