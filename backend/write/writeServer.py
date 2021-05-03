from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import writeAPI


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Instantiate WriteAPI object
        b = writeAPI.WriteAPI()
        # Pass the path of the url avoiding leading '\'
        shortUrl = b.writeData(self.path[1:])
        b.closeConn()
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path[1:], "utf-8"))
        self.wfile.write(bytes("<p>Short URL: %s</p>" % shortUrl, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(
            bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
