# -*- coding: utf-8 -*-+
"""
Created on Thu Nov 28 20:59:43 2019

@author: estudiante
"""
#This is a commentary just for you that are reading this
import random
import numpy as np
import cv2
imagen = cv2.imread("logo.jpg")

# Crea una imagen en negro

letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros='1234567890'
ciudades=['Pasto','Cali','Medellin']


for i in range (1):
    
    img = np.ones((428,905,3), np.uint8)
    imagen = cv2.imread("p.jpg")
    img[:,:]=(20,194,252)
    img = cv2.rectangle(img,(15,15),(890,415),(0,0,0),15)
        

    img = cv2.rectangle(img,(15,15),(890,415),(0,0,0),15)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(random.choice(letras+''))+str(random.choice(letras+''))+str(random.choice(letras+''))+str(random.choice(numeros+''))+str(random.choice(numeros+''))+str(random.choice(numeros+'')),(70,270), font, 6,(0,0,0),9,cv2.LINE_AA)
   # cv2.putText(img,str(random.choice(numeros))+str(random.choice(numeros))+str(random.choice(numeros)),(430,270), font, 6,(0,0,0),9,cv2.LINE_AA)
    cv2.putText(img,ciudades[random.randint(0,len(ciudades)-1)],(350,380), font, 2,(0,0,0),3,cv2.LINE_AA)
    
    cv2.imshow("", imagen)
    cv2.imshow(str(i),img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
