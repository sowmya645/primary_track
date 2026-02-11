from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

HOST = "localhost"
PORT = 8000
ROUTES = {
    ("GET", "/users"): "get_users",
}

USERS = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "David"},
]

class SimpleAPI(BaseHTTPRequestHandler):

    # -------- Helpers --------
    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def get_query_params(self):
        parsed_url = urlparse(self.path)
        return parse_qs(parsed_url.query)

    def handle_route(self):
        parsed_url = urlparse(self.path)
        route = (self.command, parsed_url.path)

        if parsed_url.path.startswith("/users/"):
            parts = parsed_url.path.split("/")
            if len(parts) == 3 and parts[2].isdigit():
                self.get_user_by_id(int(parts[2]))
                return
            else:
                self.send_json(400, {"error": "Invalid user ID"})
                return

        handler_name = ROUTES.get(route)
        if not handler_name:
            self.send_json(404, {"error": "Route not found"})
            return

        handler = getattr(self, handler_name)
        handler()

    def do_GET(self):
        self.handle_route()

    def get_users(self):
        params = self.get_query_params()

        page = int(params.get("page", [1])[0])
        limit = int(params.get("limit", [10])[0])
        search = params.get("search", [None])[0]

        users = USERS

        if search:
            users = [u for u in users if search.lower() in u["name"].lower()]

        start = (page - 1) * limit
        end = start + limit
        paginated = users[start:end]

        self.send_json(200, {
            "page": page,
            "limit": limit,
            "total": len(users),
            "data": paginated
        })

    def get_user_by_id(self, user_id):
        user = next((u for u in USERS if u["id"] == user_id), None)
        if not user:
            self.send_json(404, {"error": "User not found"})
            return
        self.send_json(200, user)


def run():
    server = HTTPServer((HOST, PORT), SimpleAPI)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run()