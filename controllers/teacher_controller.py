""" This Module Contains all the functionality that a teacher can perform """

from tabulate import tabulate
from constants.queries import READ_FEEDBACKS, READ_NOTICE
from constants.teacher_queries import GET_TEACHER_BY_ID
from controllers.handlers.issue_handler import IssueHandler
from database.database_access import DatabaseAccess


class TeacherController:
    """All these static methods contains the functionality"""

    @staticmethod
    def view_profile(user_id):
        """To view personal data for a teacher"""
        dao = DatabaseAccess()

        res_data = dao.execute_returning_query(GET_TEACHER_BY_ID, (user_id,))

        print(tabulate(res_data))

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
        """Raise Issue"""
        IssueHandler.raise_issue(user_id)

    @staticmethod
    def salary_history(user_id):
        """To view salary history for a teacher"""
        print("salary", user_id)
