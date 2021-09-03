# print('ex_12-11-01.py is this')
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    url = input('Enter - ')
    try:
        mysock.connect(('data.pr4e.org', 80))
        break
    except:
        print('enter a valid url ')

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
