from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import writeServer

hostName = "localhost"
serverPort = 8088

def main():

    webServer = HTTPServer((hostName, serverPort), writeServer.MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    main()
