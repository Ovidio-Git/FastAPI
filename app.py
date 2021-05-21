from fastapi import FastAPI
from database import database as MySQL
from database import Dogs
from schemas import UserRequestModel

app = FastAPI(title='Dogs', version='1.2')

#  DATABASE CONNECTION
@app.on_event('startup')   # if server is up connect to database
async def start():
    if MySQL.is_closed():
        MySQL.connect()

    # create tables for database
    MySQL.create_tables([Dogs])


@app.on_event('shutdown')  # if server is down disconnect to database
async def finish():
    if not MySQL.is_closed():
        MySQL.close()




@app.get("/api/dogs")
async def index():
    return "list"

@app.get("/api/dogs/{name}")
async def names(name: str):
    return "names"

@app.get("/api/dogs/is_adopted")
async def adopted():
    return "is_adopted"

@app.post("/api/dogs/{name}")
async def create_dog(dog_request: UserRequestModel):
    dog = Dogs.create(
        id =dog_request.id,
        name = dog_request.name,
        picture = dog_request.picture,
        is_adopted = dog_request.is_adopted
    )
    return "information saved"

