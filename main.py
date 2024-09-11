from fastapi import FastAPI
import random
app = FastAPI()

# 127.0.0.1:8001/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8001/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True "num_aleatorio": random.randint(1, 100)}