""" This Module contains a parent class which is named as User """

import hashlib
import logging
import shortuuid
from src.config.display_menu import PromptMessage

from src.database.database_access import DatabaseAccess
from src.database.db_connector import DatabaseConnection
from src.config.sqlite_queries import TeacherQueries, CreateTable, PrincipalQueries
from src.utils.exception_handler import exception_checker

logger = logging.getLogger(__name__)


# to hash the password using hashlib
def hash_password(password):
    """This function is responsible for hashing password"""
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return hashed_password


class User:
    """User class for getting basic info which will be inherited later on"""

    def __init__(self, name, gender, email, phone, school_name):
        self.name = name
        self.gender = gender
        self.email = email
        self.phone = phone
        self.school_name = school_name


class Teacher(User):
    """Teacher object which will inherit from user"""

    def __init__(self, teacher_info):
        super().__init__(
            teacher_info["name"],
            teacher_info["gender"],
            teacher_info["email"],
            teacher_info["phone"],
            teacher_info["school_name"],
        )
        self.experience = teacher_info["experience"]
        self.fav_subject = teacher_info["fav_subject"]
        self.user_id = shortuuid.ShortUUID().random(length=6)
        self.role = teacher_info["role"]
        self.password = hash_password(teacher_info["password"])
        self.status = "pending"
        self.username = teacher_info["email"].split("@")[0]

    @exception_checker
    def save_teacher(self):
        """Save Teacher To DB"""
        database_access_obj = DatabaseAccess()
        school_id = database_access_obj.execute_returning_query(
            TeacherQueries.GET_SCHOOL_ID, (self.school_name,)
        )

        if len(school_id) == 0:
            print(PromptMessage.NO_SCHOOL_FOUND)
            logger.error("No such school present in the system")
            return

        school_id = school_id[0][0]
        # creating tuple for execution
        cred_tuple = (
            self.username,
            self.password,
            self.user_id,
            self.role,
            self.status,
        )
        map_tuple = (self.user_id, school_id)
        user_tuple = (self.user_id, self.name, self.gender, self.email, self.phone)
        teacher_tuple = (self.user_id, self.experience, self.fav_subject)

        with DatabaseConnection("src\\database\\school.db") as connection:
            cursor = connection.cursor()
            cursor.execute(CreateTable.INSERT_INTO_CREDENTIAL, cred_tuple)
            cursor.execute(CreateTable.INSERT_INTO_MAPPING, map_tuple)
            cursor.execute(CreateTable.INSERT_INTO_USER, user_tuple)
            cursor.execute(TeacherQueries.INSERT_INTO_TEACHER, teacher_tuple)

        logger.info("User %s %s Saved to Db", self.name, self.role)

        logger.info("Teacher Saved to DB")
        print(PromptMessage.SIGNED_UP_SUCCESS)


class Principal(User):
    """Principal Class which will inherit from User"""

    def __init__(self, principal_info):
        super().__init__(
            principal_info["name"],
            principal_info["gender"],
            principal_info["email"],
            principal_info["phone"],
            principal_info["school_name"],
        )
        self.experience = principal_info["experience"]
        self.role = "principal"
        self.username = principal_info["email"].split("@")[0]
        self.user_id = shortuuid.ShortUUID().random(length=6)
        self.status = "pending"
        self.password = hash_password(principal_info["password"])

    @exception_checker
    def save_principal(self):
        """Save Principal to DB"""
        database_access_obj = DatabaseAccess()
        school_id = database_access_obj.execute_returning_query(
            TeacherQueries.GET_SCHOOL_ID, (self.school_name,)
        )
        if len(school_id) == 0:
            print(PromptMessage.NO_SCHOOL_FOUND)
            return

        school_id = school_id[0][0]
        # creating tuple for execution
        cred_tuple = (
            self.username,
            self.password,
            self.user_id,
            self.role,
            self.status,
        )
        map_tuple = (self.user_id, school_id)
        user_tuple = (self.user_id, self.name, self.gender, self.email, self.phone)
        principal_tuple = (self.user_id, self.experience)

        with DatabaseConnection("src\\database\\school.db") as connection:
            cursor = connection.cursor()
            cursor.execute(CreateTable.INSERT_INTO_CREDENTIAL, cred_tuple)
            cursor.execute(CreateTable.INSERT_INTO_MAPPING, map_tuple)
            cursor.execute(CreateTable.INSERT_INTO_USER, user_tuple)
            cursor.execute(PrincipalQueries.INSERT_INTO_PRINCIPAL, principal_tuple)

        logger.info("User %s %s Saved to Db", self.name, self.role)

        logger.info("Principal Saved to DB")
        print(PromptMessage.NO_SCHOOL_FOUND)
