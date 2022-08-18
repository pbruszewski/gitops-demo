from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # print("Request headers:", self.headers)
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        for k,v in self.headers.items():
            self.wfile.write(bytes(f"{k}: {v}\n", "utf-8"))

def main():
    print('Listening on 0.0.0.0:8080')
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
