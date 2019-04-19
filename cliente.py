# pylint: disable-msg=C0103

import socket
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Cria um cliente de rede para receber mensagens.")
parser.add_argument('--host', help="Endereco do servidor")
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

# Associa o socket ao endereco e a porta especificados pelo usuario
s.connect((args.host, args.porta))
print "> Conectado a {} na porta {}...".format(args.host, args.porta)

opcoes = 1
cont = 1 # Contador de mensagens
while opcoes != 2:
    opcoes = int(raw_input("> OPCOES: 1 - Enviar nova mensagem; 2 - Sair.\n>>> "))
    if opcoes == 2:
        break
    elif opcoes == 1:
        titulo = 'MENSAGEM #{:03d} - {:%d/%m/%Y %H:%M:%S}'.format(cont, datetime.now())
        print '>', titulo
        assunto = str(raw_input("\n> ASSUNTO: "))
        texto = str(raw_input("\n> TEXTO: "))
        print '\n'
        msg = '\n---\n> {}\n\n> ASSUNTO:\n{}\n\n> TEXTO:\n{}\n---\n'.format(titulo, assunto, texto)
        s.sendall(msg) # Envia mensagem para o servidor
        cont = cont + 1
    else:
        print "> Opcao invalida. Por favor escolha entre: 1 - Enviar nova mensagem; 2 - Sair.\n>>> "

# Encerra a conexao
s.sendall('CODIGO_SAIDA')
s.close()
