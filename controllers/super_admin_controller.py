""" This Module is Responsible for handling super admin functionality """

import logging
from datetime import datetime
import shortuuid
from constants import display_menu
from constants.config import TEACHER_SALARY, PRINCIPAL_SALARY
from constants.insert_queries import INSERT_INTO_SALARY
from constants.principal_queries import FETCH_PRINCIPAL_ID
from constants.teacher_queries import FETCH_ACTIVE_TEACHER_ID
from constants.users_query import APPROVE_LEAVE, GET_PENDING_LEAVES
from controllers.handlers import principal_handler as PrincipalHandler
from controllers.handlers import staff_handler as StaffHandler
from database.database_access import DatabaseAccess
from utils.pretty_print import pretty_print
from utils import validate

logger = logging.getLogger(__name__)


def handle_principal():
    """Handling Principal"""
    print(display_menu.HANDLE_PRINCIPAL_PROMPT)

    user_req = input("Enter Your Query [1-5]")
    match user_req:
        case "1":
            PrincipalHandler.approve_principal()
        case "2":
            PrincipalHandler.get_all_principal()
        case "3":
            PrincipalHandler.get_principal_by_id()
        case "4":
            PrincipalHandler.update_principal()
        case "5":
            PrincipalHandler.delete_principal()
        case _:
            print("Invalid Input")


def handle_staff(user_id):
    """Handling Staff"""
    print(display_menu.HANDLE_STAFF_PROMPT)

    user_req = input("Enter Your Query [1-4]")
    match user_req:
        case "1":
            StaffHandler.view_staff(user_id=user_id)
        case "2":
            StaffHandler.create_staff(user_id=user_id)
        case "3":
            StaffHandler.update_staff()
        case "4":
            StaffHandler.delete_staff()
        case _:
            print("Invalid Input")


def distribute_salary():
    """Distribute Salary"""
    # Getting values to insert it in db
    year = datetime.now().year
    month = datetime.now().strftime("%m")
    pay_date = datetime.now().strftime("%d-%m-%Y")

    # fetching active teacher id
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_ACTIVE_TEACHER_ID)

    # Inserting into db
    if len(res_data) == 0:
        print("No Teacher's Present")
    else:
        print("Initiating Teacher Salary")
        for teacher_id in res_data[0]:
            salary_id = shortuuid.ShortUUID().random(length=6)
            salary_tuple = (
                salary_id,
                teacher_id,
                TEACHER_SALARY,
                year,
                month,
                pay_date,
            )
            dao.execute_non_returning_query(INSERT_INTO_SALARY, salary_tuple)

    # fetching active principal id
    res_data = dao.execute_returning_query(FETCH_PRINCIPAL_ID)

    # Inserting into db
    if len(res_data) == 0:
        print("No Principal Present")
    else:
        print("Initiating Principal Salary")
        for principal_id in res_data[0]:
            salary_id = shortuuid.ShortUUID().random(length=6)
            salary_tuple = (
                salary_id,
                principal_id,
                PRINCIPAL_SALARY,
                year,
                month,
                pay_date,
            )
            dao.execute_non_returning_query(INSERT_INTO_SALARY, salary_tuple)


def approve_leave():
    """Approve Leave"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_PENDING_LEAVES)

    if len(res_data) == 0:
        logger.info("No Pending Leave Request")
        print("No Pending Leave Request")
        return

    headers = ["Leave_Id", "Starting Date", "No_of_Days", "User_id", "Status"]
    pretty_print(res_data, headers)

    # will happen nothing if Id was not right
    leave_id = validate.uuid_validator("Enter the leave_id you want to approve: ")

    dao.execute_non_returning_query(APPROVE_LEAVE, (leave_id,))
