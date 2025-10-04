from typing import List, Optional, Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.post("/create/therapist/", response_model=schemas.TherapistCreate)
def create_therapist(therapist: schemas.TherapistCreate, db: Session = Depends(get_db)):
    return crud.create_therapist(db=db, therapist=therapist)

@app.get("/therapist/{therapist_id}/", response_model=Union[schemas.TherapistGet, schemas.TherapistGetSimple])
def get_therapist(therapist_id : int, include : Optional[str] = None, db : Session = Depends(get_db)):
    return crud.get_therapist(db=db, include=include, therapist_id=therapist_id)

@app.get("/therapists/", response_model=Union[List[schemas.TherapistGet], List[schemas.TherapistGetSimple]])
def get_all_therapists(include : Optional[str] = None, db : Session = Depends(get_db)):
    return crud.get_all_therapists(db=db, include=include)


@app.post("/create/patient/", response_model=schemas.PatientCreate)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

@app.get("/patient/{patient_id}/", response_model=schemas.PatientGet)
def get_patient(patient_id : int, db : Session = Depends(get_db)):
    return crud.get_patient(db=db, patient_id=patient_id)

@app.put("/assignpatient/{therapist_id}/{patient_id}", response_model=schemas.PatientUpdate)
def update_patient(patient_id : int, therapist_id : int, db : Session = Depends(get_db)):
    return crud.update_patient(db=db, patient_id=patient_id, therapist_id=therapist_id)