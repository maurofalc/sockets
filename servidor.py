# pylint: disable-msg=C0103
import socket
import argparse

parser = argparse.ArgumentParser(description="Cria um servidor de rede para envio de mensagens.")
parser.add_argument('--host', help="Endereco a ser associado ao servidor")
parser.add_argument('--porta', type=int, help="Porta de comunicacao com o servidor", default=3415)
args = parser.parse_args()

# Inicializa o socket com parametros padrao
# socket_family: AF_INET (para conexao via rede)
# socket_type:   SOCK_STREAM (para uso do protocolo TCP)
# protocol:      0 (para uso dos padroes nativos do protocolo)
s = socket.socket()

# Se o host nao for fornecido por linha de comando, o host local deve ser usado
if args.host is None:
    args.host = socket.gethostname()

# Associa o host e a porta ao servidor
s.bind((args.host, args.porta))
    
# Aguarda conexao de 1 cliente
s.listen(1)

print "Servidor configurado. Aguardando conexao com cliente..."

# Armazena a conexao na variavel conn e o endereco em end.
conn, end = s.accept()
print "> Cliente {} conectou-se por meio da porta {}".format(end[0], end[1])

while True:
    msg = conn.recv(1024) # Recebe 1024 bytes da mensagem enviada pelo cliente
    if msg == 'CODIGO_SAIDA':
        break # Sai do loop se receber codigo de saida
    print msg

# Encerra a conexao
conn.close()
