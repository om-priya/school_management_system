""" This File will containtain all the queries for the project """

# Queries for creating tables for database
CREATE_CREDENTIALS_TABLE = """CREATE TABLE IF NOT EXISTS credential (
    username TEXT UNIQUE,
    password TEXT,
    user_id TEXT PRIMARY KEY,
    role TEXT,
    status TEXT
)"""
CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS user (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    gender TEXT,
    email TEXT UNIQUE,
    phone TEXT
)"""
CREATE_SCHOOL_TABLE = """CREATE TABLE IF NOT EXISTS school (
    school_id TEXT PRIMARY KEY,
    school_name TEXT,
    location TEXT,
    email TEXT,
    contact TEXT
)"""
CREATE_TEACHER_TABLE = """CREATE TABLE IF NOT EXISTS teacher (
    user_id TEXT PRIMARY KEY,
    experience INTEGER,
    fav_subject TEXT
)"""
CREATE_LEAVE_TABLE = """CREATE TABLE IF NOT EXISTS leaves (
    leave_id TEXT PRIMARY KEY,
    leave_date TEXT,
    no_of_days INTEGER,
    user_id TEXT,
    status TEXT
)"""
CREATE_NOTICE_TABLE = """CREATE TABLE IF NOT EXISTS notice (
    notice_id TEXT PRIMARY KEY,
    created_by TEXT,
    notice_message TEXT,
    created_date TEXT
)"""
CREATE_ISSUES_TABLE = """CREATE TABLE IF NOT EXISTS issue (
    issue_id TEXT PRIMARY KEY,
    issue_text TEXT,
    raised_by TEXT
)"""
CREATE_FEEDBACKS_TABLE = """CREATE TABLE IF NOT EXISTS feedbacks (
    feedback_id TEXT PRIMARY KEY,
    message TEXT,
    created_date TEXT,
    given_to TEXT,
    raised_by TEXT
)"""
CREATE_ATTENDANCE_TABLE = """CREATE TABLE IF NOT EXISTS attendance (
    attendance_id TEXT PRIMARY KEY,
    user_id TEXT,
    time_in TEXT,
    time_out TEXT,
    attendance_date TEXT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
)"""
CREATE_SALARY_TABLE = """CREATE TABLE IF NOT EXISTS salary (
    salary_id TEXT PRIMARY KEY,
    user_id TEXT,
    amount INTEGER,
    year INTEGER,
    month INTEGER,
    pay_date TEXT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
)"""
CREATE_USER_SCHOOL_MAP_TABLE = """CREATE TABLE IF NOT EXISTS mapping (
    user_id TEXT PRIMARY KEY,
    school_id TEXT,
    FOREIGN KEY (school_id) REFERENCES school(school_id)
)"""
CREATE_PRINCIPAL_TABLE = """CREATE TABLE IF NOT EXISTS principal (
    user_id TEXT PRIMARY KEY,
    experience INTEGER
)"""
CREATE_STAFF_MEMBER_TABLE = """CREATE TABLE IF NOT EXISTS staff_member (
    user_id TEXT PRIMARY KEY,
    expertise TEXT,
    name TEXT,
    gender TEXT,
    address TEXT,
    phone TEXT,
    status TEXT,
    school_id TEXT
)"""
READ_NOTICE = """SELECT notice_id, notice_message FROM notice"""
READ_FEEDBACKS = """SELECT feedback_id, message, created_date FROM feedbacks WHERE given_to = ?"""
READ_FEEDBACKS_PRINCIPAL = """SELECT feedback_id, message, created_date FROM feedbacks WHERE raised_by = ?"""
