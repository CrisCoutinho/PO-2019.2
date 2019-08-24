# -*- coding: utf-8 -*-
"""shellSort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11bTldwNT-UZwRVJllL5xAmMshbCqmP9r
"""

import numpy as np
from random import shuffle, randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt





def shellSort(elementList): 
   
    numberElement = len(elementList) 
    gap =  numberElement//2
    while gap > 0: 
  
        for i in range(gap, numberElement): 
            
            temp = elementList[i]
            j = i 
            while  j >= gap and elementList[j-gap] >temp: 
                
                elementList[j] = elementList[j-gap] 
                j = j - gap
            
            elementList[j] = temp 
        
        gap //= 2

def listInv(tamanho):
  lista =[]
  for i in range(tamanho, 0, -1):
    lista.append(tamanho)
    tamanho = tamanho - 1
  return lista


def drawGraph(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y,color = 'blue', label = "Aleatorio")
    ax.plot(x,yInv, color = 'red', label = "Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(YAxis)
    plt.show()

def listInv(tamanho):
  newList =[]
  for i in range(tamanho, 0, -1):
    newList.append(tamanho)
    tamanho = tamanho - 1
  return newList


def generateList(tam):
  newList = list(range(1, tam + 1))
  shuffle(newList)
  return newList

#sys.setrecursionlimit(10**6)  

listValueGraph = [100 ,200 , 400, 500, 1000, 2000]
#~~~~~~~~~~ Tests ~~~~~~~~~~~#


value100k = 100000
value200k = 200000
value400k = 400000
value500k = 500000
value1M = 1000000
value2M = 2000000

#~~~~~~~~~~ List Inverted Case ~~~~~~~~~~~#

listInvertedCase100k = listInv(value100k)
listInvertedCase200k = listInv(value200k)
listInvertedCase400k = listInv(value400k)
listInvertedCase500k = listInv(value500k)
listInvertedCase1M = listInv(value1M)
listInvertedCase2M = listInv(value2M)


listQuestionInvertedCase = [listInvertedCase100k,listInvertedCase200k,
                            listInvertedCase400k,listInvertedCase500k, 
                            listInvertedCase1M, listInvertedCase2M]
timeSortInvertedCase = []

#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#

listRandomCase100k = generateList(value100k)
listRandomCase200k = generateList(value200k)
listRandomCase400k = generateList(value400k)
listRandomCase500k = generateList(value500k)
listRandomCase1M = generateList(value1M)
listRandomCase2M = generateList(value2M)


listQuestionRandomCase = [listRandomCase100k,listRandomCase200k,
                          listRandomCase400k, listRandomCase500k, 
                          listRandomCase1M, listRandomCase2M] 
timeSortRandomCase = []
for i in range(6):
    timeSortInvertedCase.append(timeit.
                                timeit("shellSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import shellSort, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("shellSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import shellSort, listInv, generateList",number = 1))
    print(i)

drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg")