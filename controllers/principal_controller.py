""" This module is responsible for handling all the controlers for principal """

import logging
from constants import display_menu
from constants.principal_queries import GET_PRINCIPAL_BY_ID
from constants.users_query import GET_SALARY_HISTORY
from controllers.handlers import event_handler as EventHandler
from controllers.handlers import feedback_handler as FeedBackHandler
from controllers.handlers import issue_handler as IssueHandler
from controllers.handlers import leave_handler as LeaveHandler
from controllers.handlers import teacher_handler as TeacherHandler
from database.database_access import DatabaseAccess
from utils.pretty_print import pretty_print

logger = logging.getLogger(__name__)


def handle_teacher():
    """It will handle all the teacher related functionality"""
    print(display_menu.HANDLE_TEACHER_PROMPT)

    user_req = input("Enter Your Query [1-5]")
    match user_req:
        case "1":
            TeacherHandler.approve_teacher()
        case "2":
            TeacherHandler.get_all_teacher()
        case "3":
            TeacherHandler.get_teacher_by_id()
        case "4":
            TeacherHandler.update_teacher()
        case "5":
            TeacherHandler.delete_teacher()
        case _:
            print("Invalid Input")


def handle_feedbacks(user_id):
    """It will handle all the feedback related functionality"""
    print(display_menu.FEEDBACK_PROMPT)

    user_req = input("Enter Your Query [1-2]")
    match user_req:
        case "1":
            FeedBackHandler.read_feedback(user_id=user_id)
        case "2":
            FeedBackHandler.give_feedback(user_id=user_id)
        case _:
            print("Invalid Input")


def handle_events(user_id):
    """It will handle all the events related functionality"""
    print(display_menu.EVENTS_PROMPT)

    user_req = input("Enter Your Query [1-2]")
    match user_req:
        case "1":
            EventHandler.read_event()
        case "2":
            EventHandler.create_event(user_id=user_id)
        case _:
            print("Invalid Input")


def handle_leaves(user_id):
    """It will handle all the leaves related functionality"""
    print(display_menu.LEAVES_PROMPT)

    user_req = input("Enter Your Query [1-2]")
    match user_req:
        case "1":
            LeaveHandler.see_leave_status(user_id=user_id)
        case "2":
            LeaveHandler.apply_leave(user_id=user_id)
        case _:
            print("Invalid Input")


def view_profile(user_id):
    """View Profile of principal"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_PRINCIPAL_BY_ID, (user_id,))

    headers = ["Id", "Name", "Gender", "email", "status"]
    pretty_print(res_data, headers)


def view_issues():
    """To view the raised Issues"""
    IssueHandler.view_issue()


def see_salary_history(user_id):
    """Salary History of Principal"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_SALARY_HISTORY, (user_id,))

    if len(res_data) == 0:
        logger.error("No salary record found for user %s", user_id)
        print("No Salary Hstory Found")
        return

    headers = ["Salary Id", "Year", "Month", "Amount", "Pay_Date"]
    pretty_print(res_data, headers)
