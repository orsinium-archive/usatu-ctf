text = open('file').read()
cfrom = 'etaoinshrdlcumwfgypbvkxjqz'

from collections import Counter
cto = Counter(text.lower()).most_common()
cto = [i[0] for i in cto if i[0] in cfrom]
cto.extend(list(set(cfrom) - set(cto)))
cto = ''.join(cto).upper()

print(cfrom)
print(cto)

voiced = set('eyuioa')
voiceless = set(cfrom) - voiced

hypothesis = {
	'o': 'F',
	'e': 'L',
	'v': 'A',
	'z': 'G'
	}
real_words = {'IS', 'THE', 'FLAG'}

from random import randint
def mutation(table):
	for i, (a,b) in enumerate(table[:-1]):
		if randint(0, 8):
			table[i], table[i+1] = table[i+1], (a,b)
	return table


def test(text):
	for word in real_words:
		if word not in text:
			return False
		cnt = 0
		vcd = True
		for c in text:
			if vcd:
				if c in voiced:
					cnt += 1
					if cnt == 5:
						return False
				elif c in voiceless:
					cnt = 1
					vcd = False
			else:
				if c in voiceless:
					cnt += 1
					if cnt == 6:
						return False
				elif c in voiced:
					cnt = 1
					vcd = True
		return True

assert not test('loremipsumdolorsitamet'), 'Bad test #1'
assert not test('hellofrommoscowwithlove'), 'Bad test #2'

table = list(zip(cfrom, cto))
from time import time
t = time()
cnt = 0
while 1:
	if cnt % 10000 == 0:
		print(int(time() - t), str(cnt)[::-1].replace('000', 'k')[::-1])
	cnt += 1
	new_table = mutation(table)
	new_text = text
	for cf, ct in new_table:
		new_text = new_text.replace(cf, ct)
	if test(new_text):
		print(new_text)
