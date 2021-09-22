# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:59:54 2019

@author: TRAORE Cheick Amed
"""
#import time
import FACTORISATION as ft
#from prime import erastothene
#d=time.time()
def maillage(Nl,Nc):
    tab,tabool=[],[]
    tabool+=[ft.erastothene(Nl)]
    if tabool[0]:
        tab+=[ft.factorisation(Nl-1)]
    else:
        tab+=[ft.factorisation(Nl)]
    tabool+=[ft.erastothene(Nc)]
    if tabool[1]:
        tab+=[ft.factorisation(Nc-1)]
    else:
        tab+=[ft.factorisation(Nc)]
    return tab,tabool
#f=time.time()
#print('temps {}'.format(f-d))
#print('temp ',f-d)