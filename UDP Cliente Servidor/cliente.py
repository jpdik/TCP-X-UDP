import socket
from sys import argv
from hashlib import md5
import time
import os
import sys

sys.path.insert(0, os.getcwd()[:os.getcwd().rfind('/')])

import constantes as C

arquivo = os.getcwd()[:os.getcwd().rfind('/')+1] + 'Arquivos/' + argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = open(arquivo,'rb')

md = md5()

tempo = time.time()

while True:
	byts = f.read(2048)

	if not byts:
		s.sendto('fim', (C.IP, C.PORTA))
		break

	md.update(byts)

	s.sendto(byts,(C.IP, C.PORTA))

f.close()

print 'tempo: ' + str(time.time()-tempo)
print 'tamanho: ' + str(os.path.getsize(arquivo))
print md.hexdigest()

s.close()