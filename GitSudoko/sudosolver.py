#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 12:38:06 2020

@author: Ben
"""

#Sudoko solver

import pandas as pd
import numpy as np


df=pd.read_csv('su.csv',sep=';',header=None)
df=pd.DataFrame(df)

l=np.array(df)

def solvesud(l):
    overall=[]
    for it in range(9):
        for i1,el in enumerate(l[it]):
            sol1=[]
            overall.append(sol1)
            if el == 0:
                for x in l[:,i1]:
                    if x !=0:
                        sol1.append(x)
                for i in l[it]:
                    if i != 0:
                        sol1.append(i)
                
                if it< 3:
                    if i1 < 3:
                        
                        sol1.extend(l[0,0:3])
                        sol1.extend(l[1][0:3])
                        sol1.extend(l[2][0:3])
                    
                    if i1 > 3:
                        if i1 < 6:
                            sol1.extend(l[0][3:6])
                            sol1.extend(l[1][3:6])
                            sol1.extend(l[2][3:6])
            
                    if i1 > 6:
                        if i1 < 9:
                            sol1.extend(l[0][6:9])
                            sol1.extend(l[1][6:9])
                            sol1.extend(l[2][6:9])
                if it >3:
                    if it< 6:
                        if i1 < 3:
                            sol1.extend(l[3,0:3])
                            sol1.extend(l[4][0:3])
                            sol1.extend(l[5][0:3])
                        
                        if i1 > 3:
                            if i1 < 6:
                                sol1.extend(l[3][3:6])
                                sol1.extend(l[4][3:6])
                                sol1.extend(l[5][3:6])
                
                        if i1 > 6:
                            if i1 < 9:
                                sol1.extend(l[3][6:9])
                                sol1.extend(l[4][6:9])
                                sol1.extend(l[5][6:9])
                if it >6:
                    if it< 9:
                        if i1 < 3:
                            sol1.extend(l[6,0:3])
                            sol1.extend(l[7][0:3])
                            sol1.extend(l[8][0:3])
                        
                        if i1 > 3:
                            if i1 < 6:
                                sol1.extend(l[6][3:6])
                                sol1.extend(l[7][3:6])
                                sol1.extend(l[8][3:6])
                
                        if i1 > 6:
                            if i1 < 9:
                                sol1.extend(l[6][6:9])
                                sol1.extend(l[7][6:9])
                                sol1.extend(l[8][6:9])

                
                
                
                


    view =[]
    newnumb=[]
    for el in overall:
        el=sorted(el)
        el=list(dict.fromkeys(el))
        s= list(set(range(1,10)) - set(el)) 
        newnumb.append(s)
        view.append(el)
        
    #print(newnumb)
    
    for i2, so in enumerate(newnumb):
        
        if len(so)==1:
            print('hey')
            coord1=int(i2/9)
            coord2=int((i2%9))
            l[coord1,coord2]=so[0]

        

    return l     

d=solvesud(l)
#r=solvesud(d)
#x=solvesud(r)


x=0
while x< 100:
    x+=1
    r=solvesud(d)
    d=r
    