import sqlite3

# connect to database
conn = sqlite3.connect('customers.db')

# create cursor
c = conn.cursor()



# commit command
conn.commit()


# close database
conn.close()
