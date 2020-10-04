# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:59:37 2020

@author: Silverxenfx
"""

import string
import random
o=string.ascii_lowercase
alp=list(o)

pt=input('Enter the Plain text:')
pt=pt.replace(" ", "")
p=list(pt)

key=''
for i in range(len(p)):
    e=random.randint(0,26)
    m=alp[e]
    key+=m
print("Random key : ",key)
l=list(key)

cypher=''
for i in range(len(key)):
    a=alp.index(p[i])
    b=alp.index(l[i])
    c=(a+b)%26
    cypher+=alp[c]
print('cipher text is ',cypher)

decrypt=""


for i in range(len(p)):
    a=alp.index(cypher[i])
    b=alp.index(l[i])
    c=(a-b)%26
    decrypt+=alp[c]
print("Decryption: ",decrypt)