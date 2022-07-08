#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the Enum EstadoHospitalario, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  EstadoHospitalario.py
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


# Source packages.
from enum import Enum


class EstadoHospitalario(Enum):
    """Python class to implement an enumeration for the attribute EstadoHospitalario.

    This Python class implements an enumeration for the attribute EstadoHospitalario.

    Syntax
    ------
      obj = EstadoHospitalario.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class EstadoHospitalario.

    Attributes
    ----------

    Example
    -------
      >>> from EstadoHospitalario import EstadoHospitalario
      >>> obj_EstadoHospitalario = EstadoHospitalario
    """


    def __str__(self):
        return self.name

    @staticmethod
    def from_str(str_hospital_type):
        """Method to obtain a Enum from a String.

        This method is used to generate a Enum based on a String.

        Syntax
        ------
          [ ] = from_str(str_hospital_type)

        Parameters
        ----------
          str_hospital_type String String that represents a EstadoHospitalario Type.

        Returns
        -------
          Null .

        Example
        -------
          >>> EstadoHospitalario = obj.from_str("asintoMATIco")
          >>> EstadoHospitalario contiene EstadoHospitalario.ASINTOMATICO
        """
        str_hospital_type = str_hospital_type.lower()
        if str_hospital_type == 'asintomatico':
            return EstadoHospitalario.ASINTOMATICO
        elif str_hospital_type == 'casa':
            return EstadoHospitalario.CASA
        elif str_hospital_type == 'planta':
            return EstadoHospitalario.PLANTA
        elif str_hospital_type == 'uci':
            return EstadoHospitalario.UCI
        else:
            raise TypeError("The str " + str_hospital_type + " does not correspond with a Person Type")


def main():
    """Function main of the module.

    The function main of this module is used to test the Class EstadoHospitalario.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=======================================================.")
    print(">Test Case 1: Check Class EstadoHospitalario - Name.")
    print("=======================================================.")

    try:
      if isinstance(EstadoHospitalario.ASINTOMATICO, EstadoHospitalario):
          print("OK: Test PASS. The enum for ASINTOMATICO has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")

    try:
      if isinstance(EstadoHospitalario.CASA, EstadoHospitalario):
          print("OK: Test PASS. The enum for CASA has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")
    try:
      if isinstance(EstadoHospitalario.PLANTA, EstadoHospitalario):
          print("OK: Test PASS. The enum for PLANTA has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")
    try:
      if isinstance(EstadoHospitalario.UCI, EstadoHospitalario):
          print("OK: Test PASS. The enum for UCI has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")
      
    print("=======================================================.")
    print(">Test Case 2: Check Class EstadoHospitalario - Value.")
    print("=======================================================.")

    try:
      if EstadoHospitalario.ASINTOMATICO.value == 0:
          print("OK: Test PASS. The enum for ASINTOMATICO has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")

    try:
      if EstadoHospitalario.CASA.value == 1:
          print("OK: Test PASS. The enum for CASA has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")
 
    try:
      if EstadoHospitalario.PLANTA.value == 2:
          print("OK: Test PASS. The enum for PLANTA has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")
 
    try:
      if EstadoHospitalario.UCI.value == 4:
          print("OK: Test PASS. The enum for UCI has been correctly set.")
      else:
          print("KO: Test FAIL. Check the method __init__().")
    except:
      print("KO: Test FAIL. Check the method __init__().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
