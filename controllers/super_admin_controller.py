""" This Module is Responsible for handling super admin functionality """

from tabulate import tabulate
from constants import display_menu
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
        print("Distribute Salary", user_id)

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
