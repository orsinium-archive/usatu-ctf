import socket
connections = False

SERVER = ('127.0.0.1', 9090)
#welcome_msg = b'CONNECT 300\r\n\r\nДобро пожаловать.\r\n\r\nСервер работает на медленном dial-up соединении.\r\nПожалуйста, отнеситесь с пониманием и не пытайтесь подобрать пароль.\r\nf\x08 \x08l\x08 \x08a\x08 \x08g\x08 \x08{\x08 \x08S\x08 \x08o\x08 \x08m\x08 \x08e\x08 \x08t\x08 \x08i\x08 \x08m\x08 \x08e\x08 \x08s\x08 \x08_\x08 \x08w\x08 \x08h\x08 \x08a\x08 \x08t\x08 \x08_\x08 \x08y\x08 \x08o\x08 \x08u\x08 \x08_\x08 \x08s\x08 \x08e\x08 \x08e\x08 \x08_\x08 \x08i\x08 \x08s\x08 \x08_\x08 \x08N\x08 \x08O\x08 \x08T\x08 \x08_\x08 \x08w\x08 \x08h\x08 \x08a\x08 \x08t\x08 \x08_\x08 \x08y\x08 \x08o\x08 \x08u\x08 \x08_\x08 \x08g\x08 \x08e\x08 \x08t\x08 \x08}\x08 \x08\r\nPassword: '
flag = b'f\x08 \x08l\x08 \x08a\x08 \x08g\x08 \x08{\x08 \x085\x08 \x080\x08 \x08m\x08 \x08e\x08 \x087\x08 \x081\x08 \x08m\x08 \x08e\x08 \x08s\x08 \x08_\x08 \x08w\x08 \x08h\x08 \x08a\x08 \x08t\x08 \x08_\x08 \x08u\x08 \x08_\x08 \x08s\x08 \x08e\x08 \x08e\x08 \x08_\x08 \x08i\x08 \x08s\x08 \x08_\x08 \x08n\x08 \x08o\x08 \x08t\x08 \x08_\x08 \x08w\x08 \x08h\x08 \x08a\x08 \x08t\x08 \x08_\x08 \x08u\x08 \x08_\x08 \x08g\x08 \x083\x08 \x087\x08 \x08}\x08 \x08'
welcome_msg = b'Welcome to supermegasecure server.\r\n\r\nThe server is connected via slow dial-up connection.\r\nPlease be patient, and do not brute-force.\r\n'+flag+b'\r\nPassword: '

try:
	# sockets
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(SERVER)
	sock.listen(5)
	sock.setblocking(0)

	connections = []
	addresses = []

	print('Ready.')
	while True:
		# Подключение клиента
		try:
			conn, addr = sock.accept()
		except socket.error:
			pass
		else:
			addr = str(addr[0]) + ':' + str(addr[1])
			print('Get connection from ' + addr)
			conn.setblocking(0)
			connections.append(conn)
			addresses.append(addr)
			conn.send(welcome_msg)

		# Опрос клиентов
		for addr, conn in zip(addresses, connections):
			try:
				data = conn.recv(16384)
			except socket.error:
				pass
			else:
				# Клиент отключился
				if not data:
					print('Disconnect ' + addr)
					conn.close()
					del connections[connections.index(conn)]
				# Клиент прислал данные
				else:
					try:
						print('Get data: ' + str(data)[:70])
					except:
						print('Get bad data.')
					
					conn.send(b'Password incorrect!\r\nPassword: ')
except Exception as e:
	print(e)
finally:
	# Закрытие всех соединений любой ценой
	if connections:
		for conn in connections:
			conn.close()
