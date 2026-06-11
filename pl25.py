import serial as ak
import time

arduinoSerial = ak.Serial(port='COM6' , baudrate=9600 , timeout=0.1)
def write_read(num):
    arduinoSerial.write(bytes(num,'utf-8'))
    time.sleep(0.01)
    serialData = arduinoSerial.readline()
    return serialData

while True:
    num = input("Enter input : ")
    value = write_read(num)
    print(value)