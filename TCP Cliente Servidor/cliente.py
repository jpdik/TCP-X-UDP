#coding: utf-8

import socket
from sys import argv
from hashlib import md5
import time
import os
import sys

sys.path.insert(0, os.getcwd()[:os.getcwd().rfind('/')])

import constantes as C

arquivo = os.getcwd()[:os.getcwd().rfind('/')+1] + 'Arquivos/' + argv[1]

#Cria o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta o socket criado ao servidor
s.connect((C.IP, C.PORTA))

f = open(arquivo,'rb')

md = md5()

tempo = time.time()

while True:
	byts = f.read(2048)

	if not byts:
		break

	md.update(byts)

	s.send(byts)

f.close()

print 'tempo: ' + str(time.time()-tempo)
print 'tamanho: ' + str(os.path.getsize(arquivo))
print md.hexdigest()

s.close()