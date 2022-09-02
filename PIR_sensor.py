import RPi.GPIO as GPIO
import time
import datetime
import socket
from datetime import datetime
HOST = "172.16.0.188"
PORT = 10001
max_size = 1024
FORMAT = "utf-8"
print("Starting the client at: ", datetime.now())
Rpi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Rpi.connect((HOST, PORT))
file1 = open("/home/pi/Documents/auto_light.txt", "a")
def PIR():
    file = open("auto_light.txt", 'w')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN) #PIRSensor Pin
    GPIO.setup(3, GPIO.OUT) #LED Pin
    for j in range (50):
        i = GPIO.input(11)
        if i ==0:
            print("No motion")
            GPIO.output(3,0)
            time.sleep(0.1)
        elif i==1:
            Time = datetime.datetime.today()
            detected = " Motion Detected \n" + str(Time)
            #current_motion = Time.strftime("%H:%M:%S")
            print("Motion at", Time)
            file.write(str(detected))
            GPIO.output(3,1)
            time.sleep(0.1)
    file.close()
PIR()
file1.close()

f = open("/home/pi/Documents/auto_light.txt", "r")
data = f.read()
Rpi.send("auto_light.txt".encode(FORMAT))
msg = Rpi.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
Rpi.send(data.encode(FORMAT))
msg = Rpi.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
f.close()
Rpi.close()