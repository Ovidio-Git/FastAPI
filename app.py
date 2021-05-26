from fastapi import FastAPI
from database import database as MySQL
from database import Dogs
from schemas import UserRequestModel
from schemas import UserResponseModel

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
    response = []
    for dog in Dogs.select():
        response.append( UserResponseModel(
        id = dog.id,
        name = dog.name,
        picture = dog.picture,
        is_adopted=dog.is_adopted,
        created_date=dog.created_date))
    return response

@app.get("/api/dogs/{name}")
async def get_names(name):
    response = []
    for dog in Dogs.select().where(Dogs.name == name):
        response.append( UserResponseModel(
        id = dog.id,
        name = dog.name,
        picture = dog.picture,
        is_adopted=dog.is_adopted,
        created_date=dog.created_date))
    return response


@app.get("/api/dogs/is_adopted")
async def dogs_adopted():
    response = []
    for dog in Dogs.select().where(Dogs.name == 1):
        response.append( UserResponseModel(
        id = dog.id,
        name = dog.name,
        picture = dog.picture,
        is_adopted=dog.is_adopted,
        created_date=dog.created_date))
    return response


@app.post("/api/dogs/{name}")
async def create_dog(dog_request: UserRequestModel):
    dog = Dogs.create(
        id =dog_request.id,
        name = dog_request.name,
        picture = dog_request.picture,
        is_adopted = dog_request.is_adopted
    )
    return "information saved"

