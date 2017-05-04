from hashlib import sha224
def hash1(data):
	print(data)
	sh = sha224(data)
	return sh.hexdigest()

import sys, base64
if(len(sys.argv) > 1):
	a = [89, 108, 119, 103, 89, 50, 115, 108, 98, 108, 56, 115, 87, 50, 85, 
		108, 88, 85, 56, 50, 96, 87, 81, 110, 87, 49, 119, 117, 99, 108, 85, 56]
	
	x = sys.argv[1]
	uhash = hash1(bytes(x, encoding='utf-8'))
	
	from math import e, log
	xx = []
	for i in a:
		b = i+int(log(634*100023-532*100025-5100641*2+e))
		xx.append(chr(b))
	xx = bytes(''.join(xx), encoding='utf-8')
	ghash = hash1(base64.decodestring(xx))
	
	if(uhash == ghash):
		print('Lol, u r a genoius! ')
		print('You already know the flag, yep?')
	else:
		print("What is this? U r the hacker?????")
else:
		print("I want see your password, man")
