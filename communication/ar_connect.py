import serial
ser=serial.Serial
port = "COM4"
boudrate = 9600

def read_temp():

    temp =

    return temp

while True:
if ser.readable():
    data=ser.read()