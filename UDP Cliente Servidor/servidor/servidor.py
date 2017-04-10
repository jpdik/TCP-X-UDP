import socket
from hashlib import md5

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('10.3.1.36',8888))

while True:

	md = md5()

	while True:
		dados,dados_cli = s.recvfrom(2048)
		f = open('arq.jpg', 'wb')

		if dados == 'fim':		
			break

		md.update(dados)

		f.write(dados)
		f.close()

	print md.hexdigest()

s.close()