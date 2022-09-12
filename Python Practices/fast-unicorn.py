from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def root():
    return {"message": "Hello, Python World!"}
    

@app.get("/name")
def hello(name: str):
  return {"message": "Hello " + name + '!'} 