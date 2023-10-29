"""This file contains queries related to teacher"""

GET_SCHOOL_ID = "SELECT school_id FROM school WHERE school_name = ?"
GET_APPROVED_TEACHER = """SELECT c.user_id, u.name FROM credential AS c INNER JOIN user AS u WHERE c.role = 'active'"""
