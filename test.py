import asyncio
import sys
from asyncio.tasks import sleep
import serial
import websockets
from serial import Serial
from push2print import push2printer
import os


serialPort = str(sys.argv[1])
#serialPort = 'COM3'

#ser = serial.Serial(serialPort,115200,timeout=0)
#output = open("./out.gcode","x")
#output.close()
output = open("out.gcode","w")



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



            
asyncio.run(main())

