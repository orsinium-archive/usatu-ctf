eng_words = open('english_words').read().upper().split('\n')
#eng_words = [i for i in eng_words if i.strip() and "'" not in i and (len(i)>1 or i.lower() in {'a', 'i'})]
eng_words.extend(['A', 'IS', 'ON', 'ARE', 'UFA', 'AS', 'I', 'OF'])

text = open('file').read().lower()


hypothesis = {
	'o': 'F',
	'e': 'L',
	'v': 'A',
	'z': 'G'
	}
for a, b in hypothesis.items():
	text = text.replace(a, b)


freq_alp = 'etaoinshrdlcumwfgypbvkxjqz'.upper()
from collections import Counter
for (a, _i), b in zip(Counter(text).most_common(2), freq_alp):
	text = text.replace(a, b)


print(text)


def test(template):
	for word in eng_words:
		if len(word) <= len(template):
			new_template = template
			#for t, w in zip(new_template, word):
			for i in range(len(word)):
				t = new_template[i]
				w = word[i]
				if t != w:
					if t.isupper():
						break
					else:
						new_template = new_template.replace(t, w)
			else:
				new_template = new_template[len(word):]
				if not new_template:
					#print('(',word,')')
					yield word
				else:
					for rez in test(new_template):
						if rez:
							yield word+rez

with open('rez', 'w') as out:
	flag = text[text.find('{')+1: text.find('}')]
	for rez in test(flag):
		print(rez)
		out.write(rez+'\n')
