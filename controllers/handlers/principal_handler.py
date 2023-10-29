"""Principal Handler File"""


class PrincipalHandler:
    """This is an class for super admin responsible for CRUD in principal"""

    @staticmethod
    def approve_principal(user_id):
        """Approve principal"""
        print("approved", user_id)

    @staticmethod
    def get_all_principal(user_id):
        """Get All principals"""
        print("principals", user_id)

    @staticmethod
    def get_principal_by_id(user_id):
        """Get Specific principal"""
        print("principal", user_id)

    @staticmethod
    def update_principal(user_id):
        """Update principal"""
        print("updates", user_id)

    @staticmethod
    def delete_principal(user_id):
        """Delete principal of principal"""
        print("deleted", user_id)
