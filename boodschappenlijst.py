import sqlite3


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




db = Database()
db.create_table('test', ('een text', 'twee text'))
db.add_record('test', ('afja', 'jhsdakfha'))
db.drop_table('test')
