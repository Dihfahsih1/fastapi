from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def get_posts():
  return {'data' : 'These are your posts'}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
  return {'message': 'posts created successfully'}