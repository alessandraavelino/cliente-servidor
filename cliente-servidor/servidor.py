from socket import *
host = gethostname()
port = 7777
print("Conexão estabelecida em: ")
print(f'HOST: {host} , PORT {port}')
serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)
print("Aguardando conexão do cliente.")
while 1:
    con, adr = serv.accept()
    while 1:
        msg = con.recv(1024)
        print("Cliente diz:", msg.decode())
