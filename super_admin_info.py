"""For saving super Admin to Db"""
import shortuuid
from models.users import hash_password
from database.database_access import DatabaseAccess
from constants import insert_queries

USER_ID = 'S' + shortuuid.ShortUUID().random(length=6)
SCHOOL_ID = shortuuid.ShortUUID().random(length=6)
NAME = "om priya"
GENDER = 'M'
EMAIL = "ompriya18153789@gmail.com"
PHONE = "8229070126"
ROLE = "superadmin"
STATUS = "active"
USER_NAME = "ompriya18153789"
HASHED_PASSWORD = hash_password("Ompriya@123")
SCHOOL_NAME = "DAV PUBLIC SCHOOL"
SCHOOL_LOCATION = "Noida"
SCHOOL_EMAIL = "dav@gmail.com"
SCHOOL_CONTACT = "3883983202"

# save these info to db
database_access_object = DatabaseAccess()

# save super admin query
# Tuples for storing info
cred_tuple = (USER_NAME,HASHED_PASSWORD,USER_ID,ROLE,STATUS)
map_tuple = (USER_ID,SCHOOL_ID)
user_tuple = (USER_ID,NAME,GENDER,EMAIL,PHONE)
school_tuple = (SCHOOL_ID,SCHOOL_NAME,SCHOOL_LOCATION,SCHOOL_EMAIL,SCHOOL_CONTACT)

# Execute query
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_CREDENTIAL,cred_tuple)
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_MAPPING,map_tuple)
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_USER,user_tuple)
database_access_object.execute_non_returning_query(insert_queries.INSERT_INTO_SCHOOL,school_tuple)