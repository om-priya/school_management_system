""" This Module Contains all the functionality that a teacher can perform """

import shortuuid
from tabulate import tabulate
from constants.insert_queries import INSERT_INTO_ISSUE
from constants.queries import READ_FEEDBACKS, READ_NOTICE
from database.database_access import DatabaseAccess


class TeacherController:
    """All these static methods contains the functionality"""

    @staticmethod
    def view_profile(user_id):
        """To view personal data for a teacher"""
        print("Profile", user_id)

    @staticmethod
    def read_notice(user_id):
        """To view notice board of a school"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(READ_NOTICE)

        if len(res_data) == 0:
            print("Nothing on Notice Board")
            return

        headers = ["ID", "Message"]
        print(tabulate(res_data, headers=headers, tablefmt="grid"))

    @staticmethod
    def read_feedbacks(user_id):
        """To view feedbacks from teacher"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(READ_FEEDBACKS, (user_id,))

        if len(res_data) == 0:
            print("Nothing on Feedbacks for You")
            return

        headers = ["ID", "Message", "Created Date"]
        print(tabulate(res_data, headers=headers, tablefmt="grid"))

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

    @staticmethod
    def salary_history(user_id):
        """To view salary history for a teacher"""
        print("salary", user_id)
