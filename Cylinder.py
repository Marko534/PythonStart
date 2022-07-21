"""
Created on Thu Jul 21 14:18:24 2022

@author: marko.ilioski
"""
from math import pi

def SurfeceAreaCilindar(r, h):
    return 2*r*r*pi + 2*r*pi*h
    
def VolumeCilindar(r, h):
    return r*r*2*pi * h

x = input ("Radius")
y = input ("Height")


print ("Surfece Area = ", SurfeceAreaCilindar(x, y))
print ("\nVolume = ", VolumeCilindar(x, y))
