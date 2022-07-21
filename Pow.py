"""
Created on Thu Jul 21 14:03:05 2022
Write a Python program to implement pow(x, n).
@author: marko.ilioski

Nez dali vaka se barase ili sam samo nez kako da go napram za float stepen ako e 
"""

import math

def pow (x, y ):
    final = 1.0
    if x == 0 and y == 0 :
        print ("AAAAA ERROR")
    elif y > 0:
        for i in range(y):
            final = final * x
    elif y < 0 :
        for i in range(-y):
            final = final / x
    return final

print (math.pow(5, -3))
print (pow(5, -3))
