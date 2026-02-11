from fastapi import FastAPI
app = FastAPI()

@app.get("/books")
def get_users():
    return ["dollarbhahu", "better than the movies"]