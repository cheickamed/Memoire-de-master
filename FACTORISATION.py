# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:09:23 2019

@author: TRAORE Cheick Amed
"""

"Algorithme de factorisation d'entiers"
"Précondition l'entier doit être composé"
#import prime
from prime import erastothene

def factorisation(Nl):
    k=2
    #global tab
    tab=[]
    while k<=int(Nl**0.5):
        if Nl%k==0 and erastothene(k):
            tab=tab+[k]
        k=k+1
    #print(tab)
    #if tab[0]==2:
     #   k2=tab[1]
    #else:
     #   k2=tab[0]
    #k1=int(Nl/k2)
    #return k1,k2
    k=len(tab)
   # print(k,len(tab))
    k=k//2
   # print(k)
    k2=tab[k]
    k1=Nl//k2
    return k1,k2
