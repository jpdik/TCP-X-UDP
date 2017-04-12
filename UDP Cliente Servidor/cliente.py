import socket
from sys import argv
from hashlib import md5
import time
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = open(argv[1],'rb')

md = md5()

tempo = time.time()

while True:
	byts = f.read(2048)

	if not byts:
		s.sendto('fim',('10.3.1.36', 8888))
		break

	md.update(byts)

	s.sendto(byts,('10.3.1.36', 8888))

f.close()

print 'tempo: ' + str(time.time()-tempo)
print 'tamanho: ' + str(os.path.getsize(argv[1]))
print md.hexdigest()

s.close()