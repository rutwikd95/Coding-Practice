# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:56:15 2019

@author: rutwi
"""

# Merging : Merging two sorted Lists

def Merge(A, B , m , n):
    i=0
    j=0
#    k=0
    C= []
    while (i < m and j < n) :
        if (A[i] < B[j]):
            C.append(A[i])
#            k +=1 
            i += 1
        else:
            C.append(B[j])
#            k +=1
            j +=1
    while i < m  :
        C.append(A[i])
        i += 1
    while j < n :
        C.append(B[j])
        j +=1
    return C
            
            
            
List1 = [1,3,5,7,9]
List2 = [2,4,6,8,10]

#print(List1[2])

m = len(List1)
n = len(List2)

Merge(List1, List2 , m , n)