from http.server import HTTPServer,BaseHTTPRequestHandler

class servidor(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor Backend do claudio Funcionando")

    def do_POST(self):

        tamanho = int(self.headers['Content-Length']) 

        dados = self.rfile.read(tamanho)

        print("Dados recebidos: ", dados.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Post do cloud recebido")

HTTPServer(("0.0.0.0", 8000), servidor).serve_forever()
#comentario apenas para testar o git, porque sim.