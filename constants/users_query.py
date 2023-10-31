"""This file contains some query which will be used in operations"""

FETCH_FROM_CREDENTIALS = (
    "SELECT user_id, role, status FROM credential WHERE username = ? AND password = ?"
)
FETCH_LEAVE_STATUS = (
    """SELECT leave_date, no_of_days, status FROM leaves WHERE user_id = ?"""
)
GET_PENDING_LEAVES = """SELECT * FROM leaves WHERE status = 'pending'"""
APPROVE_LEAVE = """UPDATE leaves SET status = 'approved' WHERE leave_id = ?"""
GET_ALL_ISSUES = """SELECT * FROM issue"""
GET_SALARY_HISTORY = """SELECT salary_id, year, month, amount, pay_date FROM salary WHERE user_id = ? ORDER BY year DESC, month ASC"""
