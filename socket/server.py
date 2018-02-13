import socket
def handle_request():
    ip_port = ('127.0.0.1', 9999)
    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(5)
    while True:
         conn,address = sk.accept()
         conn.send('你好'.encode())
         flag = True
         while flag:
             data = conn.recv(1024)
             print(data.decode())
             if data == 'exit':
                 flag = False
             conn.send('sb'.encode())
         conn.close()


def main():
    handle_request()

if __name__ == '__main__':
    main()
