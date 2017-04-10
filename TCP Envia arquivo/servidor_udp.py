#coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('localhost', 8888))

dados, dados_cli = (s.recvfrom(1024))

print 'Recebebido: ', dados, dados_cli

s.sendto(dados.upper(), dados_cli)

s.close()