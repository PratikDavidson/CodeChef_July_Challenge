# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:37:11 2021

@author: Binit
"""
def max_out(d,x,y,z):
    first_way = 7*x
    second_way = d*y + (7-d)*z
    return max(first_way,second_way)
T = int(input())
for _ in range(T):
    d,x,y,z = map(int,input().split())
    print(max_out(d,x,y,z))
        