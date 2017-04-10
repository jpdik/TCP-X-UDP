#coding: utf-8

import socket
import time

#Cria o objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta o socket criado ao servidor
s.connect(('localhost', 8888))
while True:
	#Envia a mensagem pro Servidor
	s.send(raw_input())
	#Recebe a mensagem em uppercase retornada pelo servidor e imprime na tel
	print s.recv(1024)

s.close()