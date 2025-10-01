from sqlalchemy.orm import Session
from . import database, models, schemas

def get_therapist(db : Session, therapist_id : int):
    return db.query(models.Therapist).filter(models.Therapist.id == therapist_id).first()

def get_all_therapists(db : Session):
    return db.query(models.Therapist).all()

def create_therapist(db : Session, therapist: schemas.TherapistCreate):
    new_therapist = models.Therapist(name=therapist.name)
    db.add(new_therapist)
    db.commit()
    db.refresh(new_therapist)
    return new_therapist


def create_patient(db : Session, patient: schemas.PatientCreate):
    new_patient = models.Patient(name=patient.name, therapist_id=patient.therapist_id)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_patient(db : Session, patient_id : int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()