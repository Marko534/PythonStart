# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:51:05 2022

@author: marko.ilioski
"""

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
    
nterms = 100

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
       
recur_fibo(10)
#DDDDDDDDD