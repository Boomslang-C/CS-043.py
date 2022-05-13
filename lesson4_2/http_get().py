import socket

def http_get(host, page):
        request = 'GET ' + str(page) + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'
        sock = socket.create_connection((host, 80))
        sock.sendall(request.encode())
        data = sock.recv(1000)
        sock.close()
        print(data.decode())

http_get('indstudy1.org', '/CScourses/03b1_minimal.html')