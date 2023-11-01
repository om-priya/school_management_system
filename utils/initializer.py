"""This Function will run before main and create table and db"""

import logging
from database.db_connector import DatabaseConnection
from constants import queries

logger = logging.getLogger(__name__)


def initialize_app():
    """Create Db and super admin"""
    with DatabaseConnection("database\\school.db") as connection:
        cursor = connection.cursor()
        # query to create table only once
        cursor.execute(queries.CREATE_CREDENTIALS_TABLE)
        cursor.execute(queries.CREATE_USERS_TABLE)
        cursor.execute(queries.CREATE_USER_SCHOOL_MAP_TABLE)
        cursor.execute(queries.CREATE_SCHOOL_TABLE)
        cursor.execute(queries.CREATE_LEAVE_TABLE)
        cursor.execute(queries.CREATE_NOTICE_TABLE)
        cursor.execute(queries.CREATE_ISSUES_TABLE)
        cursor.execute(queries.CREATE_FEEDBACKS_TABLE)
        cursor.execute(queries.CREATE_PRINCIPAL_TABLE)
        cursor.execute(queries.CREATE_TEACHER_TABLE)
        cursor.execute(queries.CREATE_STAFF_MEMBER_TABLE)
        cursor.execute(queries.CREATE_SALARY_TABLE)
        logger.debug("Table Created only once")
