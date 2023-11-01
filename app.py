""" Introduction of project """

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
    initialize_app()
    main()

#   Work For Wednesday                                     Priority            Status
# 1. Pretty print in controllers                              2                Done
# 2. Checker for ID in principal and teacher                  1                Done
# 3. Check Validation Regex to remove py lint error           3                Done
# 4. Remove user_id where not needed                          4                Done
# 5. Look into salary approve function                        5                Done
# 6. Apply regex where not implemented                        6                Done
# 7. Remove generic exception just like past one     *** Ask From Sir ***      Done
# Diagrams Implement Karo ek document me
