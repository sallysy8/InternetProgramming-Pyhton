import socket

client_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
client_socket.connect(('127.0.0.1', 50000))
client_socket.sendall(b'Hello?')
client_socket.recv(64)
client_socket.sendall(b'Excellent!')