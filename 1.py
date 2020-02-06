#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:35:10 2019

@author: zhechenghe
"""

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    a = 0
    i = 0
    while i <= x:
        a += i**2
        i +=1
    return a

def f2(x):
    a = x**3
    return a

p = []
x = np.arange(0,100,1)
for i in range(len(x)):
    p.append(f1(x[i]))


plt.plot(x,p,color='r')
plt.plot(x,f2(x))
plt.show()


#class Dog():
#    #“一次模拟小狗的简单尝试”
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def sit(self):
#        #"模拟小狗被命令蹲下"
#        print(self.name+" is sitting down now!!!")
#    def roll_over(self):
#        #"模拟小狗被命令时打滚"
#        print(self.name +" rolled over!!!")
#my_dog=Dog('Dahuang',5)
#print("my dog's name is "+ my_dog.name+".It is "+str(my_dog.age)+ "years old")
#my_dog.sit()
#my_dog.roll_over()
#
#
#students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]  
#a = sorted(students, key=lambda dsda : dsda[1])
#print(a)
#
#from itertools import *
#import os,sys
#
#xyz = None
#
#if xyz == None and os.path.exists(bashrc):
#    xyz = 1
#else:
#    xyz = 0
#    
#print(xyz)
#    
#
#
#
#def height_class(h):
#    if h>180:
#        return 'tall'
#    elif h<160:
#        return 'short'
#    else:
#        return 'middle'
#
#
#friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
#
#
#friends = sorted(friends,key = height_class)
#print(friends)