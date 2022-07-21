# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:48:02 2022

@author: marko.ilioski
"""

import PIL
  
img = PIL.Image.open("ImageForResolution.png")
  
wid, hgt = img.size
  
print(str(wid) + "x" + str(hgt))
