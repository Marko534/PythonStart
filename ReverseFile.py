# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:33:27 2022

@author: marko.ilioski
"""

Text = open ('PrvMojFile.txt', 'r')
TextString = Text.read()

Text.close()

TextList = []
for i in TextString:
    TextList.append(i)

TextReverse = []

for i in TextList:
    TextReverse.insert(0, i)
    
FinalTextString = ''
for i in TextReverse:
    FinalTextString = FinalTextString + i
    
Text = open ('NewTextReverse.txt', 'w')
Text.write(FinalTextString)
Text.close()
print (FinalTextString)
