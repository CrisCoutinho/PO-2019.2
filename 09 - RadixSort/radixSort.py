# -*- coding: utf-8 -*-
"""RadixSort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13KQ9HGq9tMhLPM7QIMvg6zSpwbdRP5sP
"""

import numpy as np
from random import shuffle, randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import math

mpl.use('Agg')
mpl.rc('lines', linewidth=2.9)
plt.style.use('ggplot')

sys.setrecursionlimit(10**7) 

def countingSort(elementList, n, place):                                         
    integerRange = 10;                                                         
    freq =[0 for i in range(0, integerRange)];                                 
    listSorted = [0 for i in range(0, n)];                                     
                                                                                
    for i in range(0, n):                                                       
        freq[(elementList[i]//place)%integerRange] += 1;                          
                                                                                
    for i in range(1, integerRange):                                           
        freq[i] += freq[i-1];                                                   
                                                                                
    i = n-1;                                                                    
    while (i>=0):                                                               
        listSorted[freq[(elementList[i]//place)%10]-1]=elementList[i];              
        freq[(elementList[i]//place)%10] -= 1;                                     
        i -= 1;                                                                 
                                                                                
    for j in range(0, n):                                                       
        elementList[j]=listSorted[j];                                            
                                                                                
def radixSort(elementList):                                                      
    n = len(elementList);                                                         
    maxElement = max(elementList);                                               
    mul=1;                                                                      
    while (maxElement):                                                        
        countingSort(elementList, n, mul);                                       
        mul *= 10;                                                              
        maxElement /= 10;                                                      
                                                                                
    return elementList;    







def drawGraph(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação", name =" Tempo de ordenação em seg"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    plt.scatter(x,y,marker='^',facecolor='red',edgecolors= 'red', linewidths=4)  
    ax.plot(x,y,color = 'blue', markerfacecoloralt ='green', label = "Aleatorio")
    plt.scatter(x,yInv,marker= 'v',facecolor='blue',edgecolors= 'blue', linewidths=4)  
    ax.plot(x,yInv, color = 'red', label = "Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(name)
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

#Casos testados:  100k, 200k, 300k, 400k, 500k, 1M e 2M 

listValueGraph = [100 ,200, 300 , 400, 500, 1000, 2000]
#~~~~~~~~~~ Tests ~~~~~~~~~~~#


value100k = 100000
value200k = 200000
value300k = 300000
value400k = 400000
value500k = 500000
value1M = 1000000
value2M = 2000000

#~~~~~~~~~~ List Inverted Case ~~~~~~~~~~~#

listInvertedCase100k = listInv(value100k)
listInvertedCase200k = listInv(value200k)
listInvertedCase300k = listInv(value300k)
listInvertedCase400k = listInv(value400k)
listInvertedCase500k = listInv(value500k)
listInvertedCase1M = listInv(value1M)
listInvertedCase2M = listInv(value2M)


listQuestionInvertedCase = [listInvertedCase100k,listInvertedCase200k,
                            listInvertedCase300k,listInvertedCase400k,
                            listInvertedCase500k,listInvertedCase1M, 
                            listInvertedCase2M]

timeSortInvertedCase = []



#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#

listRandomCase100k = generateList(value100k)
listRandomCase200k = generateList(value200k)
listRandomCase300k = generateList(value300k)
listRandomCase400k = generateList(value400k)
listRandomCase500k = generateList(value500k)
listRandomCase1M = generateList(value1M)
listRandomCase2M = generateList(value2M)



listQuestionRandomCase = [listRandomCase100k,listRandomCase200k,
                          listRandomCase300k,listRandomCase400k,
                          listRandomCase500k,listRandomCase1M,
                          listRandomCase2M] 
timeSortRandomCase = []




for i in range(7):
    timeSortInvertedCase.append(timeit.
                                timeit("radixSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import radixSort,countingSort, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("radixSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import radixSort, countingSort, listInv, generateList",number = 1))
    
    print(i)


drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg",
         name = "Tempo de ordenação em Seg RadixSort com CS")