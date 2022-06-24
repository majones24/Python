# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:51:42 2022

@author: micha
"""

a=int(39)
b=int(143)
qlist=[]
if a<b:
    list_1=[b]
    rlist=[a]
    
    while rlist[-1] > 0:
    
        rlist.append(list_1[-1]%rlist[-1])
        list_1.append(rlist[0])
        q=list_1[-1]
        rlist.pop(0)
        
        #for
                
    print(list_1[-1],rlist,list_1)
    
        

if a>b: 
    list_1=[a]
    rlist=[b]
    
    while list_1[-1] > 0:
    
        list_1.append(rlist[-1]%list_1[-1])
        rlist.append(list_1[0])
        list_1.pop(0)
    print(rlist[-1])


