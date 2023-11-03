"""This module is responsible for validating input fields"""

import re
import maskpass

from src.config.display_menu import PromptMessage


def validator(pattern, input_data):
    """General Validator which return either True or False"""
    x = re.fullmatch(pattern, input_data)
    if x is None:
        print(PromptMessage.INVALID_INPUT.format("pattern doesn't match"))
        return False
    return True


def name_validator(prompt=PromptMessage.TAKE_INPUT.format("Name")):
    """Accepted Syntax: <string> <string>"""
    name = ""
    validated = False
    while validated is False:
        name = input(prompt)
        validated = validator(r"([A-Za-z]{2,25}[\s]?)+", name)
    return name


def gender_validator():
    """Accepted Syntax: <M/F>"""
    gender = ""
    validated = False
    while validated is False:
        gender = input(PromptMessage.TAKE_INPUT.format("Gender (M/F)")).upper()
        validated = validator("[M,F]{1}$", gender)
    return gender


def email_validator():
    """Accepted Syntax: <alphanumeric>@<alphanumeric>.<rootUrl>"""
    validated = False
    email = ""
    while validated is False:
        email = input(PromptMessage.TAKE_INPUT.format("Email"))
        validated = validator(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", email
        )
    return email


def phone_validator():
    """Accepted Syntax: <int>{10}"""
    phone_no = ""
    validated = False
    while validated is False:
        phone_no = input(PromptMessage.TAKE_INPUT.format("Phone Number"))
        validated = validator("^[0-9]{10}$", phone_no)
    return phone_no


def school_name_validator():
    """Accepted Syntax: <string> <string> ..."""
    school_name = ""
    validated = False
    while validated is False:
        school_name = input(
            PromptMessage.TAKE_INPUT.format("School Name (Only dav public school)")
        )
        validated = validator(r"^[A-Za-z]+([\sA-Za-z]+)*", school_name)
    return school_name


def password_validator():
    """Strong Password"""
    password = ""
    validated = False
    while validated is False:
        password = maskpass.advpass()
        validated = validator(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",
            password,
        )
    return password


def user_role_validator():
    """Only teacher or principal"""
    role = ""
    validated = False
    while validated is False:
        role = input(PromptMessage.TAKE_INPUT.format("Role")).lower()
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
        experience = input(PromptMessage.TAKE_INPUT.format("Experience"))
        validated = validator("^[0-9]{1,2}$", experience)
    return experience


def fav_subject_validator():
    """Fav Subject Only One word"""
    subject = ""
    validated = False
    while validated is False:
        subject = input(PromptMessage.TAKE_INPUT.format("Subject Name"))
        validated = validator(r"([a-zA-z]+[\s]?)+", subject)
    return subject


def date_validator():
    """Date Validator"""
    date_format = ""
    validated = False
    while validated is False:
        date_format = input(PromptMessage.DATE_INPUT)
        validated = validator(r"^\d{2}-\d{2}-\d{4}$", date_format)
    return date_format


def days_validator():
    """Only int less than 99"""
    experience = ""
    validated = False
    while validated is False:
        experience = input("Enter no of days: ")
        validated = validator("^[0-9]{1,2}$", experience)
    return experience


def message_validator(prompt=PromptMessage.TAKE_INPUT.format("Message")):
    """To match a paragraph of messagge"""
    message = ""
    validated = False
    while validated is False:
        message = input(prompt)
        validated = validator(r"[\w\s.,!?'\"()/-]+", message)
    return message


def uuid_validator(prompt="Enter the Id: "):
    """To match Id parameter"""
    uuid = ""
    validated = False
    while validated is False:
        uuid = input(prompt)
        validated = validator("[A-Za-z0-9]{6}", uuid)
    return uuid


def username_validator():
    """To match username"""
    username = ""
    validated = False
    while validated is False:
        username = input(PromptMessage.TAKE_INPUT.format("Username"))
        validated = validator("[A-Za-z0-9._%+-]+", username)
    return username
