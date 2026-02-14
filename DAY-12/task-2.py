from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to REST API"}

@app.get("/books")
def get_users():
    return ["dollarbhahu", "better than the movies"]