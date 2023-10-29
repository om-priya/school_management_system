"""This file contains queris for handling staff memebers"""

VIEW_ALL_STAFF = """SELECT * FROM staff_member WHERE status = 'active' \
    AND school_id = (SELECT school_id FROM mapping AS m WHERE m.user_id = ?)"""
UPDATE_STAFF = """UPDATE staff_member
                    SET {} = ?
                    WHERE user_id = ?"""
DELETE_STAFF = """UPDATE staff_member
                    SET status = 'deactivate'
                    WHERE user_id = ?"""

GET_SCHOOL_ID_STAFF = """SELECT school_id FROM mapping AS m WHERE m.user_id = ?"""
