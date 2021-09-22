# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:22:47 2019

@author: TRAORE Cheick Amed
"""

"Crible d'Erastothene"


def erastothene(n):
    root=int(n**0.5)
    i=2
    while i<=root:
        if n%i==0:
            return 0
        i=i+1
    return 1