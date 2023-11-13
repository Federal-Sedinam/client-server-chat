import socket

ADDRESS = 'localhost'
PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ADDRESS, PORT))
print(sock.recv(1024).decode('utf-8'))

while True:
    message = input('Message: ')
    sock.send(message.encode('utf-8'))   
    if message == 'bye':
        break
    
    data = sock.recv(1024).decode('utf-8')
    print(data)
    if data == 'bye':
        print('Server says bye.')
        break

sock.close()
