"""Feed Back Handler File"""

from datetime import datetime
from tabulate import tabulate
import shortuuid
from constants.insert_queries import INSERT_INTO_FEEDBACKS
from constants.queries import READ_FEEDBACKS_PRINCIPAL
from constants.teacher_queries import GET_APPROVED_TEACHER
from database.database_access import DatabaseAccess


class FeedBackHandler:
    """This is an class for feedback handler"""

    @staticmethod
    def read_feedback(user_id):
        """Read Feedbacks"""
        print("Here's the feedback given by you")
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(READ_FEEDBACKS_PRINCIPAL, (user_id,))

        if len(res_data) == 0:
            print("You have not raised any exception yet!")
            return

        headers = ["ID", "Message", "Created Date"]
        print(tabulate(res_data, headers=headers, tablefmt="grid"))

    @staticmethod
    def give_feedback(user_id):
        """Create Feedbacks"""
        print("Select User ID from the available teachers list")
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_APPROVED_TEACHER)

        if len(res_data) == 0:
            print("No Teacher Present So can't give feedback")
            return

        headers = ["ID", "Name"]
        print(tabulate(res_data, headers=headers, tablefmt="grid"))

        teacher_id = input("Enter Teacher's User ID: ")

        for data in res_data:
            if data[0] == teacher_id:
                break
        else:
            print("Wrong Teacher Id")
            return

        f_id = shortuuid.ShortUUID().random(length=6)
        f_message = input("Enter Your Feedbacks: ")
        created_date = datetime.now().strftime("%d-%m-%Y")

        dao.execute_non_returning_query(
            INSERT_INTO_FEEDBACKS, (f_id, f_message, created_date, teacher_id, user_id)
        )

        print("Feedbacks Updated")
