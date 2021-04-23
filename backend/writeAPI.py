import sqlite3

class WriteAPI():

    def __init__(self) :

        # Make a connection to the DB. Using the current path.
        # Try to make a relative path instead of absolute path.
        self.conn = sqlite3.connect('/home/cloud_user/tinyurl/backend/urlmap.db')

        self.c = self.conn.cursor()

    def createDB(self):
        # Create table
        self.c.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

    def writeDate(self):

        # Insert a row of data
        self.c.execute("INSERT INTO stocks VALUES ('2007-01-05','BUY','BHAT',100,36.14)")

        # Save (commit) the changes
        self.conn.commit()

    def readData(self):
        self.c.execute("SELECT * FROM stocks;")

        for date, trans, symbol, qty, price in self.c.fetchall():
            print(date, trans, symbol, qty, price)

    def closeConn(self):
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.conn.close()









