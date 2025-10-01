from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.post("/create/therapist/", response_model=schemas.TherapistCreate)
def create_therapist(therapist: schemas.TherapistCreate, db: Session = Depends(get_db)):
    return crud.create_therapist(db=db, therapist=therapist)

@app.get("/therapist/{therapist_id}", response_model=schemas.TherapistGet)
def get_therapist(therapist_id : int, db : Session = Depends(get_db)):
    return crud.get_therapist(db, therapist_id=therapist_id)

@app.get("/therapists/", response_model=List[schemas.TherapistGet])
def get_all_therapists(db : Session = Depends(get_db)):
    return crud.get_all_therapists(db)


@app.post("/create/patient/", response_model=schemas.PatientCreate)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

@app.get("/patient/{patient_id}", response_model=schemas.PatientGet)
def get_patient(patient_id : int, db : Session = Depends(get_db)):
    return crud.get_patient(db, patient_id=patient_id)