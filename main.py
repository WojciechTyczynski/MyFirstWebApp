from fastapi import FastAPI, HTTPException, Response, Cookie
from pydantic import BaseModel
import base64
from fastapi.responses import RedirectResponse


class PatientData(BaseModel):
    name: str
    surename: str

class Patient(BaseModel):
    id: int
    patient: dict

app = FastAPI()
app.id = 0
app.counter = 0
app.patients = []
app.secret_key = 'DWl4oicHEm87PyEfadxBz3YO3dvk2SazdaGFcxi989qewvxcsdm41cdpqcjea'

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/welcome")
def root():
    return {"message": "Welcome!"}

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

@app.post("/login")
def login_cookie(user: str, password: str, response: Response):
    session_token = base64.b64encode(bytes(f"{user}:{password}", encoding='utf8'))
    response.set_cookie(key="session_token", value=session_token)
    return return {"message": "Welcome!"}

@app.post("/patient",  response_model=Patient)
def recive_patient(rq: PatientData):
    app.id += 1
    app.patients.append(Patient(id = app.id-1, patient=rq))
    return Patient(id = app.id-1, patient=rq)

@app.get("/patient/{pk}", response_model=PatientData)
def read_patient(pk: int):
    find = False
    for patient in app.patients:
        if patient.id == int(pk):
            find = True
            result = PatientData(name = patient.patient['name'], surename = patient.patient['surename'])
            return result
    if find == False:
        raise HTTPException(status_code=204)


@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)
