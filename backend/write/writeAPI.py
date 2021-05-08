# sqlite3, haslib modules are already ported with Python3
import sqlite3
import hashlib
import math
import base62
from datetime import datetime
from flask_jsonpify import jsonify


class WriteAPI():

    def __init__(self):
        try:
            # Make a connection to the DB. Using the current path.
            self.conn = sqlite3.connect('tinyurl/database/urlmap.db')
        except Exception as e:
            print(e)
            #return jsonify({'status' : '0'})

            
    def createDB(self):
        # Create table
        self.conn.execute('''CREATE TABLE pastes
                    ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')''')

    def writeDataAPI(self, url):
        try:
            # Passed url in the method is encoded
            encodedUrl = url.encode()
            # Getting the hexadigest after using the sha256 hashing algorithm
            result = hashlib.sha256(encodedUrl).hexdigest()

            # Converting the hexadigest into base 62 coversion. It is converted from hexadecimal to decimal in order to use in the base 62 function
            new_Url = self.base_encode(int(result, 16))[:7]

            # Getting the current time
            timeNow = str(datetime.now())

            # Insert a row of data
            self.conn.execute(
                "INSERT INTO pastes ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')VALUES ( ?, 0, ?, ?)", (new_Url, timeNow, url))

            # Save (commit) the changes
            self.conn.commit()
            self.conn.close()
            return jsonify({'shorturl' : new_Url, 'status' : '1'})
        except Exception as e:
            print (e)
            return jsonify({'status' : '0'})


    def writeData(self, url):
        try:
            # Passed url in the method is encoded
            encodedUrl = url.encode()
            # Getting the hexadigest after using the sha256 hashing algorithm
            result = hashlib.sha256(encodedUrl).hexdigest()

            # Converting the hexadigest into base 62 coversion. It is converted from hexadecimal to decimal in order to use in the base 62 function
            new_Url = self.base_encode(int(result, 16))[:7]

            # Getting the current time
            timeNow = str(datetime.now())

            # Insert a row of data
            self.conn.execute(
                "INSERT INTO pastes ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')VALUES ( ?, 0, ?, ?)", (new_Url, timeNow, url))

            # Save (commit) the changes
            self.conn.commit()
            self.conn.close()
            return new_Url
        except Exception as e:
            print (e)
            return "Your request got failed"


    # Function used for base 62 conversion
    def base_encode(self, num, base=62):
        digits = []
        while num > 0:
            remainder = num % base                  # Get the modulus of num
            # This will return the fraction and integer part as a tuple
            remainder = math.modf(remainder)
            if remainder[1] > 0:                    # If integer part is greater than 0
                # Append the remainder to digits list
                digits.append(int(remainder[1]))
            num = num / base
        # Map the base62 characters and get the new URL
        newUrl = base62.calculate(digits)
        return newUrl

    # def closeConn(self):
    #     # We can also close the connection if we are done with it.
    #     # Just be sure any changes have been committed or they will be lost.
    #     self.conn.close()
