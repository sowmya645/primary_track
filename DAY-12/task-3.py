from fastapi import FastAPI
app = FastAPI()
from fastapi import FastAPI
app = FastAPI()
@app.get("/books")
def get_users():
    return ["dollarbhahu", "better than the movies"]
@app.get("/books/{book_id}")
def get_user(book_id: int):
    return {"user_id": book_id}