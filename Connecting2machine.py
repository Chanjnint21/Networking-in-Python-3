import socket 

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    s.bind(('172.16.1.0', 10001))
    s.listen(5) # how many time you want to losten
    clientsocket, clientaddress = s.accept()
    print(clientsocket) # output: <socket.socket fd=2012, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.16.1.0', 10001), raddr=('172.16.1.0', 54679)>clientaddress('172.16.1.0', 54679)
    print('Got a connection from %s' % str(clientaddress)) # output: Got a connection from ('172.16.1.0', 54679)
    msg = input('Enter message: ') # input Enter message: Thank For connecting
    msg_encode = msg.encode('utf-8')
    clientsocket.send(msg_encode)
    clientsocket.recv(1024) #output: b'Thank For letting me know'
    message_back = clientsocket.recv(1024) 
    message_back_decode = message_back.decode('utf-8')
    print('client response: ' + message_back_decode) # output :client response: Thank For letting me know
 
def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 10001
    sock.connect(('172.16.1.0', port))
    msg = sock.recv(1024) # output = b'Thank For connecting'
    msg_decode = msg.decode('utf-8')
    print('message from server:' + msg_decode) # output: message from server:Thank For connecting
    msg_back = input( 'Message to server: ') # input Message to server: Thank For letting me know
    msg_back_encode = msg_back.encode('utf-8')
    sock.send(msg_back_encode)


