import sqlite3

class DatabaseOperations:
    def __init__(self):
        self.db_name = 'boodschappenlijst.db'
        self.q_create_table = '''CREATE TABLE SqliteDb_developers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        joining_date datetime,
                                        salary REAL NOT NULL);'''
        self.q_sqlite_version = "select sqlite_version();"

    def db_operation(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            print("Successfully Connected to SQLite")

            c.execute(self.q_sqlite_version)
            conn.commit()
            record = c.fetchall()
            print("SQLite Database Version is: ", record)

            c.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if conn:
                conn.close()
                print("sqlite connection is closed")





class Database:
    def __init__(self):
        self.dbname = 'boodschappenlijst.db'

    # create table: columns is tuple example ('colname1 datatype', 'colname2 datatype')
    def create_table(self, tablename, columns):
        try:
            conn = sqlite3.connect(self.dbname)
            c = conn.cursor()
            c.execute("CREATE TABLE {} {}".format(tablename, columns))
            conn.close()
        except sqlite3.OperationalError:
            print('sqlite3 error')

    def drop_table(self, tablename):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute("DROP TABLE {}".format(tablename))
        conn.close()

    def add_record(self, tablename, data):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        c.execute("INSERT INTO {} VALUES {}".format(tablename, data))
        conn.commit()
        c.execute("SELECT * FROM test")
        print(c.fetchall())
        conn.close()

operations = DatabaseOperations()
operations.db_operation()

# db = Database()
# db.create_table('test', ('een text', 'twee text'))
# db.add_record('test', ('afja', 'jhsdakfha'))
# db.drop_table('test')
