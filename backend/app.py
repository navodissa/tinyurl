import writeAPI

def main():
    b = writeAPI.WriteAPI()
    #b.createDB()
    #b.writeData()
    b.readData()
    b.closeConn()

if __name__ == '__main__':
    main()