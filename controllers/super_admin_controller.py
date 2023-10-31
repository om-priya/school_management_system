""" This Module is Responsible for handling super admin functionality """

from datetime import datetime
from tabulate import tabulate
import shortuuid
from constants import display_menu
from constants.insert_queries import INSERT_INTO_SALARY
from constants.principal_queries import FETCH_PRINCIPAL_ID
from constants.teacher_queries import FETCH_ACTIVE_TEACHER_ID
from constants.users_query import APPROVE_LEAVE, GET_PENDING_LEAVES
from controllers.handlers.principal_handler import PrincipalHandler
from controllers.handlers.staff_handler import StaffHandler
from database.database_access import DatabaseAccess


class SuperAdminController:
    """This Class Contain the function of super admin"""

    @staticmethod
    def handle_principal(user_id):
        """Handling Principal"""
        print(display_menu.HANDLE_PRINCIPAL_PROMPT)

        user_req = input("Enter Your Query [1-5]")
        match user_req:
            case "1":
                PrincipalHandler.approve_principal(user_id=user_id)
            case "2":
                PrincipalHandler.get_all_principal(user_id=user_id)
            case "3":
                PrincipalHandler.get_principal_by_id(user_id=user_id)
            case "4":
                PrincipalHandler.update_principal(user_id=user_id)
            case "5":
                PrincipalHandler.delete_principal(user_id=user_id)
            case _:
                print("Invalid Input")

    @staticmethod
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
                StaffHandler.update_staff(user_id=user_id)
            case "4":
                StaffHandler.delete_staff(user_id=user_id)
            case _:
                print("Invalid Input")

    @staticmethod
    def distribute_salary(user_id):
        """Distribute Salary"""
        TEACHER_SALARY = 1000
        PRINCIPAL_SALARY = 2000

        year = datetime.now().year
        month = datetime.now().strftime("%m")
        pay_date = datetime.now().strftime("%d-%m-%Y")
        dao = DatabaseAccess()
        # fetching active teacher id
        res_data = dao.execute_returning_query(FETCH_ACTIVE_TEACHER_ID)

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

    @staticmethod
    def approve_leave(user_id):
        """Approve Leave"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_PENDING_LEAVES)

        if len(res_data) == 0:
            print("No pending Leave Request")
            return

        print(tabulate(res_data))

        leave_id = input("Enter the leave_id you want to approve: ")

        dao.execute_non_returning_query(APPROVE_LEAVE, (leave_id,))
