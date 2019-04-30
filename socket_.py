import socket

host = '10.108.167.229'
port = 15001
username = 'vm'
password = '123456'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	server_address = (host, port)
	sock.connect(server_address)
	sock.sendall("stop c:\\soft\\bin\\SCADAMake.exe")
finally:
	sock.close()