import socket
from sys import argv
from hashlib import md5

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = open(argv[1],'rb')

md = md5()

while True:
	byts = f.read(2048)

	if not byts:
		s.sendto('fim',('10.3.1.36', 8888))
		break

	md.update(byts)

	s.sendto(byts,('10.3.1.36', 8888))

print md.hexdigest()

f.close()
s.close()