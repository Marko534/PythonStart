# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:42:11 2022
Write a Python class which has two methods
 set_String and print_String. set_String accept a string
 from the user and print_String print the string in upper case.
@author: marko.ilioski
"""

class StringClass:
    def __init__ (self, zbor = ''):
        self.zbor = zbor
        
    def set_String(self, zbor):
        self.zbor = zbor
        
    def print_String(self):
        print (self.zbor.upper())
        
x = StringClass('Ova e test')
x.print_String()
x.set_String('Mnogu fenomenalen test')
x.print_String()

    
        
