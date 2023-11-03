"""This Function will run before main and create table and db"""

import logging
from src.database.db_connector import DatabaseConnection
from src.config.sqlite_queries import CreateTable

logger = logging.getLogger(__name__)


def initialize_app():
    """Create Db and super admin"""
    with DatabaseConnection("src\\database\\school.db") as connection:
        cursor = connection.cursor()
        # query to create table only once
        cursor.execute(CreateTable.CREATE_CREDENTIALS_TABLE)
        cursor.execute(CreateTable.CREATE_USERS_TABLE)
        cursor.execute(CreateTable.CREATE_USER_SCHOOL_MAP_TABLE)
        cursor.execute(CreateTable.CREATE_SCHOOL_TABLE)
        cursor.execute(CreateTable.CREATE_LEAVE_TABLE)
        cursor.execute(CreateTable.CREATE_NOTICE_TABLE)
        cursor.execute(CreateTable.CREATE_ISSUES_TABLE)
        cursor.execute(CreateTable.CREATE_FEEDBACKS_TABLE)
        cursor.execute(CreateTable.CREATE_PRINCIPAL_TABLE)
        cursor.execute(CreateTable.CREATE_TEACHER_TABLE)
        cursor.execute(CreateTable.CREATE_STAFF_MEMBER_TABLE)
        cursor.execute(CreateTable.CREATE_SALARY_TABLE)
        logger.debug("Table Created only once")
