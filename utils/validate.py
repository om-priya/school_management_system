"""This module is responsible for validating input fields"""

import re
import maskpass


def validator(pattern, input_data):
    """General Validator which return either True or False"""
    x = re.search(pattern, input_data)
    if x is None:
        return False
    return True


def name_validator():
    """Accepted Syntax: <string> <string>"""
    name = ""
    validated = False
    while validated is False:
        name = input("Enter the name: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", name)
    return name


def gender_validator():
    """Accepted Syntax: <M/F>"""
    gender = ""
    validated = False
    while validated is False:
        gender = input("Enter gender of user (M/F): ").upper()
        validated = validator("[M,F]{1}$", gender)
    return gender


def email_validator():
    """Accepted Syntax: <alphanumeric>@<alphanumeric>.<rootUrl>"""
    validated = False
    email = ""
    while validated is False:
        email = input("Enter the email of the user: ")
        validated = validator("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", email)
    return email


def phone_validator():
    """Accepted Syntax: <int>{10}"""
    phone_no = ""
    validated = False
    while validated is False:
        phone_no = input("Enter the phone_no of the user: ")
        validated = validator("^[0-9]{10}$", phone_no)
    return phone_no


def school_name_validator():
    """Accepted Syntax: <string> <string> ..."""
    school_name = ""
    validated = False
    while validated is False:
        school_name = input("Enter the school name: ")
        validated = validator("^[A-Za-z]+([\ A-Za-z]+)*", school_name)
    return school_name


def password_validator():
    """Strong Password"""
    password = ""
    validated = False
    while validated is False:
        password = maskpass.advpass()
        validated = validator(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",
            password,
        )
    return password


def user_role_validator():
    """Only teacher or principal"""
    role = ""
    validated = False
    while validated is False:
        role = input("Enter your role: ").lower()
        if role in ["teacher", "principal"]:
            validated = True
        else:
            print("Enter either Teacher of Principal")
    return role


def experience_validator():
    """Only int less than 99"""
    experience = ""
    validated = False
    while validated is False:
        experience = input("Enter the experience of the user: ")
        validated = validator("^[0-9]{1,2}$", experience)
    return experience


def fav_subject_validator():
    """Fav Subject Only One word"""
    subject = ""
    validated = False
    while validated is False:
        subject = input("Enter subject name: ")
        validated = validator("^[a-zA-z]", subject)
    return subject


def date_validator():
    """Date Validator"""
    date_format = ""
    validated = False
    while validated is False:
        date_format = input("Enter date in format dd-mm-yyyy: ")
        validated = validator("^\\d{2}-\\d{2}-\\d{4}$", date_format)
    return date_format


def days_validator():
    """Only int less than 99"""
    experience = ""
    validated = False
    while validated is False:
        experience = input("Enter no of days: ")
        validated = validator("^[0-9]{1,2}$", experience)
    return experience
