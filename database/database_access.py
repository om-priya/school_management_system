""" This Module contains database access class which will help in executing query """

import logging
from database.db_connector import DatabaseConnection

logger = logging.getLogger("db_logger")


class DatabaseAccess:
    """This class will execute the query for operations"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseAccess, cls).__new__(cls)
        return cls._instance

    def execute_non_returning_query(self, query, params=None):
        """This function will execute the query of non returning type"""
        with DatabaseConnection("database\\school.db") as connection:
            cursor = connection.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

    def execute_returning_query(self, query, params=None):
        """This function will execute the query of returning type"""
        with DatabaseConnection("database\\school.db") as connection:
            cursor = connection.cursor()
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)
            data_from_db = cursor.fetchall()
        return data_from_db
