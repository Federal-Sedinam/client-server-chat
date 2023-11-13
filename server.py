import socket

ADDRESS = ''
PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ADDRESS, PORT))
sock.listen(3)
client, _ = sock.accept()

while True:   
    message = input('Message: ')
    client.send(message.encode('utf-8'))
    if message == 'bye':
        break
   
    data = client.recv(1024).decode('utf-8')
    print(data)
    if data == 'bye':
        print('Client says bye.')
        break

client.close()
