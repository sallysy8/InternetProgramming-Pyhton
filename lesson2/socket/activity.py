import socket

socket.getaddrinfo('info.cern.ch', 'http')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
client.connect(('188.184.64.53', 80))

msg = "GET / HTTP/1.1\r\n"
msg += "Host: info.cern.ch\r\n\r\n"
msg = msg.encode('utf8')
client.sendall(msg)
client.recv(1024)
client.close()

