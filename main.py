from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel   
from random import randrange 

app = FastAPI()
#using schema to declare which data to save
class Post(BaseModel):
  title:str
  content:str
  published: bool = True,
  rating: Optional[int]= None,
  
my_posts =[
           {"title":"Mysteries of Life", "content":"Things don't simply just happen","id":1},
           {"title":"Bondage", "content":"Lack of proper practice of spiritual warfare","id":2} 
           ]


def find_post(id):
  for p in my_posts:
    if p['id']== id:
      return p
    
@app.get("/posts")
def get_posts():
  return {'data' : my_posts}  

@app.post("/posts")
def create_posts(post:Post):
  post_dict = post.dict()
  post_dict['id']= randrange(0, 1000000)
  my_posts.append(post_dict)
  return {"data": my_posts}

@app.get("/posts{id}")
def get_post(id: int):
  post = find_post(id)
  return{"post_details":post}
  