


class personaNino(): 
    # Variables globales


    # Constructor
    def __init__(self, persona_dni, nombre, hospital_input, edad):
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
            >>> persona1 = personaNino("12345678E","Francisco Hernando",EstadoHospitalario.PLANTA, 3)
        """



    @staticmethod
    def get_max_edad():
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

    def get_max_dosis():

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

    def dosis_vacuna(self):
        """Esta función añade una carda de vacuna a una persona si no
         supera el máximo de vacunas.
        Returns
        -------
        Devuelve 1 si se ha vacunado correctamente.
        Devuelve -1 se no ha sido posible vacunarse.

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


def main():
    """TESTS!
    """

    print("=======================================================.")
    print(">Test Case 1: gets.")
    print("=======================================================.")
    try:
        if (personaNino.get_max_edad() == 12):
            print("OK: Test PASS. get_max_edad.")
        else:
            print("KO: get_max_edad.")
        if (personaNino.get_max_dosis() == 1):
            print("OK: Test PASS. get_max_dosis.")
        else:
            print("KO: get_max_dosis.")
    except:
        print("KO TEST 1.")
 
    print("=======================================================.")
    print(">Test Case 2: Control edad.")
    print("=======================================================.")
    try:
        try:
            persona8 = personaNino("82325678E","Pepe Hernando",EstadoHospitalario.UCI, 55)
        except ValueError:
            print("OK: Test PASS. Control edad.")
        except:
            print("KO: Control de edad.")
    except:
        print("KO TEST 2.")

    print("=======================================================.")
    print(">Test Case 3: vacunado.")
    print("=======================================================.")
    try:
        try:
            persona8 = personaNino("82325678E","Pepe Hernando",EstadoHospitalario.UCI, 5)
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
        if (aux3 ==-1 and aux2 ==-1 and aux1 != -1):
            print("OK: Test PASS. máximo número de dosis")
        else:
            print("KO: máximo número de dosis")
    except:
        print("KO TEST 3.")



        

if __name__=="__main__":
    main()

