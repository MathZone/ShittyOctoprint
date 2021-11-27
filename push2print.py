import asyncio
import sys
import serial
import websockets
from serial import Serial

#serialPort = str(sys.argv[1])
#serialPort = 'COM3'



def push2printer(file, serialP):
    ser = serial.Serial(serialP,115200,timeout=0)
    with open(file, "r") as f:
        for line in f:
            print(line)
            ser.write(str.encode(line+"\r\n"))
            if(ser.readline() == b'busy: processing\r\n'):
                while 1:
                    ser.inWaiting()
                    if(ser.readline() == b'ok\r\n'):
                        break                
        print(ser.readline())

