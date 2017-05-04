text = open('file').read()
flags = open('rez').read().split('\n')

voiced = set('eyuioa'.upper())
voiceless = set('qwrtpsdfghjklzxcvbnm'.upper())

real_words = {'IS', 'THE'}

def test(text):
#	for word in real_words:
#		if word not in text:
#			return False
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
				cnt = 0
		else:
			if c in voiceless:
				cnt += 1
				if cnt == 6:
					return False
			elif c in voiced:
				cnt = 1
				vcd = True
			else:
				cnt = 0
	return True

assert test('loremipsumdolorsitamet'), 'Bad test #1'
assert test('hellofrommoscowwithlove'), 'Bad test #2'

with open('rez2', 'w') as out:
	encripted_flag = text[text.find('{')+1: text.find('}')]
	for flag in flags:
		new_text = text
		for a,b in zip(encripted_flag, flag):
			new_text = new_text.replace(a, b)
		if test(new_text):
			print(flag)
			out.write(flag+'\n')
