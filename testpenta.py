# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:11:01 2019

@author: TRAORE Cheick A. D. Gabriel pour utilisation personnelle et non commerciale
"""
import cv2 
#from FACTORISATION import factorisation
import matplotlib.pyplot as plt
from MAILLAGE import maillage
from DEFIACCU import defAccu
from COMPTAGE import compt
import math
import time

import scipy.ndimage.filters as filters
import scipy.ndimage as ndimage


img=cv2.imread('Pentagon-Canny.png')
def select_recogRf(a,n,s,img):
    d1=time.time()
    #print(img.shape)
    Nl=img.shape[0]
    Nc=img.shape[1]
    tab, tabool=maillage(Nl,Nc)
    h=tab[0][0]*tab[0][1]
    l=tab[1][0]*tab[1][1]
    #d=tab[0][1]*tab[1][1]
    theta_max=math.pi
    r_max=(Nl**2+Nc**2)**0.5
    acc, r_dim, theta_dim=defAccu(tab,tabool)
    for x in range(0,h-tab[0][1],tab[0][1]):
        for y in range(0,l-tab[1][1],tab[1][1]):
            #A=(x,y)
            #C=(x+tab[0][1],y+tab[1][1])
            #print(compt((x,y),(x+tab[0][1],y+tab[1][1]),n,img))
            if (compt((x,y),(x+tab[0][1],y+tab[1][1]),n,img))>=a:
                for z in range(x,x+tab[0][1]+1):
                    for k in range(y,y+tab[1][1]+1):
                        if img[z,k,0] ==n:
                            for itheta in range(theta_dim):
                                theta = 1.0 * itheta * theta_max / theta_dim
                                r = z* math.cos(theta) + k * math.sin(theta)
                                ir = r_dim * ( 1.0 * r ) / r_max
                                ir,itheta=round(ir),round(itheta)
                                acc[ir,itheta] = acc[ir,itheta] + 1
    #premier Si
    if tabool[0]==1 and tabool[1]==0:
        x=h
        for y in range(0,l):
            if img[x,y,0]==n:
                for itheta in range(theta_dim):
                    theta = 1.0 * itheta * theta_max / theta_dim
                    r = z* math.cos(theta) + k * math.sin(theta)
                    ir = r_dim * ( 1.0 * r ) / r_max
                    ir,itheta=round(ir),round(itheta)
                    acc[ir,itheta] = acc[ir,itheta] + 1
    #deuxieme Si             
    if tabool[0]==0 and tabool[1]==1:
        y=l
        for x in range(0,h):
            if img[x,y,0]==n:
                for itheta in range(theta_dim):
                    theta = 1.0 * itheta * theta_max / theta_dim
                    r = z* math.cos(theta) + k * math.sin(theta)
                    ir = r_dim * ( 1.0 * r ) / r_max
                    ir,itheta=round(ir),round(itheta)
                    acc[ir,itheta] = acc[ir,itheta] + 1
    #dernier Si
    if tabool[0]==1 and tabool[1]==1:
        x=h
        for y in range(0,l):
            if img[x,y,0]==n:
                for itheta in range(theta_dim):
                    theta = 1.0 * itheta * theta_max / theta_dim
                    r = z* math.cos(theta) + k * math.sin(theta)
                    ir = r_dim * ( 1.0 * r ) / r_max
                    ir,itheta=round(ir),round(itheta)
                    acc[ir,itheta] = acc[ir,itheta] + 1
        y=l
        for x in range(0,h):
            if img[x,y,0]==n:
                for itheta in range(theta_dim):
                    theta = 1.0 * itheta * theta_max / theta_dim
                    r = z* math.cos(theta) + k * math.sin(theta)
                    ir = r_dim * ( 1.0 * r ) / r_max
                    ir,itheta=round(ir),round(itheta)
                    acc[ir,itheta] = acc[ir,itheta] + 1
    #---------------------------------------------------------------------
    f2=time.time()
    
    plt.imshow(acc,origin='lower')
    plt.xlim(0,theta_dim)
    plt.ylim(0,r_dim)
    print('en seconde',f2-d1)
    #plt.savefig('alpha=0 s=100',bbox_inches='tight')
    #----------------------------------------------étape 3------------------------
    #Recherche des maxima dans la matrice d'accumulation

    neighborhood_size = 20
    threshold = s        #seuil

    data_max = filters.maximum_filter(acc, neighborhood_size)
    maxima = (acc == data_max)

    data_min = filters.minimum_filter(acc, neighborhood_size)
    diff = ((data_max - data_min) > threshold)
    maxima[diff == 0] = 0

    labeled, num_objects = ndimage.label(maxima)
    slices = ndimage.find_objects(labeled)

    x, y = [], []
    for dy,dx in slices:
        x_center = (dx.start + dx.stop - 1)/2
        x+=[x_center]
        y_center = (dy.start + dy.stop - 1)/2    
        y+=[y_center]
    #-----------------------------étape 4-------------------------------------
   #Construire les droites détectées
    line_index = 0
    for i,j in zip(y, x):
        r = round( (i * r_max ) / r_dim,1)
        theta = round( (j * theta_max) / theta_dim,1)
        fig, ax = plt.subplots()
        ax.imshow(img)
        ax.autoscale(False)

        px = []
        py = []
        for i in range(-Nc,Nc,1):
            px+=[ math.cos(-theta) * i - math.sin(-theta) * r ] 
            py+=[ math.sin(-theta) * i + math.cos(-theta) * r ]

        ax.plot(px,py, linewidth=5)
      #  plt.savefig("image_line1_"+ "%02d" % line_index +".png",bbox_inches='tight')
        plt.show()

        line_index = line_index + 1
    ff=time.time()
    print('Le temps final est: ',ff-d1,'Nombre de droites',line_index)



