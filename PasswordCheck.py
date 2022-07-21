# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:55:01 2022
o	Мин 8 карактери. DONE
o	Да има и карактери и бројки DONE
o	Најмалку еден карактер со големи букви. DONE
o	Најмалку еден карактер да е бројка DONE
o	Најмалку еден специјален карактер. 

@author: marko.ilioski
"""

class Password:
    def __init__(self, password):
        self.__password = password
        
    def __CheckLenght (self):
        return 8 < len (self.__password)
    
    def __LetersNumbers(self):
        return not(self.__password.isalpha() or self.__password.isnumeric())
    
    def __CapitalLower(self):
        return not(self.__password.islower() or self.__password.isupper())
    
    def __SpecialChar(self):
        return not self.__password.isalnum()
    
    def StrongPassword(self):
        return self.__CheckLenght() and self.__LetersNumbers() and self.__CapitalLower() and self.__SpecialChar()
        
P = Password("Marko534@")


print (P.StrongPassword())
