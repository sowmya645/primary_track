from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ProductCreate(BaseModel):
    name: str
    description: str

class BlogCreate(BaseModel):
    title: str
    content: str

class CommentCreate(BaseModel):
    blog_id: int
    content: str
