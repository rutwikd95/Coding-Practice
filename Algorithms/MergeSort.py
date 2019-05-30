# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:28:09 2019

@author: rutwi
"""

# Merge Sort using the Two Way Merging Algorithm :


def Merge(A, B, C):
    
    m = len(A)
    n = len(B)
    i=0
    j=0
    k=0
#    C= []
    while (i < m and j < n) :
        if (A[i] < B[j]):
            C[k] = (A[i])
            k +=1 
            i += 1
        else:
            C[k] = (B[j])
            k +=1
            j +=1
    while i < m  :
        C[k] = (A[i])
        i += 1
        k += 1 
    while j < n :
        C[k] = (B[j])
        j +=1
        k +=1
    return C


def MergeSort(MyList):
#    l = 0
#    h = len(MyList)
#    result = []
    if len(MyList) > 1  :
        mid = len(MyList)//2
        LeftPart = MyList[: mid]
        RightPart = MyList[mid : ]
        MergeSort(LeftPart )
        MergeSort (RightPart)
#        result.append(Merge(LeftPart , RightPart))
        Merge(LeftPart , RightPart, MyList)
#    return result
    return MyList


MyList = [3,5,1,8,2,9,10,6,7,4]

MergeSort(MyList)