"""This contains teacher handler functionality"""

import logging
from constants.teacher_queries import (
    APPROVE_TEACHER,
    DELETE_TEACHER,
    FETCH_ACTIVE_TEACHER_ID,
    FETCH_TEACHER_STATUS,
    GET_ALL_TEACHER,
    GET_TEACHER_BY_ID,
    UPDATE_TEACHER,
)
from database.database_access import DatabaseAccess
from utils.pretty_print import pretty_print
from utils import validate

logger = logging.getLogger(__name__)


def get_status(teacher_id):
    """This Function Will be responsible for fetching status"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_TEACHER_STATUS, (teacher_id,))

    return res_data


def fetch_active_teacher():
    """Fetching the id of active teacher"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_ACTIVE_TEACHER_ID)

    return res_data


def approve_teacher():
    """Approve Teacher"""
    teacher_id = validate.uuid_validator("Enter the id of Teacher: ")

    # fetching status of teacher with teacher_id
    status = get_status(teacher_id)

    # checks to handle edge cases
    if len(status) == 0:
        logger.error("No Teacher Present with this Id")
        print("No Teacher Present with this Id")
        return
    elif status[0][0] != "pending":
        logger.error("Teacher Can't be Approved")
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
        logger.error("No Teacher Found")
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
        logger.error("No Teacher Found")
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
        logger.info("Wrong Field Name")
        print("Wrong Field Name")
        return

    # fetching status for edge cases
    teacher_status = get_status(teacher_id)

    if len(teacher_status) == 0:
        logger.info("No Such Teacher Present")
        print("No Such Teacher Present")
        return

    if teacher_status[0][0] != "active":
        logger.info("Can't perform update action on entered user_id")
        print("Can't perform update action on entered user_id")
        return

    # getting table name and validating updated value
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

    # saving updates to db
    dao = DatabaseAccess()
    dao.execute_non_returning_query(
        UPDATE_TEACHER.format(table_name, field_to_update),
        (updated_value, teacher_id),
    )

    print("Updated Successfully")


def delete_teacher():
    """Delete Teacher of principal"""
    teacher_id = validate.uuid_validator("Enter the id of Teacher: ")

    active_teachers_id = fetch_active_teacher()

    if len(active_teachers_id) == 0:
        print("No Teacher Present to delete")
        return

    for tid in active_teachers_id[0]:
        if tid == teacher_id:
            break
    else:
        print("Teacher Can't be deleted")
        return
    dao = DatabaseAccess()
    dao.execute_non_returning_query(DELETE_TEACHER, (teacher_id,))
