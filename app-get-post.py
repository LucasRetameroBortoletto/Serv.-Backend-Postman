from http.server import HTTPServer,BaseHTTPRequestHandler
#importa uma biblioteca

class servidor(BaseHTTPRequestHandler):
#Metodo GET(usado anteriormente)
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor em funcionamento com o GET!!")
#Metodo POST(novo)
    def do_POST(self):
        tamanho = int(self.headers['Content-Length']) 
        #Verifica o tamanho do arquivo enviado
        dados = self.rfile.read(tamanho)
        #Exibi os dados recebidos no terminal
        print("Dados recebidos: ", dados.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST recebido!")  
        #retorna uma mensagem para o cliente

HTTPServer(("0.0.0.0", 8000), servidor).serve_forever()
