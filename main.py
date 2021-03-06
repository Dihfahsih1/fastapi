from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel   
from random import randrange 

app = FastAPI()

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

# the order of these routes matters e.g route single post can't come before route latest

#route for latest posts
@app.get("/posts/latest")
def get_latest_post():
  posts=my_posts[len(my_posts)-1]
  return{"details": posts}

#route for single post
@app.get("/posts/{id}")
def get_post(id: int):
  post = find_post(id)
  return{"post_details":post}
  
