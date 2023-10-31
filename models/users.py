""" This Module contains a parent class which is named as User """

import hashlib
import logging
import shortuuid

from database.database_access import DatabaseAccess
from constants import insert_queries, teacher_queries

logger = logging.getLogger(__name__)


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

    def save_teacher(self):
        """Save Teacher To DB"""
        database_access_obj = DatabaseAccess()
        school_id = database_access_obj.execute_returning_query(
            teacher_queries.GET_SCHOOL_ID, (self.school_name,)
        )
        
        if len(school_id) == 0:
            print("Wrong School Or School is not in the system")
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

        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_CREDENTIAL, cred_tuple
        )
        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_MAPPING, map_tuple
        )
        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_USER, user_tuple
        )
        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_TEACHER, teacher_tuple
        )
        logger.info("User %s Saved to Db", self.name)


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

    def save_principal(self):
        """Save Principal to DB"""
        database_access_obj = DatabaseAccess()
        school_id = database_access_obj.execute_returning_query(
            teacher_queries.GET_SCHOOL_ID, (self.school_name,)
        )
        if len(school_id) == 0:
            print("Wrong School Or School is not in the system")
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

        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_CREDENTIAL, cred_tuple
        )
        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_MAPPING, map_tuple
        )
        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_USER, user_tuple
        )
        database_access_obj.execute_non_returning_query(
            insert_queries.INSERT_INTO_PRINCIPAL, principal_tuple
        )
        logger.info("User %s Saved to Db", self.name)
