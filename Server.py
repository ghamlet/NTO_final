import http.server
import socketserver
import threading
import json

class msg:
    message = {}

class img:
    image1 = b''
    image2 = b''                                                                                                                                                                                                                                                                              

class data:
    data = ""

class GetHandler1(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/message':
            self._set_response()
            response_data = msg.message
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            msg.message = post_data

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(msg.message.encode())

class GetHandler2(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/image':
            self._set_response()
            response_data = img.image1
            self.wfile.write(response_data)

    def do_POST(self):
        if self.path == '/image':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            img.image1 = post_data.encode('utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

class GetHandler3(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/image':
            self._set_response()
            response_data = img.image2
            self.wfile.write(response_data)

    def do_POST(self):
        if self.path == '/image':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            img.image2 = post_data.encode('utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

class GetHandler4(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/data':
            self._set_response()
            response_data = data.data
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_POST(self):
        if self.path == '/data':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data.data = post_data
            print(data.data)

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(data.data.encode())


def start():
    port = [17360, 17361, 17362, 17363]
    server1 = socketserver.TCPServer(("0.0.0.0", port[0]), GetHandler1)
    server2 = socketserver.TCPServer(("0.0.0.0", port[1]), GetHandler2)
    server3 = socketserver.TCPServer(("0.0.0.0", port[2]), GetHandler3)
    server4 = socketserver.TCPServer(("0.0.0.0", port[3]), GetHandler4)

    def run_server(server):
        server.serve_forever()

    thread1 = threading.Thread(target=run_server, args=(server1,))
    thread2 = threading.Thread(target=run_server, args=(server2,))
    thread3 = threading.Thread(target=run_server, args=(server3,))
    thread4 = threading.Thread(target=run_server, args=(server4,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    print("Server started")

if __name__ == "__main__":
    start()