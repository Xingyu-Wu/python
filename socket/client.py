import socket
ip_port = ('127.0.0.1', 9999)
client=socket.socket()
client.connect(ip_port)
while True:
    date = client.recv(1024)
    print(date.decode('utf-8'))
    inp = input('client:')
    client.send(inp.encode())
    if inp =='exit':
        break
