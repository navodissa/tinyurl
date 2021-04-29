from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import readServer

hostName = "0.0.0.0"
serverPort = 8081

def main():
    
    webServer = HTTPServer((hostName, serverPort), readServer.MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    main()
