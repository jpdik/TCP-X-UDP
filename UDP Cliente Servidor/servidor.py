import socket
from hashlib import md5
import time
import os
import sys

sys.path.insert(0, os.getcwd()[:os.getcwd().rfind('/')])

import constantes as C

comecou = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((C.IP, C.PORTA))

f = open(C.NOME, 'wb')


md = md5()

while True:
	dados,dados_cli = s.recvfrom(2048)
	if comecou == 0:
		tempo = time.time()
		comecou = 1

	if dados == 'fim':		
		break

		md.update(dados)

		f.write(dados)

	f.close()

	print 'tempo: ' + str(time.time()-tempo)
	print 'tamanho: ' + str(os.path.getsize(C.NOME))
	print md.hexdigest()

s.close()