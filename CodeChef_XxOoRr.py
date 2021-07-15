# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:37:52 2021

@author: Binit
"""
def min_op(A,N,K):
    
    maxi = max(A)
    k = 1
    while maxi//2:
        maxi //= 2
        k += 1
    b = [0]*N
    s = [0]*k
    c = 0
    for i in range(N):
        b[i] = binary_op(A[i],k)
    for i in range(N):
        for j in range(k):
            s[j] += b[i][j]
    for i in range(k):
        if s[i]%K == 0:
            c += s[i]//K
        else:
            c += s[i]//K+1
    return c
def binary_op(a,k):
    b = [0]*k
    if a != 0:
        i = -1
        while a//2:
            b[i] = a%2
            a //= 2
            i -= 1
        b[i] = 1       
    return b.copy()
        
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    print(min_op(A,N,K))


    