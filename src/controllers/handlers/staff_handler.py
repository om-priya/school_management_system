"""Staff Handler File"""

import shortuuid
from src.config.sqlite_queries import StaffQueries
from src.config.display_menu import PromptMessage
from src.database.database_access import DatabaseAccess
from src.utils.pretty_print import pretty_print
from src.utils import validate


def view_staff(user_id):
    """View Staff Members"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(StaffQueries.VIEW_ALL_STAFF, (user_id,))

    # for no staff members
    if len(res_data) == 0:
        print(PromptMessage.NOTHING_FOUND.format("Staff"))
        return

    headers = [
        "Staff_Id",
        "expertise",
        "name",
        "phone",
        "address",
        "gender",
        "status",
        "school_id",
    ]

    pretty_print(res_data, headers=headers)


def create_staff(user_id):
    """Create Staff Members"""
    # getting info to save it in db
    staff_id = shortuuid.ShortUUID().random(length=6)
    name = validate.name_validator()
    expertise = validate.name_validator(PromptMessage.TAKE_INPUT.format("Expertise"))
    phone = validate.phone_validator()
    address = validate.name_validator(PromptMessage.TAKE_INPUT.format("Address"))
    gender = validate.gender_validator()
    status = "active"

    # fetching school id of super admin who is logged in
    dao = DatabaseAccess()
    school_id = dao.execute_returning_query(
        StaffQueries.GET_SCHOOL_ID_STAFF, (user_id,)
    )[0][0]

    # inserting info to db
    dao.execute_non_returning_query(
        StaffQueries.INSERT_INTO_STAFF_MEMBER,
        (staff_id, expertise, name, gender, address, phone, status, school_id),
    )

    print(PromptMessage.ADDED_SUCCESSFULLY.format("Staff"))


def update_staff():
    """Update staff"""
    staff_id = validate.uuid_validator(PromptMessage.TAKE_SPECIFIC_ID.format("Staff"))
    field_to_update = input(PromptMessage.FIELD_UPDATE).lower()
    options = [
        "expertise",
        "name",
        "phone",
        "address",
        "gender",
    ]

    # if wrong field is provided
    if field_to_update not in options:
        print(PromptMessage.INVALID_INPUT)
        return

    # taking updated value with input validation
    if field_to_update == "gender":
        updated_value = validate.gender_validator()
    elif field_to_update == "phone":
        updated_value = validate.phone_validator()
    else:
        updated_value = validate.name_validator(
            PromptMessage.TAKE_INPUT.format("Expertise")
        )

    # updatind value to db
    dao = DatabaseAccess()
    dao.execute_non_returning_query(
        StaffQueries.UPDATE_STAFF.format(field_to_update), (updated_value, staff_id)
    )


def delete_staff():
    """Delete staff"""
    staff_id = validate.uuid_validator(PromptMessage.TAKE_SPECIFIC_ID.format("Staff"))

    # will happen nothing if wrong id is provided
    dao = DatabaseAccess()
    dao.execute_non_returning_query(StaffQueries.DELETE_STAFF, (staff_id,))
