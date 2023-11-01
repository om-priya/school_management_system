"""Leave Handler File"""

import logging
from datetime import datetime
import shortuuid
from constants.insert_queries import INSERT_INTO_LEAVES
from constants.users_query import FETCH_LEAVE_STATUS
from database.database_access import DatabaseAccess
from utils.pretty_print import pretty_print
from utils.validate import date_validator, days_validator

logger = logging.getLogger(__name__)


def apply_leave(user_id):
    """Apply Leave"""
    dao = DatabaseAccess()

    leave_id = shortuuid.ShortUUID().random(length=6)
    leave_date = date_validator()

    curr_date = datetime.now().strftime("%d-%m-%Y")

    if leave_date <= curr_date:
        print(f"{leave_date} is previous to curr date {curr_date}")
        return

    no_of_days = days_validator()

    dao.execute_non_returning_query(
        INSERT_INTO_LEAVES, (leave_id, leave_date, no_of_days, user_id, "pending")
    )

    logger.info("Applied to leave by user %s", user_id)
    print("Applied Successfully")


def see_leave_status(user_id):
    """See Leave Status"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_LEAVE_STATUS, (user_id,))

    if len(res_data) == 0:
        logger.error("No Leaves Record Found for user %s", user_id)
        print("No Leaves Record Found for You")
        return

    headers = ["Leave Date", "No of Days", "Status"]

    pretty_print(res_data, headers=headers)
