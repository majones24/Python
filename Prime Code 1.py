# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:10:16 2022

@author: micha
"""

numlist = []
primelist = []
bigprimes = []
bigprimetriples = []
littleprimes = []
r_1=2
r_2=1000
i=0

for m in range(r_1,r_2):
    numlist.append(m)
 
while len(numlist) > 0:
    primelist.append(numlist[0])
    for i in numlist[0:len(numlist)]:
        if i % primelist[(-1)] == 0:
            numlist.remove(i)    
print(primelist)


#for n in range(1,len(primelist)):
    #if primelist[n]%3==2 or primelist[n]%3==0:
        #bigprimes.append(primelist[n])
        #bigprimetriples.append((primelist[n]-1)*(primelist[n]-2))
    #if primelist[n]%3==1:
        
        
#print(bigprimetriples)        