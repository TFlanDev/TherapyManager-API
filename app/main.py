from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name : str):
    return {"message" : f"Hello {name}"}

@app.post("/therapists/", response_model=schemas.TherapistCreate)
def create_therapist(therapist: schemas.TherapistCreate, db: Session = Depends(get_db)):
    # check if therapist already exists in db
    return crud.create_therapist(db=db, therapist=therapist)


@app.get("/therapist/{therapist_id}", response_model=schemas.TherapistGet)
def get_therapist(therapist_id : int, db : Session = Depends(get_db)):
    return crud.get_therapist(db, therapist_id=therapist_id)