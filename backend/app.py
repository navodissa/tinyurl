import writeAPI

def main():
    b = writeAPI.WriteAPI()
    #b.createDB()
    #b.writeDate()
    b.readData()
    b.closeConn()

if __name__ == '__main__':
    main()