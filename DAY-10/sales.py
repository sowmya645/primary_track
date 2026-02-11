from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

HOST = "localhost"
PORT = 8000

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Phone Case", "price": 200},
    {"id": 2, "name": "Smartphone", "price": 450},
    {"id": 3, "name": "Laptop", "price": 1000},
    {"id": 4, "name": "Headphones", "price": 150},
]


class ProductAPI(BaseHTTPRequestHandler):

    def send_json(self, status=200, data=None):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        parsed = urlparse(self.path)

        # Only handle /products
        if parsed.path != "/products":
            self.send_json(404, {"error": "Route not found"})
            return

        query = parse_qs(parsed.query)
        name = query.get("name", [None])[0]
        max_price = query.get("max_price", [None])[0]

        results = PRODUCTS

        # Partial name match
        if name:
            results = [p for p in results if name.lower() in p["name"].lower()]

        # Optional max_price filter
        if max_price:
            try:
                max_price = float(max_price)
                results = [p for p in results if p["price"] <= max_price]
            except ValueError:
                self.send_json(400, {"error": "Invalid max_price"})
                return

        self.send_json(200, results)


def run():
    server = HTTPServer((HOST, PORT), ProductAPI)
    print(f"Product API running on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()


if __name__ == "__main__":
    run()