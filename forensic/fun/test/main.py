data = open('text').read().replace('\n', ' ')
data = data.split()

def dec(x, table):
	rez = 0
	for i, c in enumerate(x):
		rez += table.index(c)**(5-i)
	return rez

from itertools import permutations
i = 0
for table in permutations('.?!'):
	rez = b''
	for x in data:
		print(chr(dec(x, table)), end='')
		x = dec(x, table)
		rez += bytes(chr(x), encoding='utf-8')
	open(str(i), 'wb').write(rez)
	i += 1
	print('\n\n\n')
