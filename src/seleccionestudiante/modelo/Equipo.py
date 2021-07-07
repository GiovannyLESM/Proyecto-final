from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Equipo(Base):
    __tablename__="equipo"
    idEquipo=Column(Integer,primary_key = True)
    denominacionEquipo = Column ( String )
	
    actividades = relationship('Actividad', cascade='all, delete, delete-orphan')
    estudiantes = relationship ( 'Estudiante' , secondary = 'estudiante_equipo' )