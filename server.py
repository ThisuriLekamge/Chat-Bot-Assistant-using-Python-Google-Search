import http.server
import socketserver
from google_request import chatbot_query
import os

PORT = 8080
DIRECTORY = 'templates'
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
os.chdir(template_dir)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*args, **kwargs):
    
        super().__init__(*args, **kwargs)

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        self.end_headers()
        print('user query', post_body)
        google_search_chatbot_reply = chatbot_query(post_body)
        self.wfile.write(str.encode(google_search_chatbot_reply))

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('serving at port', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()