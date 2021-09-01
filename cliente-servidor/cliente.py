from socket import *
host = gethostname()
port = 7777
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))
while 1:
    msg = input("Digite uma mensagem: ")
    cli.send(msg.encode())
