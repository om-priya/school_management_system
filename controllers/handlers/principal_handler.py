"""Principal Handler File"""

from utils.pretty_print import pretty_print
from utils import validate
from constants.principal_queries import (
    APPROVE_PRINCIPAL,
    DELETE_PRINCIPAL,
    FETCH_PENDING_PRINCIPAL_ID,
    FETCH_PRINCIPAL_ID,
    GET_ALL_PRINCIPAL,
    GET_PRINCIPAL_BY_ID,
    UPDATE_PRINCIPAL,
)
from database.database_access import DatabaseAccess


def get_all_principal_id():
    """Fetch All Principal Id"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_PRINCIPAL_ID)

    return res_data


def get_all_pending_id():
    """ok thik"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(FETCH_PENDING_PRINCIPAL_ID)

    return res_data


def approve_principal():
    """Approve principal"""
    principal_id = validate.uuid_validator("Enter the id of Principal: ")

    all_principal_id = get_all_principal_id()

    if len(all_principal_id) == 0:
        pending_id = get_all_pending_id()

        if len(pending_id) == 0:
            print("No request for approval")
            return

        for p_id in pending_id[0]:
            if p_id == principal_id:
                break
            else:
                print("Invalid Id's Given")
                return
        dao = DatabaseAccess()
        dao.execute_non_returning_query(APPROVE_PRINCIPAL, (principal_id,))
    else:
        print("Can't add more than one principal")
        return

    print("Principal Approved Successfully")


def get_all_principal():
    """Get All principals"""
    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_ALL_PRINCIPAL)

    if len(res_data) == 0:
        print("No Principal Found")
        return

    headers = ["User_id", "name", "gender", "email", "status"]
    pretty_print(res_data, headers)


def get_principal_by_id():
    """Get Specific principal"""
    principal_id = validate.uuid_validator("Enter the id of Principal: ")

    dao = DatabaseAccess()
    res_data = dao.execute_returning_query(GET_PRINCIPAL_BY_ID, (principal_id,))

    if len(res_data) == 0:
        print("No Principal Found")
        return

    headers = ["User_id", "name", "gender", "email", "status"]
    pretty_print(res_data, headers)


def update_principal():
    """Update principal"""
    principal_id = validate.uuid_validator("Enter the id of Principal: ")
    field_to_update = input("Enter the field you want to update: ").lower()

    all_principal_id = get_all_principal_id()

    if principal_id != all_principal_id[0][0]:
        print(f"No Such Principal With id {principal_id}")
        return

    options = ["name", "gender", "email", "phone", "experience"]

    if field_to_update not in options:
        print("No Such Field is Present")
        return

    if field_to_update in options[:4]:
        table_name = "user"
    else:
        table_name = "principal"

    match field_to_update:
        case "name":
            update_value = validate.name_validator()
        case "gender":
            update_value = validate.gender_validator()
        case "email":
            update_value = validate.email_validator()
        case "phone":
            update_value = validate.phone_validator()
        case "experience":
            update_value = validate.experience_validator()

    dao = DatabaseAccess()
    dao.execute_non_returning_query(
        UPDATE_PRINCIPAL.format(table_name, field_to_update),
        (update_value, principal_id),
    )


def delete_principal():
    """Delete principal of principal"""
    principal_id = validate.uuid_validator("Enter the id of Principal: ")

    all_principal_id = get_all_principal_id()

    if principal_id != all_principal_id[0][0]:
        print(f"No Such Principal With id {principal_id}")
        return

    dao = DatabaseAccess()
    dao.execute_non_returning_query(DELETE_PRINCIPAL, (principal_id,))
