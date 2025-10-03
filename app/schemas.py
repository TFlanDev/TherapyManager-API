from pydantic import BaseModel
from typing import List, Optional

class PatientBase(BaseModel):
    name : str

"""
create new patient
optionally assign new patient to a therapist
"""
class PatientCreate(PatientBase):
    therapist_id : Optional[int] = None

"""
Assign existing patient to a therapist
"""
class PatientUpdate(PatientBase):
    therapist_id : int

class PatientGet(PatientBase):
    id: int
    therapist_id : Optional[int] = None

    class Config:
        from_attributes = True


class TherapistBase(BaseModel):
    name : str

class TherapistCreate(TherapistBase):
    pass

class TherapistGet(TherapistBase):
    id : int
    patients : List[PatientGet]
    class Config:
        from_attributes = True

class TherapistGetSimple(TherapistBase):
    id : int
    class Config:
        from_attributes = True





    
