from pynput.keyboard import Key, Controller
import serial
from time import sleep
ser = serial.Serial(port = "COM3", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


while True:
    data = ser.readline().decode('utf-8').rstrip()
    if len(data) > 0:
        print ('Got:', data)
    else:
        sleep(0.5)
        print ('not blocked')
    
ser.close()


