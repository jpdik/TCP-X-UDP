#coding: utf-8

import socket
from sys import argv
from hashlib import md5
import time
import os 

#Cria o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta o socket criado ao servidor
s.connect(('127.0.0.1', 7777))

f = open(argv[1],'rb')

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
print 'tamanho: ' + str(os.path.getsize(argv[1]))
print md.hexdigest()

s.close()