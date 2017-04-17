#coding: utf-8

import socket
from hashlib import md5
import time
import os
import sys
import matplotlib.pyplot as plt

sys.path.insert(0, os.getcwd()[:os.getcwd().rfind('/')])

import constantes as C

comecou = 0

tempoLista = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((C.IP, C.PORTA))

f = open(C.NOME, 'wb')


md = md5()

while True:
	tempoL = time.time()
	dados,dados_cli = s.recvfrom(C.CARACTERES_PACOTE)
	tempoLista.append(time.time()-tempoL)
	if comecou == 0:
		tempo = time.time()
		comecou = 1

	if dados == 'fim':		
		break

	md.update(dados)

	f.write(dados)

	
f.close()

tempoLista = tempoLista[1:]
tempoMedio = sum(tempoLista)/float(len(tempoLista))

print 'tempo: ' + str(time.time()-tempo)
print 'tamanho: ' + str(os.path.getsize(C.NOME))
print 'tempo médio: ' + str(tempoMedio)
print md.hexdigest()

plt.plot(tempoLista)
plt.plot(range(len(tempoLista)), [tempoMedio for x in tempoLista], color='red')
plt.savefig(C.GERA_GRAFICO)
plt.show()

s.close()