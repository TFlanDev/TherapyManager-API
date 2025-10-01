from sqlalchemy.orm import Session
from . import database, models, schemas

def get_therapist(db : Session, therapist_id : int):
    return db.query(models.Therapist).filter(models.Therapist.id == therapist_id).first()

def create_therapist(db : Session, therapist: schemas.TherapistCreate):
    new_therapist = models.Therapist(name=therapist.name)
    db.add(new_therapist)
    db.commit()
    db.refresh(new_therapist)
    return new_therapist