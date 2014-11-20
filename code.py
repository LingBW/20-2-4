# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 14:20:32 2014

@author: bling


mon = input('the money: ')
tl = int(mon/2)
ygai = 0
ypin = 0
ls = int(mon/2)
while ls>1:
    print ls
    g=int(ls/2)
    tl=tl+int(ls/2)
    if ls%2 >=1:
        ygai= ygai+ls%2
        if (ygai/2)>=1:
            tl=tl+int(ygai/2)
            ygai=ygai-2
            g=g+1
                
    p=int(ls/4)
    tl=tl+int(ls/4)
    if ls%4>=1:
        ypin=ypin+ls%4
        if (ypin/4)>=1:
            tl=tl+int(ypin/4)
            ypin=ypin-4
            p=p+1
    
    ls=g+p

print tl

定错对象，，对象 应该是盖，空瓶
"""

a=10; b=10; c=0; s=10; # 


while a/2>0 or b/4>0:
    c=a/2+b/4
    a=c+a%2
    b=c+b%4
    s=s+c
print s
