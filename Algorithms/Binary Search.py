# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:09:34 2019

@author: rutwi
"""
# Binary Search (Requires Numbers already in Sorted Order) 

def BinSearch(Array, n , key):
    l = 0
    h = n
    while (l <= h):
            mid = ((l + h) // 2)
            if key == Array[mid]:
                return mid + 1
            elif key < Array[mid]:
                h = mid - 1
            else:
                l = mid + 1
    return 0 



myList = [10,20,30,40,50,60,70,80,90,100]
myList2 = [2,4,6,8,10]
n = len(myList2)
print (" n = ", n )
MyKey = 8

BinSearch(myList2,n , MyKey )
        