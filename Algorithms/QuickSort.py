# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:40:27 2019

@author: rutwi
"""

# Quick Sort

def Partition(MyList, l , h) :
    pivot = MyList[0]
    i = l
    j = h
    
    while (i <= j):
        while (MyList[i] <= pivot):
            i = i + 1
        while (MyList[j] > pivot):
            j = j - 1
        
        #Swapping elements at i and j positions
        MyList[i] , MyList[j] = MyList[j] , MyList[i]
        i = i + 1
        j = j - 1
        
    
    if i <= j :
        MyList[0], MyList[j] = MyList[j], MyList[0]
    
    return j


def QuickSort(MyList, l , h ):
    l = 0
    h = len(MyList) - 1
    if(l < h):
        j = Partition(MyList , l , h)
        QuickSort(MyList, l , j)
        QuickSort(MyList, j+1 , h)
    return MyList


MyList = [3,5,1,8,2,9,10,6,7,4] 

print(" len of mylist = " , len(MyList))

l = 0
h = len(MyList) - 1
QuickSort(MyList, l , h)
        
        
            
    