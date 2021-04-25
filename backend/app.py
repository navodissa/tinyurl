import writeAPI

def main():
    b = writeAPI.WriteAPI()
    #b.createDB()
    #b.writeData()
    result = b.readData()
    new_Url = b.base_encode(int(result, 16))[:7]
    print (new_Url)
    b.closeConn()

if __name__ == '__main__':
    main()