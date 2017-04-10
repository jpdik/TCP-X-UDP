#coding: utf-8

import socket
import sys
import os

def obter_tamanho(Bytes):
	if Bytes < 1024:
		return str(Bytes) + ' B'

	elif Bytes < (2**20):
		return str(float(Bytes/2**10)) + ' KB'

	elif Bytes < (2**30):
		return str(float(Bytes/2**20)) + ' MB'
	
	else:
		return str(float(Bytes/2**30) + float((Bytes%2**30)/1000000000)) + ' GB'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('10.3.1.36', 8888))

while True:
	s.listen(1)
	con, info_cli = s.accept()
	print 'Conexão estabelecida por', info_cli

	cont = 0

	nome = con.recv(1024)

	if not nome:
		sys.exit(0)

	con.send('nome ok')

	with open(nome, 'wb') as f:	
		while True:
			dados = con.recv(1024)
			#print dados

			if not dados:
				break

			f.write(dados)

			cont += 1024
			if cont % (100024) == 0:
				os.system('clear')
				print obter_tamanho(cont)

	print 'Arquivo (' + nome + ') Recebido. Tamanho: ' + obter_tamanho(cont)
	con.close()