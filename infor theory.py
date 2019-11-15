#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import numpy as np

a = np.array([[1/6,1/10,1/15],[2/15,1/10,1/10],[1/30,3/10,0]])

b = np.array([[1/2,1/5,2/5],[2/5,1/5,3/5],[1/10,3/5,0]])
res=0

for i in range(0,3):
    for j in range(0,3):
        if(a[i][j]!=0):
            res=res-a[i][j]*math.log(b[i][j],2)

print(res)
