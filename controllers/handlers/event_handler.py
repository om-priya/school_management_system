"""Event Handler File"""

from datetime import datetime
import shortuuid
import logging
from utils.validate import message_validator
from utils.pretty_print import pretty_print
from constants.insert_queries import INSERT_INTO_NOTICE
from constants.queries import READ_NOTICE

from database.database_access import DatabaseAccess

logger = logging.getLogger(__name__)


def read_event():
    """Read Events"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(READ_NOTICE)

    if len(res_data) == 0:
        logger.error("No Records On Notice Board")
        print("No Records on Notice Board")
        return

    headers = ["ID", "Message"]
    pretty_print(res_data, headers)


def create_event(user_id):
    """Create Events"""
    dao = DatabaseAccess()

    notice_id = shortuuid.ShortUUID().random(length=6)
    created_by = user_id
    notice_mssg = message_validator()
    create_date = datetime.now().strftime("%d-%m-%Y")

    # Inserting into db
    dao.execute_non_returning_query(
        INSERT_INTO_NOTICE, (notice_id, created_by, notice_mssg, create_date)
    )
    logger.info("Added to Notice Board")
    print("Successfully Added to Notice Board")
