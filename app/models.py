from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Therapist(Base):
    __tablename__ = 'therapists'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    patients = relationship('Patient', back_populates='therapist')
    
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    therapist_id = Column(Integer, ForeignKey('therapists.id'))
    therapist = relationship('Therapist', back_populates='patients')
