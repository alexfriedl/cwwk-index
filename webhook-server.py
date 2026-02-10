#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json
import hmac
import hashlib
import os

SECRET = os.environ.get('WEBHOOK_SECRET', '')

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        # Verify signature if secret is set
        if SECRET:
            signature = self.headers.get('X-Hub-Signature-256', '')
            expected = 'sha256=' + hmac.new(SECRET.encode(), body, hashlib.sha256).hexdigest()
            if not hmac.compare_digest(signature, expected):
                self.send_response(403)
                self.end_headers()
                return
        
        # Run deploy script
        try:
            result = subprocess.run(
                ['/app/deploy.sh'],
                capture_output=True,
                text=True,
                timeout=30
            )
            print(f"Deploy output: {result.stdout}")
            if result.returncode == 0:
                self.send_response(200)
            else:
                self.send_response(500)
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
