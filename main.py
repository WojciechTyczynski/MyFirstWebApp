from fastapi import FastAPI
from pydantic import BaseModel

class PatientData(BaseModel):
    name: str
    surename: str

class Patient(BaseModel):
    id: int
    patient: dict

app = FastAPI()
app.id = 0
app.counter = 0

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

@app.post("/patient",  response_model=Patient)
def recive_patient(rq: PatientData):
    app.id += 1
    return Patient(id = app.id, patient=rq)
