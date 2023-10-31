""" This module is responsible for handling all the controlers for principal """

from tabulate import tabulate
from constants import display_menu
from constants.principal_queries import GET_PRINCIPAL_BY_ID
from constants.users_query import GET_SALARY_HISTORY
from controllers.handlers.event_handler import EventHandler
from controllers.handlers.feedback_handler import FeedBackHandler
from controllers.handlers.issue_handler import IssueHandler
from controllers.handlers.leave_handler import LeaveHandler
from controllers.handlers.teacher_handler import TeacherHandler
from database.database_access import DatabaseAccess


class PrincipalController:
    """This Class is for controller functions for principal"""

    @staticmethod
    def handle_teacher(user_id):
        """It will handle all the teacher related functionality"""
        print(display_menu.HANDLE_TEACHER_PROMPT)

        user_req = input("Enter Your Query [1-5]")
        match user_req:
            case "1":
                TeacherHandler.approve_teacher(user_id=user_id)
            case "2":
                TeacherHandler.get_all_teacher(user_id=user_id)
            case "3":
                TeacherHandler.get_teacher_by_id(user_id=user_id)
            case "4":
                TeacherHandler.update_teacher(user_id=user_id)
            case "5":
                TeacherHandler.delete_teacher(user_id=user_id)
            case _:
                print("Invalid Input")

    @staticmethod
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

    @staticmethod
    def handle_events(user_id):
        """It will handle all the events related functionality"""
        print(display_menu.EVENTS_PROMPT)

        user_req = input("Enter Your Query [1-2]")
        match user_req:
            case "1":
                EventHandler.read_event(user_id=user_id)
            case "2":
                EventHandler.create_event(user_id=user_id)
            case _:
                print("Invalid Input")

    @staticmethod
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

    @staticmethod
    def view_profile(user_id):
        """View Profile of principal"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_PRINCIPAL_BY_ID, (user_id,))

        print(tabulate(res_data))

    @staticmethod
    def view_issues():
        """To view the raised Issues"""
        IssueHandler.view_issue()

    @staticmethod
    def see_salary_history(user_id):
        """Salary History of Principal"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_SALARY_HISTORY, (user_id,))

        if len(res_data) == 0:
            print("No Salary Hstory Found")

        print(tabulate(res_data))
