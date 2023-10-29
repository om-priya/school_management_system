"""For saving super Admin to Db"""
import shortuuid
from models.users import hash_password
from database.database_access import DatabaseAccess
from constants import insert_queries

user_id = 'S' + shortuuid.ShortUUID().random(length=6)
school_id = shortuuid.ShortUUID().random(length=6)
name = "om priya"
gender = 'M'
email = "ompriya18153789@gmail.com"
phone = "8229070126"
role = "superadmin"
status = "active"
username = "ompriya18153789"
hashed_password = hash_password("Ompriya@123")
school_name = "DAV PUBLIC SCHOOL"
school_location = "Noida"
school_email = "dav@gmail.com"
school_contact = "3883983202"

# save these info to db
database_access_object = DatabaseAccess()

# save super admin query
# Tuples for storing info
cred_tuple = (username,hashed_password,user_id,role,status)
map_tuple = (user_id,school_id)
user_tuple = (user_id,name,gender,email,phone)
school_tuple = (school_id,school_name,school_location,school_email,school_contact)

# Execute query
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_CREDENTIAL,cred_tuple)
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_MAPPING,map_tuple)
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_USER,user_tuple)
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_SCHOOL,school_tuple)
