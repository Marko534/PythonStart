# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:08:04 2022

@author: marko.ilioski
"""

import queue

MyFirstQueue= queue.Queue()

for i in range(10):
    MyFirstQueue.put(i)
    

for i in range(10):
    print(MyFirstQueue.get())
    MyFirstQueue.put(i)
    
