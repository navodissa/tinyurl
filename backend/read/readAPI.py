# sqlite3 module are already ported with Python3
import sqlite3
from flask_jsonpify import jsonify

class ReadAPI():

    def __init__(self) :
        # Make a connection to the DB. Using the current path.
        self.conn = sqlite3.connect('tinyurl/database/urlmap.db')


    def get(self, shortPath):
        try:
            query = self.conn.execute("""SELECT * FROM pastes WHERE shortlink = ?""",(shortPath,))
            # Fetch the top result
            result = query.fetchone()
            # Close the DB connection
            self.conn.close()
            if result == None:
                return jsonify({'ERROR': 'Not Found', 'status' : '1'})
            # Jsonfiying the result as requested
            return jsonify({'shorturl' : result[0], 'created' : result[2], 'data' : result[3],  'status' : '1'},)
        except Exception as e:
            print(e)
            return jsonify({'status' : '0'})
 


    
    









