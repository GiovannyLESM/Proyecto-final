from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base

class Estudiante(Base):
    __tablename__="estudiante"
    idEstudiante=Column(Integer,primary_key = True)
    apellidoPaterno = Column ( String )
    apellidoMaterno = Column ( String )
    nombres = Column ( String )
    elegible = Column ( Boolean )

    asignaturas = relationship ( 'Asignatura' , secondary = 'asignatura_estudiante' )
    equipos = relationship ( 'Equipo' , secondary = 'estudiante_equipo' )

class EstudianteEquipo(Base): #uno
    __tablename__ = 'estudiante_equipo'

    estudiante = Column(Integer, ForeignKey('estudiante.idEstudiante'), primary_key=True)
    equipo = Column ( Integer , ForeignKey ( 'equipo.idEquipo' ) , primary_key = True )