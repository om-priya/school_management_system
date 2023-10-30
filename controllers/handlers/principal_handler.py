"""Principal Handler File"""

from tabulate import tabulate
from utils import validate
from constants.principal_queries import (
    APPROVE_PRINCIPAL,
    DELETE_PRINCIPAL,
    GET_ALL_PRINCIPAL,
    GET_PRINCIPAL_BY_ID,
    UPDATE_PRINCIPAL,
)
from database.database_access import DatabaseAccess


class PrincipalHandler:
    """This is an class for super admin responsible for CRUD in principal"""

    @staticmethod
    def approve_principal(user_id):
        """Approve principal"""
        principal_id = input("Enter the id of Principal: ")

        dao = DatabaseAccess()

        dao.execute_non_returning_query(APPROVE_PRINCIPAL, (principal_id,))

    @staticmethod
    def get_all_principal(user_id):
        """Get All principals"""
        dao = DatabaseAccess()

        res_data = dao.execute_returning_query(GET_ALL_PRINCIPAL)

        if len(res_data) == 0:
            print("No Principal FOund")
            return

        print(tabulate(res_data))

    @staticmethod
    def get_principal_by_id(user_id):
        """Get Specific principal"""
        principal_id = input("Enter the id of Principal: ")

        dao = DatabaseAccess()
        res_data = dao.execute_returning_query(GET_PRINCIPAL_BY_ID, (principal_id,))

        if len(res_data) == 0:
            print("No Principal Found")
            return

        print(tabulate(res_data))

    @staticmethod
    def update_principal(user_id):
        """Update principal"""
        principal_id = input("Enter the id of Principal: ")

        field_to_update = input("Enter the field you want to update: ").lower()
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

    @staticmethod
    def delete_principal(user_id):
        """Delete principal of principal"""
        principal_id = input("Enter the id of Principal: ")

        dao = DatabaseAccess()

        dao.execute_non_returning_query(DELETE_PRINCIPAL, (principal_id,))
