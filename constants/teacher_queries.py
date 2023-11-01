"""This file contains queries related to teacher"""

GET_SCHOOL_ID = "SELECT school_id FROM school WHERE school_name = ?"
GET_APPROVED_TEACHER = """SELECT c.user_id, u.name FROM credential AS c INNER JOIN user AS u ON u.user_id = c.user_id WHERE c.role = 'teacher' AND c.status = 'active'"""
GET_ALL_TEACHER = """SELECT u.user_id, u.name, u.phone, u.email, c.status FROM user AS u INNER JOIN credential AS c ON u.user_id = c.user_id WHERE c.role = 'teacher' AND c.status = 'active'"""
APPROVE_TEACHER = """UPDATE credential SET status = 'active' WHERE user_id = ? AND status = 'pending' AND role = 'teacher'"""
DELETE_TEACHER = """UPDATE credential SET status = 'deactivate' WHERE user_id = ? AND role = 'teacher'"""
GET_TEACHER_BY_ID = """SELECT u.user_id, u.name, u.phone, u.email, c.status FROM user AS u INNER JOIN credential AS c ON u.user_id = c.user_id WHERE u.user_id = ? AND c.role = 'teacher' AND c.status = 'active'"""
UPDATE_TEACHER = """UPDATE {} SET {} = ? WHERE user_id = ?"""
FETCH_ACTIVE_TEACHER_ID = (
    """SELECT user_id FROM credential WHERE role = 'teacher' AND status = 'active'"""
)
FETCH_TEACHER_STATUS = (
    """SELECT status FROM credential WHERE user_id = ? and role = 'teacher'"""
)
