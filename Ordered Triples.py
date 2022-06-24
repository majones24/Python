# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:01:24 2022

@author: micha
"""

numlist=[]
primelist=[]
r_1=2
r_2=6000
i=0

for m in range(r_1,r_2+1):
    numlist.append(m)

while len(numlist)>0:
    primelist.append(numlist[0])
    for i in numlist[0:len(numlist)]:
        if i % primelist[-1]==0:
            numlist.remove(i)
#print(primelist)
littleprimes=[]
bigprimes=[]
bigprimetriples=[]
for n in range(1,len(primelist)):
    if primelist[n]%3==2 or primelist[n]%3==0:
       #bigprimes.append(primelist[n])
        bigprimetriples.append((primelist[n]-1)*(primelist[n]-2))
    if primelist[n]%3==1:
        littleprimes.append(primelist[n])
remainders=[]
cubes=[]
blist=[]
littleprimetriples=[]
for r in range(len(littleprimes)):
    for k in range(1,littleprimes[r]):
        x=(k**3) % littleprimes[r]
        remainders.append(x)
        remainders.sort()
       # for j in remainders:
            #if j not in cubes:
             #   cubes.append(j)
              #  cubes.sort()      
        for t in range(len(remainders)):
            if remainders[t]==(remainders[t-1]+1) and remainders[t] not in blist:
                blist.append(remainders[t])
                #blist.sort()    
    remainders.clear()        
    #print(littleprimes[r],",",len(blist))  
    #print(blist)
    littleprimetriples.append(3*len(blist)*(littleprimes[r]-1))
    blist.clear()    
#print(littleprimetriples)    
print(sum(littleprimetriples)+sum(bigprimetriples))