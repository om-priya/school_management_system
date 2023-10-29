"""Event Handler File"""

from datetime import datetime
import shortuuid
from tabulate import tabulate
from constants.insert_queries import INSERT_INTO_NOTICE
from constants.queries import READ_NOTICE

from database.database_access import DatabaseAccess


class EventHandler:
    """This is an class for handling event"""

    @staticmethod
    def read_event(user_id):
        """Read Events"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(READ_NOTICE)

        if len(res_data) == 0:
            print("Nothing on Notice Board")
            return

        headers = ["ID", "Message"]
        print(tabulate(res_data, headers=headers, tablefmt="grid"))

    @staticmethod
    def create_event(user_id):
        """Create Events"""
        dao = DatabaseAccess()
        notice_id = shortuuid.ShortUUID().random(length=6)
        created_by = user_id
        notice_mssg = input("Enter Your Message: ")
        create_date = datetime.now().strftime("%d-%m-%Y")

        dao.execute_non_returning_query(
            INSERT_INTO_NOTICE, (notice_id, created_by, notice_mssg, create_date)
        )
