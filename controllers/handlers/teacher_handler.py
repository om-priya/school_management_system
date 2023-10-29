"""This contains teacher handler functionality"""


class TeacherHandler:
    """This is an class for principal responsible for CRUD in teacher"""

    @staticmethod
    def approve_teacher(user_id):
        """Approve Teacher"""
        print("approved", user_id)

    @staticmethod
    def get_all_teacher(user_id):
        """Get All Teachers"""
        print("teachers", user_id)

    @staticmethod
    def get_teacher_by_id(user_id):
        """Get Specific Teacher"""
        print("teacher", user_id)

    @staticmethod
    def update_teacher(user_id):
        """Update Teacher"""
        print("updates", user_id)

    @staticmethod
    def delete_teacher(user_id):
        """Delete Teacher of principal"""
        print("deleted", user_id)
