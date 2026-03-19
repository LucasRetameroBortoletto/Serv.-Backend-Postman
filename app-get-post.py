from http.server import HTTPServer,BaseHTTPRequestHandler

class servidor(BaseHTTPRequestHandler):
#Metodo GET(usado anteriormente)
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Servidor em funcionamento com o GET")
#Metodo POST(novo)
    def do_POST(self):
        #identifica o tamanho dos arquivos enviados na requisição
        tamanho = int(self.headers['Content-Length']) 

        #le os dados enviados
        dados = self.rfile.read(tamanho)
        
        #Mostra os dados recebidos do terminal
        print("Dados recebidos: ", dados.decode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"POST recebido!") #retorna uma mensagem para o cliente 

HTTPServer(("0.0.0.0", 8000), servidor).serve_forever()
