from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session

class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura):
        if(nombreAsignatura==""):
            return False

        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    def editar_asignatura ( self , idAsignatura , nombreAsignatura ) :
        busqueda = session.query ( Asignatura ).filter ( Asignatura.nombreAsignatura == nombreAsignatura ,
                                                         Asignatura.idAsignatura != idAsignatura ).all ( )
        if len ( busqueda ) == 0 :
            asignatura = session.query ( Asignatura ).filter ( Asignatura.idAsignatura == idAsignatura ).first ( )
            asignatura.nombreAsignatura = nombreAsignatura
            session.commit ( )
            return True
        else :
            return False

    def eliminar_asignatura ( self , idAsignatura ) :
        try :
            asignatura = session.query ( Asignatura ).filter ( Asignatura.idAsignatura == idAsignatura ).first ( )
            session.delete ( asignatura )
            session.commit ( )
            return True
        except :
            return False

    def dar_asignatura ( self ) :
        asignaturas = [ elem.__dict__ for elem in
                        session.query ( Asignatura ).all ( ) ]
        return asignaturas

    def dar_asignatura_por_idAsignatura ( self , idAsignatura ) :
        return session.query ( Asignatura ).get ( idAsignatura ).__dict__

    def buscar_asignatura_por_nombreAsignatura ( self , nombreAsignatura ) :
        asignaturas = [ elem.__dict__ for elem in
                        session.query ( Asignatura ).filter (
                            Asignatura.nombreAsignatura.ilike ( '%{0}%'.format ( nombreAsignatura ) ) ).all ( ) ]
        return asignaturas