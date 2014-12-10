# -*- coding: utf-8 -*-
"""
Created on Sun Dec 07 14:04:37 2014

@author: san
"""
t=10;p=10;g=10
while p>=4 or g>=2:  
    e=(int(p/4)+int(g/2))
    p-=4;g-=2
    t+=e
    print t
    p=p%4+e;g=e+g%2
print t,p,g
