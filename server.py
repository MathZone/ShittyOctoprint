#server.py
#!/usr/bin/env python

import asyncio
import base64
import sys

import websockets

file = open(str(sys.argv[1]),"r")
#file = open("test","r");

async def echo(websocket):
    async for message in websocket:
        if(message == "READY!"):
            print("SENDING!")
            for x in file:
                await websocket.send(x)
            file.seek(0)
        elif (message=="CLOSE!"):
            exit()
            

async def main():
    async with websockets.serve(echo, '192.168.0.187', 8765):
        await asyncio.Future()

asyncio.run(main())
