""" This project aims to provide a management system for a school 
through which they can manage different entities in their school. 
The base assumption of this project is that it manages with the perspective of one school """

import logging

from constants import display_menu
from menu import super_admin_menu, principal_menu, teacher_menu
from controllers import user_controller as UserController
from utils.initializer import initialize_app

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    level=logging.DEBUG,
    filename="logs.log",
)

logger = logging.getLogger(__name__)


def main():
    """This Function is responsible for making my app run contineously"""

    # setting initial value to default
    is_logged_in = False
    user_id = ""
    role = ""

    while True:
        # For login and signup
        while not is_logged_in:
            print(display_menu.ENTRY_POINT_PROMPT)

            user_req = input("Enter your Query: ")
            if user_req == "1":
                # Function returning 3 things
                is_logged_in, user_id, role = UserController.is_logged_in()
            elif user_req == "2":
                # saving to db with status pending
                UserController.sign_up()
            else:
                print("Invalid Input")

        logger.info("Logged in user: %s, role: %s", user_id, role)

        while True:
            if role == "superadmin":
                super_admin_menu(user_id=user_id)
            elif role == "principal":
                principal_menu(user_id=user_id)
            elif role == "teacher":
                teacher_menu(user_id=user_id)
            else:
                print("You don't have access to the protal")
            # Resetting the variable due to logged out functionality
            is_logged_in = False
            user_id = ""
            role = ""
            break


if __name__ == "__main__":
    # created db with all the tables and run main function
    initialize_app()
    main()
