from fastapi import FastAPI
from database import database as MySQL

app = FastAPI(title='Dogs', version='1.1')

#  DATABASE CONNECTION
@app.on_event('startup')   # if server is up connect to database
async def start():
    if MySQL.is_closed():
        MySQL.connect()


@app.on_event('shutdown')  # if server is down disconnect to database
async def finish():
    if not MySQL.is_closed():
        MySQL.close()




@app.get("/api/dogs")
async def index():
    return "pegelo"

@app.get("/api/dogs/{name}")
async def names(name: str):
    return {"name": name}

@app.get("/api/dogs/is_adopted")
async def adopted():
    return {"Hello": "World"}

