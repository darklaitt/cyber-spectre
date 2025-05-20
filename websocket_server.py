import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print("Получено:", message)
            await asyncio.gather(*[client.send(f"Аномалия: {message}") for client in clients])
    finally:
        clients.remove(websocket)

start_server = websockets.serve(handler, "localhost", 9002)
print("WebSocket сервер запущен на ws://localhost:9002")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
