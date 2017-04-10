# coding: utf-8
import os.path as os
import sys

''' exercicioTCP.py '''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect(("10.3.1.36",8888))
except:
	print "Não foi possível connectar ao servidor."
	exit()
while True:
	arquivo = raw_input('Insira o nome do arquivo: ')
	if arquivo == 'exit':
		s.send('')
		sys.exit(0)
	if os.isfile(arquivo):
		break
	print 'Arquivo insexistente'

s.send(arquivo.strip())

s.recv(1024)

f = open(arquivo,"rb")

dados = f.read(1024)
while dados:
	
	s.send(dados)	

	dados = f.read(1024)

f.close()
s.close()