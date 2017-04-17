#coding: utf-8

import socket
from hashlib import md5
import time
import os
import sys

sys.path.insert(0, os.getcwd()[:os.getcwd().rfind('/')])

import constantes as C

comecou = 0

#Cria  objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#O argumento é uma tupla de 2 posições
s.bind((C.IP, C.PORTA))

#Coloca o socket pra aguardar conexões, trava nessa parte
s.listen(1)

#Interrompe o fluxo de execução do programa, usa 2 variaveis pra pegar os 2 valores da tupla
con, info_cli = s.accept()
print 'Conexão estabelecida por', info_cli

md = md5()

f = open(C.NOME,'wb')

while True:
	#Recebe ate 1024 bytes enviados pelo cliente
	dados = con.recv(2048)
	if comecou == 0:
		tempo = time.time()
		comecou = 1
	
	if not dados:
		break;

	f.write(dados)

	md.update(dados)

f.close()

print 'tempo: ' + str(time.time()-tempo)
print 'tamanho: ' + str(os.path.getsize(C.NOME))
print md.hexdigest()

con.close()
