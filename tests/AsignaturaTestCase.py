import unittest
from datetime import datetime
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.logica.Sorteo import Sorteo
from src.seleccionestudiante.modelo.declarative_base import Session

class AsignaturaTestCase ( unittest.TestCase ) :
    def setUp ( self ) :
        # Crea una sorteo para hacer las pruebas
        self.sorteo = Sorteo ( )

        # Abre la sesión
        self.session = Session ( )

        # crear estudiantes
        self.estudiante1 = Estudiante ( apellidoPaterno = "Ramos" , apellidoMaterno = "Ortega" , nombres = "Juan Carlos" ,
                                   elegible = True )
        self.estudiante2 = Estudiante ( apellidoPaterno = "Solis" , apellidoMaterno = "Matos" , nombres = "Pedro" ,
                                   elegible = True )
        self.estudiante3 = Estudiante ( apellidoPaterno = "Paredes" , apellidoMaterno = "Torres" , nombres = "Luis Alberto" ,
                                   elegible = True )
        self.estudiante4 = Estudiante ( apellidoPaterno = "Garcia" , apellidoMaterno = "Mateo" , nombres = "Miguel Angel" ,
                                   elegible = True )

        self.session.add ( self.estudiante1 )
        self.session.add ( self.estudiante2 )
        self.session.add ( self.estudiante3 )
        self.session.add ( self.estudiante4 )
        self.session.commit ( )

        # crear asignatura
        self.asignatura1 = Asignatura ( nombreAsignatura = "Análisis y diseño de sistemas" )
        self.asignatura2 = Asignatura ( nombreAsignatura = "Pruebas de software" )
        self.session.add ( self.asignatura1 )
        self.session.add ( self.asignatura2 )
        self.session.commit ( )

        # crear equipo de trabajo
        self.equipo1 = Equipo ( denominacionEquipo = "Equipo01" )
        self.equipo2 = Equipo ( denominacionEquipo = "Equipo02" )
        self.session.add ( self.equipo1 )
        self.session.add ( self.equipo2 )
        self.session.commit ( )

        # crear actividad
        self.actividad1 = Actividad ( denominacionActividad = "Prueba unitaria" ,
                                 fecha = datetime ( 2021 , 9 , 28 , 00 , 00 , 00 , 00000 ) )
        self.actividad2 = Actividad ( denominacionActividad = "TDD" , fecha = datetime ( 2021 , 9 , 25 , 00 , 00 , 00 , 00000 ) )
        self.actividad3 = Actividad ( denominacionActividad = "BDD" , fecha = datetime ( 2021 , 9 , 25 , 00 , 00 , 00 , 00000 ) )
        self.session.add ( self.actividad1 )
        self.session.add ( self.actividad2 )
        self.session.add ( self.actividad3 )
        self.session.commit ( )

        # Relacionar Asignatura con estudiantes
        self.asignatura1.estudiantes = [ self.estudiante1 , self.estudiante4 ]
        self.asignatura2.estudiantes = [ self.estudiante2 , self.estudiante3 ]
        self.session.commit ( )

        # Relacionar equipo con estudiantes
        self.equipo1.estudiantes = [ self.estudiante1 , self.estudiante3 ]
        self.equipo2.estudiantes = [ self.estudiante2 , self.estudiante4 ]
        self.session.commit ( )

        # Relacionar Equipo de trabajo con actividad
        self.equipo1.actividades = [ self.actividad1 , self.actividad2 ]
        self.equipo2.actividades = [ self.actividad3 ]
        self.session.commit ( )

        self.session.close ( )

    def tearDown ( self ) :
        self.session = Session ( )

        estudiantes = self.session.query ( Estudiante ).all ( )
        for estudiante in estudiantes :
            self.session.delete ( estudiante )
        self.session.commit ( )
        self.session.close()

        asignaturas = self.session.query ( Asignatura ).all ( )
        for asignatura in asignaturas :
            self.session.delete ( asignatura )
        self.session.commit ( )
        self.session.close ( )

        actividades = self.session.query ( Actividad ).all ( )
        for actividad in actividades :
            self.session.delete ( actividad )
        self.session.commit ( )
        self.session.close ( )

        equipos = self.session.query ( Equipo ).all ( )
        for equipo in equipos :
            self.session.delete ( equipo )
        self.session.commit ( )
        self.session.close ( )

    def test_agregar_asignatura ( self ) :
        resultado = self.sorteo.agregar_asignatura ( nombreAsignatura = "Estructura de datos" )
        self.assertEqual ( resultado , True )

    def test_agregar_asignatura_repetido(self):
        resultado = self.sorteo.agregar_asignatura(nombreAsignatura = "Pruebas de software")
        self.assertNotEqual(resultado, True)