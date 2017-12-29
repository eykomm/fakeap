#!/usr/bin/env python
# local webserver for intercepting the requests forwarded by index.php
# by s3t3bo55

import time
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):

        def do_GET(self):

                request_path = self.path

                file = open("user.log","a")


                file.write("\n")
                file.write("\n ------ Request Start ------> \n")
		file.write(time.strftime("%d/%m/%Y\t"))
		file.write(time.strftime("%H:%M:%S\n"))
                file.write(request_path + "\n")
                z = str(self.headers)
                file.write(z + "\n")
                file.write("<----- Request End ------ \n")
                file.write("\n")

                self.send_response(200)
                self.send_header("Set-Cookie", "foo=bar")

                file.close()

        def do_POST(self):

                request_path = self.path

                file = open("user.log","a")

                file.write("\n")
                file.write("\n ---- Request Start -----> \n")
                file.write(request_path + "\n")

                request_headers = self.headers
                content_length = request_headers.getheaders('content-length')
                length = int(content_length[0]) if content_length else 0

                file.write(request_headers + "\n")
                file.write(self.rfile.read(length) + "\n")
                file.write("<----- Request End ------\n")
                file.write("\n")


                self.send_response(200)

                file.close()

        do_PUT = do_POST
        do_DELETE = do_GET

def main():

	port = 65534
        print('Listening on localhost:%s' % port)
        server = HTTPServer(('172.31.1.100', port), RequestHandler)
        server.serve_forever()

if __name__ == "__main__":

        parser = OptionParser()
        parser.usage = ("Creates http server that echoes GET and POST \n"
                        "Run: \n\n"
                        " reflect")
        (option, args) = parser.parse_args()

        main()
