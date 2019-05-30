# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:38:43 2019

@author: rutwi
"""

# Recursive Binary Search

def RBinSearch(Array, l , h, key):
    if l==h:
        if Array[l] == key:
            return l
        else:
            return 0
    
    else:
        mid = (l+h)//2 
        if key == Array[mid]:
            return mid
        elif key < Array[mid]:
            return RBinSearch(Array, l, mid -1 ,key)
        else:
            return RBinSearch(Array , mid + 1 , h, key)
        
        
        
myList = [10,20,30,40,50,60,70,80,90,100]
myList2 = [2,4,6,8,10]
n = len(myList)
print (" n = ", n )
MyKey = 90

RBinSearch(myList ,0 , n , MyKey )
        