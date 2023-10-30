""" Introduction of project """

import logging

from constants import display_menu
from controllers.teacher_controller import TeacherController
from controllers.principal_controller import PrincipalController
from controllers.super_admin_controller import SuperAdminController
from controllers.user_controller import UserController

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename="logs.txt",
)

logger = logging.getLogger(__name__)


def main():
    """This Function is responsible for making my app run contineously"""
    is_logged_in = False
    user_id = ""
    role = ""

    while True:
        while not is_logged_in:
            print(display_menu.ENTRY_POINT_PROMPT)
            user_req = input("Enter your Query: ")
            if user_req == "1":
                is_logged_in, user_id, role = UserController.is_logged_in()
            elif user_req == "2":
                UserController.sign_up()
            else:
                print("Invalid Input")

        logger.info("Logged in user: %s, role: %s", user_id, role)
        while True:
            if role == "superadmin":
                print(display_menu.SUPER_ADMIN_MAIN_PROMPT)
                user_req = input("Enter Your Query [1-5]: ")
                while True:
                    match user_req:
                        case "1":
                            SuperAdminController.handle_principal(user_id=user_id)
                        case "2":
                            SuperAdminController.handle_staff(user_id=user_id)
                        case "3":
                            SuperAdminController.distribute_salary(user_id=user_id)
                        case "4":
                            SuperAdminController.approve_leave(user_id=user_id)
                        case "5":
                            is_logged_in = False
                            user_id = None
                            role = None
                        case _:
                            print("Invalid Input Enter only [1-5]")
                    if user_req == "5":
                        break
                    print(display_menu.SUPER_ADMIN_MAIN_PROMPT)
                    user_req = input("Enter Your Query [1-5]: ")
                break
            elif role == "principal":
                print(display_menu.PRINCIPAL_MAIN_PROMPT)
                user_req = input("Enter Your Query [1-7]: ")
                while True:
                    match user_req:
                        case "1":
                            PrincipalController.handle_teacher(user_id=user_id)
                        case "2":
                            PrincipalController.handle_feedbacks(user_id=user_id)
                        case "3":
                            PrincipalController.handle_events(user_id=user_id)
                        case "4":
                            PrincipalController.handle_leaves(user_id=user_id)
                        case "5":
                            PrincipalController.view_profile(user_id=user_id)
                        case "6":
                            PrincipalController.see_salary_history(user_id=user_id)
                        case "7":
                            is_logged_in = False
                            user_id = None
                            role = None
                            break
                        case _:
                            print("Invalid Input Enter only [1-7]")
                    print(display_menu.PRINCIPAL_MAIN_PROMPT)
                    user_req = input("Enter Your Query [1-7]: ")
                break
            elif role == "teacher":
                print(display_menu.TEACHER_MAIN_PROMPT)
                user_req = input("Enter Your Query [1-6]: ")
                while True:
                    match user_req:
                        case "1":
                            TeacherController.view_profile(user_id=user_id)
                        case "2":
                            TeacherController.read_notice(user_id=user_id)
                        case "3":
                            TeacherController.read_feedbacks(user_id=user_id)
                        case "4":
                            TeacherController.raise_issue(user_id=user_id)
                        case "5":
                            TeacherController.salary_history(user_id=user_id)
                        case "6":
                            is_logged_in = False
                            user_id = None
                            role = None
                            break
                        case _:
                            print("Invalid Input Enter only [1-6]")
                    print(display_menu.TEACHER_MAIN_PROMPT)
                    user_req = input("Enter Your Query [1-6]: ")
                break
            else:
                print("You are not approved yet!")


if __name__ == "__main__":
    main()
