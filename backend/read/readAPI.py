# sqlite3, haslib modules are already ported with Python3
import sqlite3

class ReadAPI():

    def __init__(self) :

        # Make a connection to the DB. Using the current path.
        self.conn = sqlite3.connect('tinyurl/database/urlmap.db')

        self.c = self.conn.cursor()
      

    def readData(self, shortPath):

        # Query the data
        self.c.execute("""SELECT paste_path FROM pastes WHERE shortlink = ?""",(shortPath,))
        # (self.c.fetchall())

        for shortlink in self.c.fetchall():
            return shortlink

        #return result    


    def closeConn(self):
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.conn.close()
    
    









