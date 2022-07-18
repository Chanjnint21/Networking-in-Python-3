import socket
from datetime import datetime

PORT = 10002
HOST = '172.16.2.191'
max_size = 1024

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))

    print('Starting The server At: ', datetime.now())
    print("waiting FOr the Incoming connection From client....")

    sock.listen(5)
    client, addr = sock.accept()

    while True:
        data = client.recv(max_size)
        if data.decode('utf-8') == 'q' :
            break
        # if data.decode('utf-8') == 'cd' :
        #     os.chdir(data.decode(utf-8) [3:])  //change dir on server
        # if data.decode('utf-8') == 'start' :
        #     subprocess.Popen('notepad', shell=True)
        print('At', datetime.now(), addr, "said", data.decode('utf-8'))
        message_to_client = input("Enter the message To client: ")
        message_to_client_encode = message_to_client_encode.encode('utf-8')
        client.send(message_to_client_encode)
        if message_to_client == 'q' :
            break
    client.close()
    sock.close()

def client():
    print('Starting The server At: ', datetime.now())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    while True:
        message_to_server = input("Enter the message To Server: ")
        message_to_server_encode = message_to_server_encode.encode('utf-8')
        if message_to_server == 'q' :
            break
        data = s.recv(max_size)
        if data.decode('utf-8') == 'q':
            break
        print('At', datetime.now(),"server replied", data.decode('utf-8'))
    s.close()

