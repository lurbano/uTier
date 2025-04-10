import asyncio
from aiohttp import web, ClientSession
from datetime import datetime
import json
#from getIP import getIP
from uAio import *

# database
from tierDB import *
db = tierDB()

dir_path = os.path.dirname(os.path.abspath(__file__))

async def handle(request):
    with open(dir_path+"/"+"index.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')

async def handlePost(request):
    data = await request.json()
    rData = {}
    print(data)
    # print(data["action"], data["value"])

    if data['action'] == "getTime":
        now = datetime.now()
        print(now.ctime())
        rData['item'] = "time"
        rData['status'] = now.ctime() # a string representing the current time

    if data['action'] == 'updateTier':
        # register device with the base station
        info = data['value']
        print("Updating: ", info)
        db.update(
            username=info['username'], 
            item=info['item'], 
            itemDescription=info['itemDescription'],
            tier=info['tier'] 
        )
        rData['item'] = 'updateTier'
        rData['status'] = 'updated'

async def main():
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post("/", handlePost)
    
    runner = web.AppRunner(app)
    await runner.setup()
    port = 14142

    host = getIP()
    site = web.TCPSite(runner, host, port)  # Bind to the local IP address
    await site.start()
    print(f"Server running at http://{host}:{port}/")

    # asyncio.create_task(print_hello())
    # asyncio.create_task(getLightLevel(dt=5))

    '''Testing post request'''
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")

    await asyncio.Event().wait()  # Keep the event loop running

if __name__ == '__main__':
    asyncio.run(main())