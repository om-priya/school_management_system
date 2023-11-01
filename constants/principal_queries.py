"""This File COntains Queries for Principal Handlers"""

APPROVE_PRINCIPAL = """UPDATE credential SET status = 'active' WHERE user_id = ? AND status = 'pending' AND role = 'principal'"""
GET_ALL_PRINCIPAL = """SELECT u.user_id, u.name, u.gender, u.email, c.status FROM user AS u INNER JOIN credential AS c ON c.user_id = u.user_id WHERE c.role = 'principal' AND c.status = 'active'"""
GET_PRINCIPAL_BY_ID = """SELECT u.user_id, u.name, u.gender, u.email, c.status FROM user AS u INNER JOIN credential AS c ON c.user_id = u.user_id WHERE c.user_id = ? AND c.role = 'principal'"""
UPDATE_PRINCIPAL = """UPDATE {} SET {} = ? WHERE user_id = ?"""
DELETE_PRINCIPAL = """UPDATE credential SET status = 'deactivate' WHERE user_id = ? AND role = 'principal'"""
FETCH_PRINCIPAL_ID = (
    """SELECT user_id FROM credential WHERE role = 'principal' AND status = 'active'"""
)
FETCH_PENDING_PRINCIPAL_ID = (
    """SELECT user_id FROM credential WHERE role = 'principal' AND status = 'pending'"""
)
