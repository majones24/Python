# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:50:36 2021

@author: micha
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

a=1
b=3
c=5
n=9

p=[[[0,0,0]],[[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]]
masterlist=[[0,0,0],[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]
X=[0,a,a,b,b,c,c]
Y=[0,b,c,a,c,a,b]
Z=[0,c,b,c,a,b,a]
i=2
check=1

while check==1:
    p.append([])
    
    for j in range(len(p[i-1])):
        if p[i-1][j][0] !=0 and p[i-1][j][1] !=0 and p[i-1][j][2] !=0:
            pm_1=(p[i-1][j][0]+a) % n
            pm_2=(p[i-1][j][1]+b) % n
            pm_3=(p[i-1][j][2]+c) % n
        
            pm_4=(p[i-1][j][0]+a) % n
            pm_5=(p[i-1][j][1]+c) % n
            pm_6=(p[i-1][j][2]+b) % n
        
            pm_7=(p[i-1][j][0]+b) % n
            pm_8=(p[i-1][j][1]+a) % n
            pm_9=(p[i-1][j][2]+c) % n
        
            pm_10=(p[i-1][j][0]+b) % n
            pm_11=(p[i-1][j][1]+c) % n
            pm_12=(p[i-1][j][2]+a) % n
        
            pm_13=(p[i-1][j][0]+c) % n
            pm_14=(p[i-1][j][1]+a) % n
            pm_15=(p[i-1][j][2]+b) % n
        
            pm_16=(p[i-1][j][0]+c) % n
            pm_17=(p[i-1][j][1]+b) % n
            pm_18=(p[i-1][j][2]+a) % n
        
            if [pm_1,pm_2,pm_3] not in masterlist:
                masterlist.append([pm_1,pm_2,pm_3])
                p[i].append([pm_1,pm_2,pm_3])
                X.append(pm_1)
                Y.append(pm_2)
                Z.append(pm_3)
            
            if [pm_4,pm_5,pm_6] not in masterlist:
                masterlist.append([pm_4,pm_5,pm_6])
                p[i].append([pm_4,pm_5,pm_6])
                X.append(pm_4)
                Y.append(pm_5)
                Z.append(pm_6)
            
            if [pm_7,pm_8,pm_9] not in masterlist:
                masterlist.append([pm_7,pm_8,pm_9])
                p[i].append([pm_7,pm_8,pm_9])
                X.append(pm_7)
                Y.append(pm_8)
                Z.append(pm_9)
            
            if [pm_10,pm_11,pm_12] not in masterlist:
                masterlist.append([pm_10,pm_11,pm_12])
                p[i].append([pm_10,pm_11,pm_12])
                X.append(pm_10)
                Y.append(pm_11)
                Z.append(pm_12)
        
            if [pm_13,pm_14,pm_15] not in masterlist:
                masterlist.append([pm_13,pm_14,pm_15])
                p[i].append([pm_13,pm_14,pm_15])
                X.append(pm_13)
                Y.append(pm_14)
                Z.append(pm_15)
        
            if [pm_16,pm_17,pm_18] not in masterlist:
                masterlist.append([pm_16,pm_17,pm_18])
                p[i].append([pm_16,pm_17,pm_18])
                X.append(pm_16)
                Y.append(pm_17)
                Z.append(pm_18)
        x=X
        y=Y
        z=Z
#x=[pm_1,pm_4,pm_7,pm_10,pm_13,pm_16]
#y=[pm_2,pm_5,pm_8,pm_11,pm_14,pm_17]
#z=[pm_3,pm_6,pm_9,pm_12,pm_15,pm_18]

        ax = plt.axes(projection ="3d")
        ax.scatter3D(x,y,z)
        ax.set_xlabel('Player 1\'s Chips')
        ax.set_ylabel('Player 2\'s Chips')
        ax.set_zlabel('Player 3\'s Chips')
        plt.show()
            
    if p[i]==[]:
        check=2
    i=i+1
    
#print(p)

