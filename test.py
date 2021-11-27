import asyncio
import sys
import serial
import websockets
from serial import Serial
from push2print import push2printer
import os


serialPort = str(sys.argv[1])
#serialPort = 'COM3'

#ser = serial.Serial(serialPort,115200,timeout=0)
os.remove("out.gcode")
output = open("./out.gcode","x")
output.close()
output = open("out.gcode","a")

def push2printer(file, serialPort):
    ser = serial.Serial(serialPort,115200,timeout=0)
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
        
async def main():
    async with websockets.connect("ws://192.168.0.187:8765") as websocket:
        await websocket.send("READY!")
        while 1:
            text = await websocket.recv()
            if text == "closeWS":
                #ser.close()
                print("DONE")
                break
            print(text)
            output.write(text)
            #ser.write(str.encode(text+"\r\n"))
            #print(ser.readline())

    push2printer("./out.gcode",serialPort)

#def push2printer(file):
#    with open(file, "r") as f:
#        for line in f:
#            print(line)
#            ser.write(str.encode(line+"\r\n"))
#            if(ser.readline() == b'busy: processing\r\n'):
#                while 1:
 #                   ser.inWaiting()
 #                   if(ser.readline() == b'ok\r\n'):
  #                      break                
   #         print(ser.readline())

            
asyncio.run(main())

