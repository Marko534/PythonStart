# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:18:18 2022

@author: marko.ilioski
"""

def NumberOfElementsList( element, *list):
    Number = 0
    for i in words:
        if i == element:
            Number = Number +1
    return Number



words = [   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red']


print (words)
final = {}
for i in words:
    if i not in final:
        final.update({i: NumberOfElementsList(i, words)})
        
final = sorted(final.items(), key=lambda x: x[1])
print (final)

