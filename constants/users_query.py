"""This file contains some query which will be used in operations"""

FETCH_FROM_CREDENTIALS = (
    "SELECT user_id, role, status FROM credential WHERE username = ? AND password = ?"
)
FETCH_LEAVE_STATUS = (
    """SELECT leave_date, no_of_days, status FROM leaves WHERE user_id = ?"""
)
