# import os
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def main():
#     return "Welcome!"

# @app.route('/how are you')
# def hello():
#     return 'I am good, how about you?'

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)

import sys
# from http.server import HTTPServer, SimpleHTTPRequestHandler #Python 3
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class PythonServer(BaseHTTPRequestHandler):
    """Python HTTP Server that handles GET and POST requests"""

    def do_GET(self):
        if self.path == '/':
            # self.path = './templates/form.html'
            # file = read_html_template(self.path)
            # html = f"<html><head></head><body><h1>Application is running !!!</h1></body></html>"
            html = "Application is running !!!" # Python 2.7

            self.send_response(200, "OK")
            self.end_headers()
            # self.wfile.write(bytes(html, "utf-8"))
            self.wfile.write(html) # Python 2.7

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), PythonServer)
    print("Server started http://localhost:8080")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped successfully")
        sys.exit(0)
