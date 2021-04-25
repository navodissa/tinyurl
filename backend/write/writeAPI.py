# sqlite3, haslib modules are already ported with Python3
import sqlite3
import hashlib, math
import base62
from datetime import datetime

class WriteAPI():

    def __init__(self) :

        # Make a connection to the DB. Using the current path.
        self.conn = sqlite3.connect('tinyurl/database/urlmap.db')

        self.c = self.conn.cursor()
      

    def createDB(self):
        # Create table
        self.c.execute('''CREATE TABLE pastes
                    ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')''')

    def writeData(self, url):

        encodedUrl = url.encode()
        result = hashlib.sha256(encodedUrl).hexdigest()

        new_Url = self.base_encode(int(result, 16))[:7]
        timeNow = str(datetime.now())

        # Insert a row of data
        self.c.execute("INSERT INTO pastes ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')VALUES ( ?, 0, ?, ?)",(new_Url, timeNow, url))

        # Save (commit) the changes
        self.conn.commit()

        return new_Url

    def readData(self):

        # Query the data
        self.c.execute("SELECT * FROM pastes;")

        for shortlink, expiration_length_in_minutes, created_at, paste_path in self.c.fetchall():
            print(shortlink, expiration_length_in_minutes, created_at, paste_path)

        return result    

    def base_encode(self, num, base=62):
        digits = []
        while num > 0:
            remainder = num % base
            remainder = math.modf(remainder)
            if remainder[1] > 0:
                digits.append(int(remainder[1]))
            num = num / base
        newUrl = base62.calculate(digits)
        return newUrl

    def closeConn(self):
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        self.conn.close()
    
    









