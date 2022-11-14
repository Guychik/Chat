######################## Websocket server ########################
CLIENTS = set()

import websockets
import asyncio

async def send(websocket, message):
    try:
        await websocket.send(message)
    except websockets.ConnectionClosed:
        pass

def broadcast(message):
    for websocket in CLIENTS:
        asyncio.create_task(send(websocket, message))

async def handler(websocket):
    async for message in websocket:
        print(message)

async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()  # runs forever

if __name__ == "__main__":
    asyncio.run(main())