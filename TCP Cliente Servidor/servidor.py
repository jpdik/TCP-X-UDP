#coding: utf-8

import socket
import time

tempo = time.time()

#Cria  objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#O argumento é uma tupla de 2 posições
s.bind(('localhost', 8888))

#Coloca o socket pra aguardar conexões, trava nessa parte
s.listen(1)

#Interrompe o fluxo de execução do programa, usa 2 variaveis pra pegar os 2 valores da tupla
con, info_cli = s.accept()
print 'Conexão estabelecida por', info_cli


while True:
	#Recebe ate 1024 bytes enviados pelo cliente
	dados = con.recv(1024)
	if not dados:
		break;
	print '\nMensagem recebida:',dados

	#Envia a mensagem de volta em letras maiusculas
	con.send(dados.upper())

con.close()
