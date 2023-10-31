"""Leave Handler File"""

from tabulate import tabulate
import shortuuid
from constants.insert_queries import INSERT_INTO_LEAVES
from constants.users_query import FETCH_LEAVE_STATUS
from database.database_access import DatabaseAccess
from utils.validate import date_validator, days_validator


class LeaveHandler:
    """This class is responsible for handling leaves"""

    @staticmethod
    def apply_leave(user_id):
        """Apply Leave"""
        dao = DatabaseAccess()
        
        leave_id = shortuuid.ShortUUID().random(length=6)
        leave_date = date_validator()
        no_of_days = days_validator()

        dao.execute_non_returning_query(
            INSERT_INTO_LEAVES, (leave_id, leave_date, no_of_days, user_id, "pending")
        )

    @staticmethod
    def see_leave_status(user_id):
        """See Leave Status"""
        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(FETCH_LEAVE_STATUS, (user_id,))

        if len(res_data) == 0:
            print("No Leaves Record Found")
            return

        headers = ["Leave Date", "No of Days", "Status"]

        print(tabulate(res_data, headers=headers, tablefmt="grid"))
