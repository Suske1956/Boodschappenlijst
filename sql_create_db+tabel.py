import sqlite3

# connect to database in memory (temporary)
# conn = sqlite3.connect(':memory:')
# connect to database create if not exist
conn = sqlite3.connect('customers.db')

# create a cursor
c = conn.cursor()

# create table with docstring
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

# commit changes
conn.commit()

# close connection
conn.close()

