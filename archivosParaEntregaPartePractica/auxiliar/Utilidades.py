import random

#!/usr/bin/env python

"""Utilidades.py: Implementation of different util and commonly used algorithms in Python"""

__author__      = "Alberto Gil de la Fuente"
__copyright__   = "GPL License version 3"

def generaListDeIntsAleatorio(listSize, min, max):
  """ Return a list of random Int between min and max with length listSize
  """
  mylist = []
  for i in range(0, listSize):
    x = random.randint(min,max)
    mylist.append(x)
  return mylist

def generaIntAleatorio(min,max):
  return random.randint(min,max)

def imprime(intList):
  """
    imprime la lista de enteros pasada con 10 numeros en cada linea
  """
  subList = []
  slice=10
  listSize=len(intList)
  #print(listSize, intList)
  for i in range(0,listSize-slice,slice):
    subList=intList[i:i+slice]
    print(subList)
  subList=intList[(listSize-slice)+(listSize%slice):]
  print(subList)

def main():
  # Aqui se generarian los tests!! Habria que hacer tests para diferentes tipos y valores (negativos, 0) a generaListDeIntsAleatorio
  myList=generaListDeIntsAleatorio(100,1,10)
  imprime(myList)
  myRandomNumber=generaIntAleatorio(1,10)
  print(myRandomNumber)

if __name__ == "__main__":
	# Para ejecutar los tests definidos en el main unicamente cuando se ejecute este fichero
  main()
