import http.server
import os
import json
import base64
import mimetypes
import urllib.parse

TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_temp')
os.makedirs(TEMP_DIR, exist_ok=True)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
                filename = data.get('filename', 'file')
                file_content = base64.b64decode(data.get('content', ''))
                filepath = os.path.join(TEMP_DIR, filename)
                with open(filepath, 'wb') as f:
                    f.write(file_content)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'url': '/_temp/' + filename}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    port = 8080
    server = http.server.HTTPServer(('localhost', port), Handler)
    print(f'稿子菌服务器已启动: http://localhost:{port}')
    print(f'临时文件目录: {TEMP_DIR}')
    server.serve_forever()
