from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse

HOST = "localhost"
PORT = 8000

notes = []  # in-memory storage

class SimpleAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return {}
        body = self.rfile.read(length)
        return json.loads(body)

    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/notes":
            # Return all notes
            self.send_json(200, notes)
        else:
            self.send_json(404, {"error": "Route not found"})

    def do_POST(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/notes":
            try:
                data = self.read_json()
            except json.JSONDecodeError:
                self.send_json(400, {"error": "Invalid JSON"})
                return

            text = data.get("text")
            if not text:
                self.send_json(400, {"error": "Missing 'text' field"})
                return

            note = {"id": len(notes) + 1, "text": text}
            notes.append(note)
            self.send_json(201, note)
        else:
            self.send_json(404, {"error": "Route not found"})


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Notes API running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()
    

