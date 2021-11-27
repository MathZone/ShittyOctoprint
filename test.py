import asyncio
import sys
import serial
import websockets
from serial import Serial

serialPort = str(sys.argv[1])
#serialPort = 'COM3'

ser = serial.Serial(serialPort,115200)

output = open("./out.gcode","x")
output.close()
output = open("out.gcode","a")

async def main():
    async with websockets.connect("ws://192.168.0.187:8765") as websocket:
        await websocket.send("READY!")
        while 1:
            text = await websocket.recv()
            if text == "closeWS":
                ser.close()
                print("DONE")
                break
            print(text)
            output.write(text)
            ser.write(str.encode(text+"\r\n"))
            #print(ser.readline())
            
asyncio.run(main())