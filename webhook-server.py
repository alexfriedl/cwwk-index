#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import os

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            result = subprocess.run(
                ['/home/alex/docker/landing-page/deploy.sh'],
                capture_output=True,
                text=True,
                timeout=30
            )
            print(f"Deploy stdout: {result.stdout}")
            print(f"Deploy stderr: {result.stderr}")
            self.send_response(200)
        except Exception as e:
            print(f"Deploy error: {e}")
            self.send_response(500)
        
        self.end_headers()
        self.wfile.write(b'OK')
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Webhook server running')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 9999), WebhookHandler)
    print('Webhook server running on port 9999')
    server.serve_forever()
