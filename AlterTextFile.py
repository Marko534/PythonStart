# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:18:25 2022

@author: marko.ilioski
"""

Text = open ('PrvMojFile.txt', 'a')
Text.write('FFFFFFFF \n')

Text.close()

Text = open ('PrvMojFile.txt', 'r')
print (Text.read())