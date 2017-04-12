import socket
from hashlib import md5
import time
import os

NOME = 'arq.zip'

comecou = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('10.3.1.36',8888))

f = open(NOME, 'wb')


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
	print 'tamanho: ' + str(os.path.getsize(NOME))
	print md.hexdigest()

s.close()