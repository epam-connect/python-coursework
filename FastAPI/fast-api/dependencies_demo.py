from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class MyPayload(BaseModel):
    x: int
    y: int

class DBConnection:...

class DBSession:...

# take token from header -> decode this toke -> get corresponding user -> validate if the use has permissions

async def get_db_connection():
    return DBConnection()

async def get_session(connection=Depends(get_db_connection)):   # nesting dependencies
    print(connection)
    return DBSession()

@app.get("/")
async def handler(arg=Depends(get_session)):            # injecting dependencies
    print(arg)
    return  {"x" : 1, "y": 2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("dependencies_demo:app", reload=True)