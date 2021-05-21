from fastapi import FastAPI

app = FastAPI()



@app.get("/api/dogs")
async def index():
    return "pegelo"

@app.get("/api/dogs/{name}")
async def names(name: str):
    return {"name": name}

@app.get("/api/dogs/is_adopted")
async def adopted():
    return {"Hello": "World"}

