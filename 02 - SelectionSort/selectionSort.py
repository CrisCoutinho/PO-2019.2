# -*- coding: utf-8 -*-
"""SelectionSort.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19nG93nZGPHI7PrHoifD_FfRDj2zJ1LDb
"""

import numpy as np
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def SelectionSort(elementList):
  swappedNumber = 0
  for i in range(len(elementList)): 
      
    minIndex = i 
    for j in range(i+1, len(elementList)): 
      swappedNumber = swappedNumber + 1
      if elementList[minIndex] > elementList[j]: 
        minIndex = j
            
    if minIndex != 1:
      elementList[i], elementList[minIndex] = elementList[minIndex], elementList[i]
  return swappedNumber


def listInv(tamanho):
  lista =[]
  for i in range(tamanho, 0, -1):
    lista.append(tamanho)
    tamanho = tamanho - 1
  return lista


def desenhaGrafico(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Aleatorio")
    ax.plot(x,yInv, label = "Pior Caso(Invertida)")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(YAxis)
    plt.show()

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista    

value10k = 10000
value20k = 20000
value50k = 50000
value100k = 100000

list10k = geraLista(value10k)
list20k = geraLista(value20k)
list50k = geraLista(value50k)
list100k = geraLista(value100k)

listWorseCase10k = listInv(value10k)
listWorseCase20k = listInv(value20k)
listWorseCase50k = listInv(value50k)
listWorseCase100k = listInv(value100k)

listValue = [value10k,value20k,value50k,value100k]
listQuestion = [list10k,list20k,list50k,list100k]
listQuestionWorseCase = [listWorseCase10k, listWorseCase20k, listWorseCase50k, listWorseCase100k]
timeSort = []
timeSortWorseCase = []
listNumberSwap = []
listNumberSwapWorseCase = []

for i in range(4):
    timeSort.append(timeit.timeit("SelectionSort({})".format(listQuestion[i]),setup="from __main__ import geraLista,SelectionSort, listInv",number = 1))
    listNumberSwap.append(SelectionSort(listQuestion[i]))
    timeSortWorseCase.append(timeit.timeit("SelectionSort({})".format(listQuestionWorseCase[i]),setup="from __main__ import geraLista,SelectionSort, listInv",number = 1))
    listNumberSwapWorseCase.append(SelectionSort(listQuestionWorseCase[i]))

desenhaGrafico(listValue,timeSort,timeSortWorseCase, XAxis="Número de elementos", YAxis="Tempo de ordenação em Seg")
desenhaGrafico(listValue,listNumberSwap,listNumberSwapWorseCase,  XAxis="Número de elementos", YAxis="Numero de Trocas")