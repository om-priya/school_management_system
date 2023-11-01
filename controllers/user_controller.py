"""This module controls the login and signup functionality"""
import logging
import maskpass
from constants import users_query
from database.database_access import DatabaseAccess

from utils import validate
from models.users import Teacher, Principal, hash_password

logger = logging.getLogger(__name__)


def is_logged_in():
    """This function is for checking whether the user is valid or not,\
        this will return True/False, user_id, status, role"""
    username = input("Enter Your Username: ").lower()
    password = maskpass.advpass()
    hashed_password = hash_password(password)

    dao = DatabaseAccess()

    params = (username, hashed_password)
    data = dao.execute_returning_query(users_query.FETCH_FROM_CREDENTIALS, params)

    if len(data) == 0:
        logger.error("Wrong Credentials")
        print("Wrong Credentials")
    elif data[0][2] == "pending":
        logger.error("Pending User %s tried to logged In", data[0][0])
        print("Ask Super Admin to approve first")
    elif data[0][2] == "deactivate":
        logger.error("User %s don't exists", data[0][0])
        print("User No longer exists")
    else:
        return [True, data[0][0], data[0][1]]

    return [False, "", ""]


def sign_up():
    """This function is responsible for signing user on platform"""
    print("Welcome User")
    user_info = {}
    user_info["name"] = validate.name_validator().lower()
    user_info["gender"] = validate.gender_validator()
    user_info["email"] = validate.email_validator().lower()
    user_info["phone"] = validate.phone_validator()
    user_info["school_name"] = validate.school_name_validator().upper()
    user_info["password"] = validate.password_validator()
    user_info["role"] = validate.user_role_validator().lower()
    user_info["experience"] = validate.experience_validator()

    if user_info["role"] == "teacher":
        user_info["fav_subject"] = validate.fav_subject_validator().lower()
        new_teacher = Teacher(user_info)
        new_teacher.save_teacher()
    else:
        new_principal = Principal(user_info)
        new_principal.save_principal()
