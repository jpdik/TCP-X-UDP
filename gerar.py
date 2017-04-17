import os
from sys import argv

f = open('teste.txt','wb')

i = 0

while i < int(argv[1]):
	f.write('a'*1024*1024*1024)
	i+=1

f.close()

print os.path.getsize('teste.txt')