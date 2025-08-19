import json
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import requests

# 전역 데이터 저장소
dictionary = {}
stopwords = set()
models = []

# 데이터 로드 함수들
def load_dictionary(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            key, value = line.strip().split(None, 1)
            dictionary[key.lower()] = value

def load_stopwords(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            stopwords.add(line.strip())

def load_models(path):
    global models
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        models = data["models"]

# 전처리 함수
def preprocess(sentence):
    tokens = re.split(r'\s+', sentence.strip())
    vectors = []
    for token in tokens:
        key = token.lower()
        vector = dictionary.get(key)
        if vector and vector not in stopwords:
            vectors.append(vector)
    return ' '.join(vectors)

# 모델 서버에 POST 요청
def request_model(url, processed):
    headers = {'Content-Type': 'application/json'}
    payload = {'query': processed}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result.get('result', 'unknown')

# HTTP 요청 핸들러
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/":
            self.send_error(404, "Not Found")
            return

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        request_json = json.loads(body)

        modelname = request_json.get('modelname')
        queries = request_json.get('queries', [])

        model = next((m for m in models if m['modelname'] == modelname), None)

        if model is None:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Model not found"}).encode('utf-8'))
            return

        results = []
        for query in queries:
            processed = preprocess(query)
            try:
                code = request_model(model['url'], processed)
                value = next((c['value'] for c in model['classes'] if c['code'] == code), "unknown")
                results.append(value)
            except Exception as e:
                results.append("error")

        response_json = {"results": results}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_json).encode('utf-8'))

# 서버 실행 함수
def run_server():
    load_dictionary('DICTIONARY.TXT')
    load_stopwords('STOPWORD.TXT')
    load_models('MODELS.JSON')

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on http://localhost:8080")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()