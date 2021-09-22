# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:25:53 2019

@author: TRAORE Cheick Amed
"""
#import MAILLAGE as mg
#from MAILLAGE import maillage
#import numpy as np
from numpy import zeros
#tab,tabool=maillage(11,13)
def defAccu(tab,tabool):
    #tab,tabool=maillage(Nl,Nc)
    if tabool[0]==0 and tabool[1]==0:
        return zeros((tab[0][0],tab[1][0])), tab[0][0],tab[1][0]
    elif tabool[0]==1 and tabool[1]==0:
        return zeros((tab[0][0]+1,tab[1][0])), tab[0][0]+1,tab[1][0]
    elif tabool[0]==0 and tabool[1]==1:
        return zeros((tab[0][0],tab[1][0]+1)), tab[0][0],tab[1][0]+1
    else:
        return zeros((tab[0][0]+1,tab[1][0]+1)), tab[0][0]+1,tab[1][0]+1
    
#ac,r,t=defAccu(tab,tabool)