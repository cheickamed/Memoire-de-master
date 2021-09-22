# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 14:48:29 2019

@author: TRAORE Cheick Amed
"""
import time
#import COMPTAGE as cpt
#from scipy import misc
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

import scipy.ndimage.filters as filters
import scipy.ndimage as ndimage
d=time.localtime()

img = cv2.imread('Lena-Canny.png')#tof.jpg

#print('image shape: ', img.shape)

#plt.imshow(img, )

#plt.savefig("image.png",bbox_inches='tight')

#plt.close()
#etape 2
#d1=time.localtime()
d2=time.time()

img_shape = img.shape

x_max = img_shape[0]
y_max = img_shape[1]

theta_max = math.pi 
theta_min = 0.0

r_min = 0.0
r_max = (x_max**2+ y_max**2)**0.5

r_dim = x_max 
theta_dim = y_max

hough_space = np.zeros((r_dim,theta_dim))
#A=(35,120)
#C=(180,150)
#i=A[0]
#j=C[0]
#print('Image ttttt',img[A[0],C[0],0],img[i,j,0])
#print('Comptage ', cpt.compt((35,120),(180,150),0,img))
#Accumulateur de donnée
for x in range(x_max):
    for y in range(y_max):
        if img[x,y,0] ==255:
            for itheta in range(theta_dim):
                theta = 1.0 * itheta * theta_max / theta_dim
                r = x * math.cos(theta) + y * math.sin(theta)
                ir = r_dim * ( 1.0 * r ) / r_max
                ir,itheta=round(ir),round(itheta)
                hough_space[ir,itheta] = hough_space[ir,itheta] + 1
           
#print(hough_space)
#f1=time.localtime()
f2=time.time()
#plt.imshow(hough_space, origin='lower')
#plt.xlim(0,theta_dim)
#plt.ylim(0,r_dim)

#tick_locs = [i for i in range(0,theta_dim,80)]
#tick_lbls = [round( (1.0 * i * theta_max) / theta_dim,1) for i in range(0,theta_dim,40)]
#plt.xticks(tick_locs)#, tick_lbls)

#tick_locs = [i for i in range(0,r_dim,60)]
#tick_lbls = [round( (1.0 * i * r_max ) / r_dim,1) for i in range(0,r_dim,20)]
#plt.yticks(tick_locs)#, tick_lbls)

#plt.xlabel(r'Theta')
#plt.ylabel(r'r')
#plt.title('Espace de Hough')
#plt.savefig('Espace-Hough-Sans.png', bbox_inches = 'tight')
#plt.close()
print('en seconde',f2-d2)
#----------------------------------------------étape 3------------------------
#Trouver les maxima de la matrice d'accumulation
neighborhood_size = 40
threshold = 150

data_max = filters.maximum_filter(hough_space, neighborhood_size)
maxima = (hough_space == data_max)

data_min = filters.minimum_filter(hough_space, neighborhood_size)
diff = ((data_max - data_min) > threshold)
maxima[diff == 0] = 0

labeled, num_objects = ndimage.label(maxima)
slices = ndimage.find_objects(labeled)
#print(labeled, len(labeled[0]))

x, y = [], []
for dy,dx in slices:
    x_center = (dx.start + dx.stop - 1)/2
    x+=[x_center]
    y_center = (dy.start + dy.stop - 1)/2    
    y+=[y_center]

#print(x)
#print(y)
#f=open("Accumulateur",'w')
#for i in range(hough_space.shape[0]):
#    for j in range(hough_space.shape[1]):
#        f.write(str(hough_space[i,j]))
#f.close()
#  (x,y) représentent les coordonnées du centre des rectangle ayant un grand vote dans leur voisinage, ici 20
#plt.imshow(hough_space, origin='lower')
#plt.savefig('hough_space_i_j.png', bbox_inches = 'tight')
#plt.autoscale(False)
#plt.plot(x,y, 'ro')
#plt.savefig('hough_space_maximas.png', bbox_inches = 'tight')
#plt.close()

#-----------------------------étape 4-------------------------------------
#Construire les droites détectées
line_index = 0
for i,j in zip(y, x):

    r = round( (1.0 * i * r_max ) / r_dim,1)
    theta = round( (1.0 * j * theta_max) / theta_dim,1)

    fig, ax = plt.subplots()

    ax.imshow(img)

    ax.autoscale(False)

    px = []
    py = []
    for i in range(-y_max,y_max,1):
        px+=[ math.cos(-theta) * i - math.sin(-theta) * r ] #j
        py+=[ math.sin(-theta) * i + math.cos(-theta) * r ] #j

    ax.plot(px,py, linewidth=5)

    #plt.savefig("image_line_"+ "%02d" % line_index +".png",bbox_inches='tight')

    plt.show()

    #plt.close()

    line_index = line_index + 1
f=time.time()
print('Le temps écoulé est: ',f-d2)
print('droites detectees ',line_index)