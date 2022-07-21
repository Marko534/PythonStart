# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:33:32 2022
f.	Write a Python program to reverse a string word by word.
@author: marko.ilioski
"""

Recenica = "Sekoe sabajle treba da trujam nekoj da mi otvori"


RecenicaList = Recenica.split()

RecenicaFlip = []
for i in RecenicaList:
    RecenicaFlip.insert(0, i)
    
RecenicaFinal = ''

for i in RecenicaFlip:
    RecenicaFinal = RecenicaFinal + ' ' + i

print (RecenicaFinal)

