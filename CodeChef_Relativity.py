# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:27:13 2021

@author: Binit
"""
def smallest_height(g,c):
    return int((c**2)/(2*g))
    pass
T = int(input())
for _ in range(T):
    g,c = map(int,input().split())
    print(smallest_height(g,c))