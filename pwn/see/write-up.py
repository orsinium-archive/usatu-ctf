import socket
SERVER = ('127.0.0.1', 9090)

sock = socket.socket()
sock.connect(SERVER)
sock.setblocking(0)

from time import sleep
sleep(1)

data = sock.recv(8192)
start = data.find(b'\x08')
end = data.rfind(b'\x08')
data = data[start-1:end]
data = data.replace(b'\x08', b'').replace(b' ', b'')
print(str(data)[2:-1])
