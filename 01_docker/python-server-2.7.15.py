

import SimpleHTTPServer
import SocketServer

PORT = 8080
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = Socket.Server.TCPServer(("",PORT), Handler)
httpd.serve_forever()
