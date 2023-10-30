""" This Module is Responsible for handling super admin functionality """

from constants import display_menu
from controllers.handlers.principal_handler import PrincipalHandler
from controllers.handlers.staff_handler import StaffHandler


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
        print("Approve Leave", user_id)
