# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:37:52 2021

@author: Binit
"""
import time

def opt_denomination(emps,N):
   if N == 1:
       return 1
   elif N == 2:
       return 2
   else:
       s = []
       forward_hcf = [0]*N
       backward_hcf = [0]*N
       forward_hcf[0] = emps[0]      
       backward_hcf[N-1] = emps[N-1]
       for i in range(1,N):
           forward_hcf[i] = find_gcd(forward_hcf[i-1],emps[i])
       for i in range(-2,-(N+1),-1):
           backward_hcf[i] = find_gcd(backward_hcf[i+1],emps[i])
       print(forward_hcf)
       print(backward_hcf)
       mid_hcf = [backward_hcf[1]]
       for i in range(1,N-1):
           mid_hcf.append(find_gcd(forward_hcf[i-1],backward_hcf[i+1]))
       mid_hcf.append(forward_hcf[N-2])
       print(mid_hcf)
       ts = sum(emps)
       for i in range(N):
           s.append((ts-emps[i])//mid_hcf[i]+1)
       return min(s) 
           

def find_gcd(x, y):
    if y == 0:
        return x
    else:
        return find_gcd(y,x%y)
ts = time.time()           
T = int(input())
for _ in range(T):
    N = int(input())
    emps = list(map(int,input().split()))
    print(opt_denomination(emps,N))
te = time.time()
print(te-ts)

    