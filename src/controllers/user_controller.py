"""This module controls the login and signup functionality"""
import logging
from src.config.display_menu import PromptMessage
from src.config.sqlite_queries import UserQueries
from src.database.database_access import DatabaseAccess
from src.utils import validate
from src.models.users import Teacher, Principal, hash_password

logger = logging.getLogger(__name__)


def is_logged_in():
    """This function is for checking whether the user is valid or not,\
        this will return True/False, user_id, status, role"""
    # Taking Username and password and validating it
    username = validate.username_validator().lower()
    password = validate.password_validator()
    hashed_password = hash_password(password)

    # checking in db with username and password
    dao = DatabaseAccess()
    params = (username, hashed_password)
    data = dao.execute_returning_query(UserQueries.FETCH_FROM_CREDENTIALS, params)

    # Checking For Credentials with db response
    if len(data) == 0:
        logger.error("Wrong Credentials")
        print(PromptMessage.WRONG_CREDENTIALS)
    elif data[0][2] == "pending":
        logger.error("Pending User %s tried to logged In", data[0][0])
        print(PromptMessage.PENDING_USER_LOG_IN)
    elif data[0][2] == "deactivate":
        logger.error("User %s don't exists", data[0][0])
        print(PromptMessage.NOTHING_FOUND.format("User"))
    else:
        return [True, data[0][0], data[0][1]]

    return [False, "", ""]


def sign_up():
    """This function is responsible for signing user on platform"""
    print(PromptMessage.GREET_PROMPT.format("User"))
    print("\n")

    # Taking User Input For SignUp with Validations
    user_info = {}
    user_info["name"] = validate.name_validator().lower()
    user_info["gender"] = validate.gender_validator()
    user_info["email"] = validate.email_validator().lower()
    user_info["phone"] = validate.phone_validator()
    user_info["school_name"] = validate.school_name_validator().upper()
    user_info["password"] = validate.password_validator()
    user_info["role"] = validate.user_role_validator().lower()
    user_info["experience"] = validate.experience_validator()

    # Creating Object according to role and saving it
    if user_info["role"] == "teacher":
        user_info["fav_subject"] = validate.fav_subject_validator().lower()
        new_teacher = Teacher(user_info)
        logger.info("Initiating saving teacher")
        new_teacher.save_teacher()
    else:
        new_principal = Principal(user_info)
        logger.info("Initiating saving principal")
        new_principal.save_principal()
