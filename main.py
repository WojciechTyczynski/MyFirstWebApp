from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.get("/method")
def get_something():
    return {"method": "GET"}

@app.post("/method")
def post_something():
    return {"method":"POST"}

@app.put("/method")
def put_something():
    return {"method":"PUT"}

@app.delete("/method")
def delete_something():
    return {"method":"DELETE"}
