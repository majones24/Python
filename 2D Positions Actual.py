# -*- coding: utf-8 -*-
import numpy as np

import matplotlib.pyplot as plt

a=1
b=3
n=9

p=[[[0,0]],[[a,b],[b,a]]]

masterlist=[[0,0],[a,b],[b,a]]
X=[0,a,b]
Y=[0,b,a]
i=2
check=1

while check==1:
    p.append([])
    
    for j in range(len(p[i-1])):
        
        if p[i-1][j][0] !=0 and p[i-1][j][1] !=0:
            k=(p[i-1][j][0]+a) % n
            l=(p[i-1][j][1]+b) % n
            o=(p[i-1][j][0]+b) % n
            m=(p[i-1][j][1]+a) % n
        #p[i].append([k,l])
        
            if [k,l] not in masterlist:
                masterlist.append([k,l])
                p[i].append([k,l])
                X.append(k)
                Y.append(l)
            if [o,m] not in masterlist:
                masterlist.append([o,m])
                p[i].append([o,m])
                X.append(o)
                Y.append(m)   
    
    #print(p[i])
    if p[i]==[]:
        check=2
    i=i+1
#check==2            
        #if p==[[]]:
            #check==2
print(p)
x=X
y=Y
            
plt.scatter(x,y)
plt.xlim(0,n)
plt.ylim(0,n)
plt.xlabel('Player 1\'s Chips each Turn')
plt.ylabel('Player 2\'s Chips each Turn')       
