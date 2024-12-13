# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:36:21 2024

@author: 115548
"""

def MixtureDP (A:str|list, B:str|list, C:str|list)->bool:
    n = len(A)
    m = len(B)
    s = len(C)
    sol=""
    
    if (n + m) != s:
        return False

    t=[[[False,""] for i in range(m+1)] for j in range(n+1)] 
    t[0][0][0] = True

    for i in range(n + 1):
        for j in range(m + 1):
            t[i][j][0] = t[max(0, i-1)][j][0] or t[i][max(0, j-1)][0]
            if t[i][j][0] and (i < n or j < m):
                k = i + j
                t[i][j][0] = False
                
                if i < n:
                    t[i][j][0] = t[i][j] or (A[i] == C[k])
                    t[i][j][1] = "A"
                    
                
                if j < m:
                    t[i][j][0] = t[i][j] or (B[j] == C[k])
                    t[i][j][1] = "B"
    for i in range(n+1):
        for j in range(m+1):
            if t[i][j][0] == False:
                sol+= f"{t[i][j][1]}"
                    

    return sol
for i in range(s):
    cnt1=0
    cnt2=0
    for j in range(cnt1,n):
        if A[j] == C[i]:
            sol += "A"
        if cnt1>=n:
            break
        else:
            cnt1+=1   
    if  A[j] == C[i]:
        break
        
    for k in range(cnt2,m):      
        if B[k] == C[i]:
            sol += "B"
            break
        cnt2+=1
        
for i in range(s):
    if i<n:
        j=i
    else:
        j=i-n
    if C[i]==A[j]:
        if j==i:
            sol+="A"
        if j==i-n:
            if A[j] != C[i-n]:
                sol+="A"
            else:
                sol+="B"
        
    if C[i]==B[j]and C[i]!=A[j]:
        sol+="B"