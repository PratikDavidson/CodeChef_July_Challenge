# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:16:25 2021

@author: Binit
"""
def ans(L,R):
    if L == 1:
        return 1
    else:
        lc = chefora(L)
        s = A[R]-A[L]
        return pow(lc,s,1000000007)    
def chefora(N):
    if N > 9:
        s = str(N)
        s = s+s[-2::-1]
        N = int(s)
    return N
        
Q = int(input())
A = [0]
for i in range(1,100001):
    A.append(chefora(i)+A[i-1])
for _ in range(Q):
    L,R = map(int,input().split())
    print(ans(L,R))