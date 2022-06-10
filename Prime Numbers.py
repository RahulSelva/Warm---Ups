# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:24:23 2022

@author: raghul.selvam
"""

def prime_number(lower_limit, upper_limit):
    l=[2]
    for i in range(lower_limit,upper_limit):
        global j
        for j in range(2,i):
            if i%j==0:
                break
        if i%j!=0:
            if i not in l:
                l.append(i)
    return(l)
x=prime_number(1,200000)
print(len(x))
