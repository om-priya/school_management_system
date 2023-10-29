"""This file contains queries to insert data into db"""

INSERT_INTO_CREDENTIAL = """INSERT INTO credential
    (username, password, user_id, role, status) 
    VALUES (?, ?, ?, ?, ?)"""
INSERT_INTO_USER = """INSERT INTO user
    (user_id, name, gender, email, phone)
    VALUES (?, ?, ?, ?, ?)"""
INSERT_INTO_MAPPING = """INSERT INTO mapping
    (user_id, school_id)
    VALUES (?, ?)"""
INSERT_INTO_SCHOOL = """INSERT INTO school
    (school_id, school_name, location, email, contact)
    VALUES (?, ?, ?, ?, ?)"""
INSERT_INTO_LEAVES = """INSERT INTO leaves
    (leave_id, leave_date, no_of_days, user_id, status)
    VALUES (?, ?, ?, ?, ?)"""
INSERT_INTO_NOTICE = """INSERT INTO notice
    (notice_id, created_by, notice_message, created_date)
    VALUES (?, ?, ?, ?)"""
INSERT_INTO_ISSUE = """INSERT INTO issue
    (issue_id, issue_text, raised_by)
    VALUES (?, ?, ?)"""
INSERT_INTO_FEEDBACKS = """INSERT INTO feedbacks
    (feedback_id, message, created_date, given_to, raised_by) 
    VALUES (?, ?, ?, ?, ?)"""
INSERT_INTO_PRINCIPAL = """INSERT INTO principal
    (user_id, experience)
    VALUES (?, ?)"""
INSERT_INTO_TEACHER = """INSERT INTO teacher
    (user_id, experience, fav_subject)
    VALUES (?, ?, ?)"""
INSERT_INTO_STAFF_MEMBER = """INSERT INTO staff_member
    (user_id, expertise, name, gender, address, phone, status, school_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
INSERT_INTO_SALARY = """INSERT INTO salary
    (salary_id, user_id, amount, year, month, pay_date)
    VALUES (?, ?, ?, ?, ?, ?)"""
INSERT_INTO_ATTENDANCE = """INSERT INTO attendance
    (attendance_id, user_id, time_in, time_out, attendance_date)
    VALUES (?, ?, ?, ?, ?)"""
