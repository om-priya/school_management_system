"""This file contains Issue Handler Class"""

import logging
import shortuuid
from constants.insert_queries import INSERT_INTO_ISSUE
from constants.users_query import GET_ALL_ISSUES
from database.database_access import DatabaseAccess
from utils.pretty_print import pretty_print
from utils.validate import message_validator

logger = logging.getLogger(__name__)


def view_issue():
    """Showing all the Raised Issues"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_ALL_ISSUES)

    if len(res_data) == 0:
        logger.error("No issues Found")
        print("No issues Raised")
        return

    headers = ["issue_id", "issue_text", "raised_by"]
    pretty_print(res_data, headers)


def raise_issue(user_id):
    """To raise issue for the management"""
    issue_id = shortuuid.ShortUUID().random(length=6)
    issue_mssg = message_validator("Enter Your Issues: ")

    dao = DatabaseAccess()
    dao.execute_non_returning_query(INSERT_INTO_ISSUE, (issue_id, issue_mssg, user_id))

    logger.info("Issue Created Successfully")
    print("Issue Raised Successfully")
