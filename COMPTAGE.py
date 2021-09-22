# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:43:54 2019

@author: TRAORE Cheick Amed
"""

def compt(A,C,n,img):
    k,l=0,0
    for i in range(A[0],C[0]+1):
        for j in range(A[1],C[1]+1):
            #print(i,j)
            if img[i,j,0]==n:
                k=k+1
            else:
                l=l+1
        
    return k/(l+k)
