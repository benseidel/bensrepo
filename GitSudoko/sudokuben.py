#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:51:25 2020

@author: Ben
"""
import pandas as pd
import numpy as np
from getbox import getbox
import time

df=pd.read_csv('su1.csv',sep=';',header=None)
df=pd.DataFrame(df)

l=np.array(df)




def prove(y,x,n):
    global l
    if n in l[y,0:9]:
        return False
    if n in l[0:9,x]:
        return False
    if n in getbox([y,x],l):
        return False
    return True



def intelsolv():
    global l
    missingpoints=[]
    coords=np.argwhere(l==0)
    for coord in coords:
        y=coord[0]
        x=coord[1]
        gather=[]
        gather.extend(l[y,0:9])
        gather.extend(np.transpose(l[0:9,x]))
        gather.extend(getbox([y,x],l))
        lostnumbers=list(set(range(0,10))-set(gather))
        missingpoints.append([[y,x],lostnumbers])

    sornumb=sorted(missingpoints, key=lambda l: (len(l[1])))
    
    for misnum in sornumb:
        if len(misnum)==1:
            y=misnum[0][0]
            x=misnum[0][1]
            l[y,x] = misnum[1][0]
        else:
            for n in misnum[1]:
                y=misnum[0][0]
                x=misnum[0][1]
                if prove(y,x,n):
                    l[y,x] = n
                    intelsolv()
                    l[y,x] = 0
        return
    print(l)

start = time.time()
intelsolv()
print( "solved in {} seconds".format( time.time() - start ) )