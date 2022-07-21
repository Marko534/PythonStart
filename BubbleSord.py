# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:01:38 2022

@author: marko.ilioski
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            if array[j] > array [j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

test = [6, 7, 4, 5, 8, 155, -7]

print (test)

test = bubbleSort(test)

print (test)