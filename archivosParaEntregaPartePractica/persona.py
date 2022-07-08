#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  persona.py
@author :  Ruben Juarez Cadiz 

@version :  0.0.1, 26 December 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""

from archivosParaEntregaPartePractica.SerVivo import SerVivo
from auxiliar import Utilidades
class Persona(SerVivo):
    # Variables globales

    # Constructor
    def __init__(self, persona_dni, nombre, hospital_input, edad):
        if(type(persona_dni)!= str):
            raise TypeError("")
        self.__dni = persona_dni
        self.__nombre = nombre
        self.__estadohospitalario = hospital_input
        self.__maxedad = 100
        self.__edad = edad
        self.__dosis = Utilidades.generaIntAleatorio(0,3)
        self.__dosismaximas = 3
        self.__cargaviral = 100-edad
        self.__listado_dni = dict()
        for clave in self.__listado_dni.keys():
            if isinstance( clave, persona_dni):
                raise ValueError("no se puede añadir la clave de un valor que ya esta en la lista")
            else:
                self.__listado_dni.update({self.__dni,self.__nombre})









        """Constructor of the class.
        This special method is executed when an object of this class is
        created.

        Syntax
        ------
            [ ] = __init__(self, persona_dni, nombre, hospital_input, edad)

        Parameters
        ----------
            [in] self Python object that represents an instance of the
                    class Persona.
            [in] persona_dni DNI de la persona.
            [in] nombre nombre de la persona.
            [in] hospital_input Estado hospitalario de la persona.
            [in] edad edad de la persona.

        Returns
        -------
            obj Python object output parameter that represents an instance
                of the class Persona.

        Exceptions
        ----------
            TypeError:
            If the parameter persona_dni is NOT a String.
            If the parameter nombre is NOT a String.
            If the parameter hospital_input is NOT a enum EstadoHospitalario.
            If the parameter edad is NOT be an int.

            ValueError:
            If the parameter dni no tiene 9 dígitos.
            If the parameter dni  ya está en la lista.

        Example
        -------
            >>> from SerVivo import SerVivo
            >>> from EstadoHospitalario import EstadoHospitalario
            >>> from Covid import Covid
            >>> from persona import Persona
            >>> persona1 = Persona("12345678E","Francisco Hernando",EstadoHospitalario.PLANTA, 31)
        """

    def get_cargaviral(self):
        return self.__cargaviral
        """Method to get the attribute cargaViral of the object.

        Syntax
        ------
          [ ] = obj_Persona.get_CargaViral( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.get_CargaViral( )
        """
    
    def get_dni(self):
        return self.__dni
        """Method to get the attribute dni of the object.

        Syntax
        ------
          [ ] = obj_Persona.get_dni( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.get_dni( )
        """
    @staticmethod
    def get_maxedad():
        return 30
        """Method to get the attribute edad máxima of the object.

        Syntax
        ------
          [ ] = obj_Persona.get_max_edad( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.get_CargaViral( )
        """

    def get_listsdni(self):
        return self.__listado_dni.keys()
        """Method to get la lista de dnis of the object.

        Syntax
        ------
          [ ] = obj_Persona.get_list_dnis( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.get_list_dnis( )
        """

    def get_dosis(self):
        return self.__dosis
        """Method to get número máximo de dosis of the object.

        Syntax
        ------
          [ ] = obj_Persona.get_max_dosis( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.get_max_dosis( )
        """

    def set_CargaViral(self,x):
        if(type(x)!= int):
            raise TypeError("")
        elif(x<0 or x>100):
            raise ValueError("")
        self.__cargaviral = x
        """Method to set the attribute cargaviral of the object.

        Method to set the attribute attack_rating based on a human-readable
        format of the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Persona.set_CargaViral( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.
          [in] attack_rating_to_be_set String that contains the attack rating
                                       to assign to the Persona.

        Returns
        -------

        Exceptions
        ----------
          TypeError If the parameter attack_rating_to_be_set is NOT a int.
          ValueError If the parameter attack_rating_to_be_set is NOT > 0 and <= 10.

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.set_CargaViral(8)
        """


    def eliminarUsuario(self):
        if(type(self.get_dni)!=str):
            raise TypeError("")
        self.__listado_dni.pop(self.get_dni())
        """Esta función elimina de la lista  el dni de la persona eliminada.

        Syntax
        ------
          [ ] = eliminarUsuario(self)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.eliminarUsuario( )
        """

    def __str__(self):
        """Method to present a human-readable format of the object.

        Method to present a human-readable format of the object that is formed
        in this class. This method is useful for logging or displaying some
        information about the object.

        Syntax
        ------
          [ ] = __str__( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Returns
        -------
          String Human-readable format of the object.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.__str__( )
        """


    def dosis_vacuna(self):
        if(self.is_vivo == False):
            pass
        else:
            azar = Utilidades.generaIntAleatorio(0,1)
            if(azar == 0):
                return 0
            else:
                return 1
        """Esta función añade una carda de vacuna a una persona si no
         supera el máximo de vacunas.
        Returns
        -------
        Devuelve 1 si se ha vacunado correctamente.
        Devuelve -1 si no ha sido posible vacunarse.

        Syntax
        ------
          [ ] = dosis_vacuna(self)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.dosis_vacuna( )
        """


    def infectado(self, Covid):
        if(self.is_vivo == False):
            pass
        if(self.__cargaviral<0):
            self.die()
            return -1
        else:
            return self.__cargaviral
        """Esta función gestiona la carga viral de una persona que ha sido
        infectada por la c lase Covid.
        Returns
        -------
        Devuelve la carga viral de la persona.
        Devuelve -1 si el usuario fallece y lo elimina de la lista.

        Syntax
        ------
          [ ] = infectado(self, Covid)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Persona.

        Exceptions
        ----------

        Example
        -------
          >>> from Persona import Persona
          >>> obj_Persona = Persona()
          >>> obj_Persona.infectado(Covid)
        """


def main():
    """TESTS!
    """
    nota = 0
    print("=======================================================.")
    print(">Test Case 1: Constructor.")
    print("=======================================================.")
    try:
        persona1 = Persona("12345678E","Francisco Hernando",EstadoHospitalario.PLANTA, 31)
        print("OK: Test PASS. Constructor.")
    except:
        print("KO: Constructor erróneo.")

    try:
        persona2 = Persona("12345678E","Francisco Hernando",EstadoHospitalario.PLANTA, 31)
        print("KO: Constructor erróneo en DNI, no puedes tener dos iguales.")
    except ValueError:
        print("OK: Test PASS. lista de dnis diferentes.")
    except:
        print("KO: Constructor erróneo en DNI, no puedes tener dos iguales.")
    try:
        persona3 = Persona("23","Elena Pérez",EstadoHospitalario.UCI, 31)
        print("KO: Test error, revise la condición del número de caracteres del DNI.")
    except ValueError:
        print("OK: Test PASS. Test DNI pasa correctamente.")
    except:
        print("KO: Test error, revise la condición del número de caracteres del DNI.")
        
    try:
        persona4 = Persona("12335678E","Elena Pérez","ugfhci", 31)
        print("KO: Test error, revise la condición del estado EstadoHospitalario.")
    except TypeError:
        print("OK: Test PASS. Test EstadoHospitalario pasa correctamente.")
    except:
        print("KO: Test error, revise la condición del estado EstadoHospitalario.")
    try:
        persona5 = Persona("12325678E","Elena Pérez",EstadoHospitalario.UCI, 222)
        print("KO: Test error, revise la condición del estado edad.")
    except ValueError:
        print("OK: Test PASS. Test edad pasa correctamente.")
    except:
        print("KO: Test error, revise la condición del estado edad.")
    try:
        persona5 = Persona("12325678E","Elena Pérez",EstadoHospitalario.UCI, 31)
        if (persona5.is_vivo() == True):
            print("OK: Test PASS. Herencia.")
        else:
            print("KO: Herencia.")
    except ValueError:
        print("OK: Test PASS. Test edad pasa correctamente.")
    except:
        print("KO: Herencia.")

    print("=======================================================.")
    print(">Test Case 2: gets.")
    print("=======================================================.")

    try:
        if (Persona.get_max_edad() == 100):
            print("OK: Test PASS. get_max_edad.")
        else:
            print("KO: get_max_edad.")
        if (Persona.get_list_dnis() == ['12345678E', '12325678E']):
            print("OK: Test PASS. get_list_dnis.")
        else:
            print("KO: get_list_dnis.")
        if (Persona.get_max_dosis() == 3):
            print("OK: Test PASS. get_max_dosis.")
        else:
            print("KO: get_max_dosis.")

        if (persona1.get_dni() == "12345678E"):
            print("OK: Test PASS. get_max_dosis.")
        else:
            print("KO: get_dni.")
        if (persona1.get_CargaViral() == 69):
            print("OK: Test PASS. get_CargaViral.")
        else:
            print("KO: get_CargaViral.")
        persona1.set_CargaViral(120)
        if (persona1.get_CargaViral() == 120):
            print("OK: Test PASS. set_CargaViral.")
        else:
            print("KO: set_CargaViral.")
    except:
        print("KO: sets.")    
    print("=======================================================.")
    print(">Test Case 3: Delete.")
    print("=======================================================.")
    try:
        persona6 = Persona("22325678E","Francisco Hernando",EstadoHospitalario.PLANTA, 31)
    except:
        print("KO: Constructor erróneo.")
    try:
        persona6.eliminarUsuario()
        if persona6.get_dni() in Persona.get_list_dnis():
            print("KO: Delete.")
        else:
            print("OK: Test PASS. Delete.")
    except:
        print("KO: Delete.")    
    print("=======================================================.")
    print(">Test Case 4: Str.")
    print("=======================================================.")
    try:
        persona7 = Persona("72345678E","Pablo Herrero",EstadoHospitalario.PLANTA, 25)
    except:
        print("KO: Constructor erróneo.")

    try:
        AuxString = persona7.__str__( )
        print(AuxString)
        if AuxString == "DNI: 72345678E\nNombre: Pablo Herrero\nEdad: 25\nEstado: PLANTA\nCarga Viral: 75\nDosis: 0":
            print("OK: Test PASS. Str.")
        else:
            print("KO: Str.")
    except:
        print("KO: Str.")

    print("=======================================================.")
    print(">Test Case 5: vacunado.")
    print("=======================================================.")
    try:
        try:
            persona8 = Persona("82325678E","Pepe Hernando",EstadoHospitalario.UCI, 55)
        except:
            print("KO: Constructor erróneo.")

        aux1 = persona8.get_CargaViral()
        persona8.dosis_vacuna() # 1
        if (aux1 == (persona8.get_CargaViral()-25)):
            print("OK: Test PASS. dosis vacuna.")
        else:
            print("KO: dosis vacuna.")
        persona8.dosis_vacuna() # 2
        aux2 = persona8.dosis_vacuna() # 3
        aux3 = persona8.dosis_vacuna() # 4
        if (aux3 ==-1 and aux2 != -1):
            print("OK: Test PASS. máximo número de dosis")
        else:
            print("KO: máximo número de dosis")
    except:
        print("KO: función vacunado")


    print("=======================================================.")
    print(">Test Case 6: infectado.")
    print("=======================================================.")
    try:
        persona9 = Persona("92325678E","Pepe Hernando",EstadoHospitalario.UCI, 55)
    except:
        print("KO: Constructor erróneo.")
    try:
        aux = 0
        while (aux !=-1):
            aux = persona9.infectado(Covid("covid-19"))
        if (persona9.is_vivo() != True):
            if (persona9.get_dni() not in Persona.get_list_dnis()):
                print("OK: Test PASS. infectado.")
            else:
                print("KO: infectado.")
        else:
            print("KO: infectado.")
    except:
        print("KO: Infectado.")


        

if __name__=="__main__":
    main()

