from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import readAPI


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        b = readAPI.ReadAPI()
        longPath = b.readData(self.path[1:])
        b.closeConn()
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path[1:], "utf-8"))
        self.wfile.write(bytes("<p>Short URL: %s</p>" % longPath, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
