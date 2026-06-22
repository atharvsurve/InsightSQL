# create_db.py

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite:///sales.db")

with engine.begin() as conn:

    conn.execute(text("""
        CREATE TABLE customers(

            id INTEGER PRIMARY KEY,

            name TEXT,

            city TEXT
        )
    """))

    conn.execute(text("""
        CREATE TABLE orders(

            id INTEGER PRIMARY KEY,

            customer_id INTEGER,

            amount REAL
        )
    """))

    conn.execute(text("""

        INSERT INTO customers

        VALUES

        (1,'Tesla','Texas'),

        (2,'Amazon','Seattle'),

        (3,'Google','California')

    """))

    conn.execute(text("""

        INSERT INTO orders

        VALUES

        (1,1,50000),

        (2,2,30000),

        (3,3,45000)

    """))

print("Database Created")