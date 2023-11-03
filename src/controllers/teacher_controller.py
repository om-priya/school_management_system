""" This Module Contains all the functionality that a teacher can perform """
import logging
from src.config.display_menu import PromptMessage
from src.config.sqlite_queries import TeacherQueries, UserQueries
from src.controllers.handlers import issue_handler as IssueHandler
from src.database.database_access import DatabaseAccess
from src.utils.pretty_print import pretty_print

logger = logging.getLogger(__name__)


def view_profile(user_id):
    """To view personal data for a teacher"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(TeacherQueries.GET_TEACHER_BY_ID, (user_id,))

    headers = ["Id", "Name", "phone", "email", "status"]
    pretty_print(res_data, headers)


def read_notice():
    """To view notice board of a school"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(UserQueries.READ_NOTICE)

    if len(res_data) == 0:
        logger.error("Nothing on notice board")
        print(PromptMessage.NOTHING_FOUND.format("Notice"))
        return

    headers = ["ID", "Message"]
    pretty_print(res_data, headers=headers)


def read_feedbacks(user_id):
    """To view feedbacks from teacher"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(UserQueries.READ_FEEDBACKS, (user_id,))

    if len(res_data) == 0:
        logger.error("Nothing on Feedbacks for You")
        print(PromptMessage.NOTHING_FOUND.format("Feedback"))
        return

    headers = ["ID", "Message", "Created Date"]
    pretty_print(res_data, headers=headers)


def raise_issue(user_id):
    """Raise Issue"""
    IssueHandler.raise_issue(user_id)


def salary_history(user_id):
    """To view salary history for a teacher"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(UserQueries.GET_SALARY_HISTORY, (user_id,))

    if len(res_data) == 0:
        logger.error("No Salary Hstory Found")
        print(PromptMessage.NOTHING_FOUND.format("Salary History"))
        return

    headers = ["Salary Id", "Year", "Month", "Amount", "Pay_Date"]
    pretty_print(res_data, headers)
