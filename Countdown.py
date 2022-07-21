# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:02:07 2022

@author: marko.ilioski
"""

import time

def CountdowSeconds (TimeSeconds):
    while TimeSeconds > 0 :
        print (TimeSeconds)
        TimeSeconds =TimeSeconds - 1
        time.sleep(1)
    print ("BOOO!!!")
    
x = int(input("Time for a suprise \n"))
CountdowSeconds(x)
#aaaaaaaaa
