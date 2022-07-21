# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:47:25 2022

@author: marko.ilioski
"""

x = int(input("Number \n"))

Factorial = 1

while x>0:
    Factorial = Factorial*x
    x = x - 1
print (Factorial)