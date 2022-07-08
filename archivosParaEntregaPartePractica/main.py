#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :             Ruben Juarez Cadiz 

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
import csv
import copy

from EstadoHospitalario import EstadoHospitalario
from persona import Persona


def get_data_from_rastreador(name_file):
    """Function to obtain data from each rastreador.

    This function obtains data from each rastreador in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_rastreador(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      Null .

    Example
    -------
      >>> get_data_from_rastreador("file.csv")
    """
    return -1


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

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
    try:
      print("Rastreador 1. \n")
      # Devuelve las personas que tiene registradas el rastreador 1
      PersonasRastreador = get_data_from_rastreador("rastreador1.csv")
      for i in range(0,len(PersonasRastreador)):
          print(PersonasRastreador[i])
    except:
      print("KO info del rastreador.")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
