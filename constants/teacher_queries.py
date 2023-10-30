"""This file contains queries related to teacher"""

GET_SCHOOL_ID = "SELECT school_id FROM school WHERE school_name = ?"
GET_APPROVED_TEACHER = """SELECT c.user_id, u.name FROM credential AS c INNER JOIN user AS u ON u.user_id = c.user_id WHERE c.role = 'teacher' AND c.status = 'active'"""
GET_ALL_TEACHER = """SELECT u.user_id, u.name, u.phone, c.status FROM user AS u INNER JOIN credential AS c ON u.user_id = c.user_id WHERE c.role = 'teacher'"""
APPROVE_TEACHER = """UPDATE credential SET status = 'active' WHERE user_id = ?"""
DELETE_TEACHER = """UPDATE credential SET status = 'deactivate' WHERE user_id = ?"""
GET_TEACHER_BY_ID = """SELECT u.user_id, u.name, u.phone, c.status FROM user AS u INNER JOIN credential AS c ON u.user_id = c.user_id WHERE u.user_id = ? AND c.role = 'teacher'"""
UPDATE_TEACHER = """UPDATE {} SET {} = ? WHERE user_id = ?"""
