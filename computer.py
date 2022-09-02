# import mysql.connector
import socket
from datetime import datetime
HOST = socket.gethostbyname(socket.gethostname())
PORT = 10001
MaxSIZE = 1024
FORMAT = "utf-8"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5)
client, addr = sock.accept()
# Receive Data from RaspBerry Pi 
while True:

    filename = client.recv(MaxSIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")

    file = open("auto_light.txt", "w")
    client.send("Filename received.".encode(FORMAT))

    data = client.recv(MaxSIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    client.send("File data received".encode(FORMAT))

    file.close()

    client.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
    break

sock.close()

# Store sensor data and datetime in a persistent media (MySQL or local file) (6)

# dataBase = mysql.connector.connect(

#     host="localhost",

#     user="root",

#     passwd="",

#     database="Jnint"
# )


# cursorObject = dataBase.cursor()
# f = open("Light sensor.txt", "r")
# end_of_file = f.readline()
# for x in f:
#     res = x.split()
#     sql = "INSERT INTO tbl_STUDENT (NAME, EMAIL) VALUES (%s, %s)"
#     val = (str(res[0]), str(res[1]))
#     cursorObject.execute(sql, val)
#     dataBase.commit()
#     if not end_of_file:
#         break