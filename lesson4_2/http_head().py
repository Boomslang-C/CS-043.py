import socket

def http_head(host, page):
        request = 'HEAD ' + str(page) + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'
        sock = socket.create_connection((host, 80))
        sock.sendall(request.encode())
        data = sock.recv(1000)
        sock.close()
        print(data.decode())

http_head('50.87.178.13', '/')