#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Covid, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  omicron.py
@author :  
           Ruben Juarez Cadiz 

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

class Omicron():
  """Python class to implement the basic version of Covid.

  This Python class implements the basic version of Covid.

  Syntax
  ------
    obj = Covid(covid_name)

  Parameters
  ----------
    [in] covid_name Name of the Covid.


  Returns
  -------
    obj Python object output parameter that represents an instance
        of the class Covid.

  Attributes
  ----------

  Example
  -------
    >>> from Covid import Covid
    >>> obj_Covid = Covid("covid-19")
  """
  def __init__(self, covid_name):
    """Python class to implement the basic version of Covid.

    This Python class implements the basic version of Covid.

    Syntax
    ------
        obj = Covid(covid_name)

    Parameters
    ----------
        [in] covid_name Name of the Covid.


    Returns
    -------
        obj Python object output parameter that represents an instance
            of the class Omicron.

    Attributes
    ----------

    Example
    -------
        >>> from Omicron import Omicron
        >>> obj_Omicron = Omicron("covid-19")
    """


  def get_max_impacto():
    print("")


def main():
  """Function main of the module.

  The function main of this module is used to test the Class that is described
  in this module.

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
  print(">Test Case 1: Create a Omicron.")
  print("=======================================================.")
  try:
    covid1 = Omicron("covid-19")
    covid2 = Omicron("covid-19")
    covid3 = Omicron("covid-19")
    covid4 = Omicron("covid-19")
    if(covid1._impacto >=0 and covid1._impacto<=10):
      if(covid2._impacto >=0 and covid2._impacto<=10):
        if(covid3._impacto >=0 and covid3._impacto<=10):
          if(covid4._impacto >=0 and covid4._impacto<=10):
            print("OK: Test PASS. número aleatorio.")
          else:
            print("KO: Test FAIL. número aleatorio entre intervalo.")
        else:
            print("KO: Test FAIL. número aleatorio entre intervalo.")
      else:
          print("KO: Test FAIL. número aleatorio entre intervalo.")
    else:
        print("KO: Test FAIL. número aleatorio entre intervalo.")
  except:
    print("KO: Fallo al crear la instancia Covid.")


  print("=======================================================.")
  print(">Test Case 2: Máximo Impacto cambiado.")
  print("=======================================================.")
  try:
    omi1 = Omicron("omicron")
    try:
      if (Omicron.get_max_impacto() == 10):
        print("OK: Test PASS. máximo impacto.")
      else:
        print("KO: Test FAIL. Máximo impacto.")
    except:
      print("Fallo al crear la función max impacto.")
  except:
    print("KO: máximo impacto cambiado.")

# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
