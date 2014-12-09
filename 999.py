# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 12:56:13 2014

@author: bling


for i in range(1000):
    if i%7==0:
        print i
        continue
    for j in str(i):
        if j=='7':
            print i
"""
l=[]
p=[]
for i in range(999):
    
    if len(str(i))==1:
        l.append('00'+str(i))
        continue
    if len(str(i))==2:
        l.append('0'+str(i))
        continue
    l.append(str(i))
for i in l:
    r=[]
    for j in i:
        r.append(j)
    if r[0]!=r[1] and r[1]!=r[2] and r[0]!=r[2]:
        p.append(i)
        print i
print p,len(p)
