from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MockModelHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/predict":
            self.send_error(404, "Not Found")
            return

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(body)

        query = data.get("query", "")

        # 간단한 규칙: "good" 들어있으면 긍정, "bad" 들어있으면 부정, 아니면 무조건 긍정
        if "G1" in query:
            result = "POS"
        elif "B1" in query:
            result = "NEG"
        else:
            result = "POS"

        response = {"result": result}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))


def run_mock_model_server():
    server_address = ('', 9090)
    httpd = HTTPServer(server_address, MockModelHandler)
    print("Mock model server running on http://localhost:9090")
    httpd.serve_forever()


if __name__ == "__main__":
    run_mock_model_server()
