# test_db.py

from database import db

print(db.test_connection())

print(db.get_tables())

print(db.get_schema())