# sqlite3, haslib modules are already ported with Python3
import sqlite3
import hashlib, math
import base62

class WriteAPI():

    def __init__(self) :

        # Make a connection to the DB. Using the current path.
        self.conn = sqlite3.connect('tinyurl/database/urlmap.db')

        self.c = self.conn.cursor()

    def calculate(digits):
        digitsCount = len(digits)
        hashString = ""
        i = 0
        while digitsCount > i:
            hashString += BASE62ALPHABET[digits[i]] 
            i = i + 1
        return hashString
        

    def createDB(self):
        # Create table
        self.c.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

    def writeData(self, url):

        result = hashlib.sha256(url).hexdigest()
        print (result)

        # Insert a row of data
        self.c.execute("INSERT INTO stocks VALUES ('2007-01-05','BUY','BHAT',100,36.14)")

        # Save (commit) the changes
        self.conn.commit()

    def readData(self):

        url = ('https://www.google.lk').encode()
        result = hashlib.sha256(url).hexdigest()
        print (result)

        # Query the data
        self.c.execute("SELECT * FROM stocks;")

        for date, trans, symbol, qty, price in self.c.fetchall():
            print(date, trans, symbol, qty, price)

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
    
    









