"""This file contains Issue Handler Class"""

from tabulate import tabulate
import shortuuid
from constants.insert_queries import INSERT_INTO_ISSUE
from constants.users_query import GET_ALL_ISSUES
from database.database_access import DatabaseAccess


class IssueHandler:
    """This class contains two functionality View Issue and Create Issue"""

    @staticmethod
    def view_issue():
        """Showing all the Raised Issues"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_ALL_ISSUES)

        if len(res_data) == 0:
            print("No issues Raised")
            return

        print(tabulate(res_data))

    @staticmethod
    def raise_issue(user_id):
        """To raise issue for the management"""
        issue_id = shortuuid.ShortUUID().random(length=6)
        issue_mssg = input("Enter Your Message: ")

        dao = DatabaseAccess()
        dao.execute_non_returning_query(
            INSERT_INTO_ISSUE, (issue_id, issue_mssg, user_id)
        )
        
        print("Issue Raised Successfully")
