import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def h_original(im):
    #Histograma de imagen original
    im2=cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    hist=cv.calcHist([im2], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('Original', im)
    cv.waitKey()
    
    return hist
    

def desplazamiento_d(im,a):
    #DESPLAZAMIENTO HACIA LA DERECHA
    i=0
    while i<im.shape[0]:
        j=0
        while j<im.shape[1]:
            b,g,r=im[i,j]
            v0=int(b)+a
            v1=int(g)+a
            v2=int(r)+a
            if v0>255:
                v0=255
            if v1>255:
                v1=255
            if v2>255:
                v2=255
            im[i,j]=v0,v1,v2
            j+=1
        i+=1
    
    hist= cv.calcHist([im], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('DesDerecha', im)
    cv.waitKey()


def desplazamiento_i(im,a):
    #DESPLAZAMIENTO HACIA LA IZQUIERDA
    i=0
    while i<im.shape[0]:
        j=0
        while j<im.shape[1]:
            b,g,r=im[i,j]
            v0=int(b)-a
            v1=int(g)-a
            v2=int(r)-a
            if v0<0:
                v0=0
            if v1<0:
                v1=0
            if v2<0:
                v2=0
            im[i,j]=v0,v1,v2
            j+=1
        i+=1
    
    hist= cv.calcHist([im], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('DesIzquierda', im)
    cv.waitKey()

def estiramiento(hist,im):
    frec=[]
    
    k=0
    for i in range(0,hist.shape[0]):
        for j in range(0,hist.shape[1]):
            if hist[i,j]>0:
                frec.insert(k,i)
                k+=1
    
    minimo=frec[0]
    maximo=frec[len(frec)-1]
    
    i=0
    while i<im.shape[0]:
        j=0
        while j<im.shape[1]:
            b,g,r=im[i,j]
            v0=(int(b)-minimo)*255/(maximo-minimo)
            v1=(int(g)-minimo)*255/(maximo-minimo)
            v2=(int(r)-minimo)*255/(maximo-minimo)
            im[i,j]=v0,v1,v2
            j+=1
        i+=1
    
    hist2= cv.calcHist([im], [0], None, [256], [0, 256])
    plt.plot(hist2, color='gray' )
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('Estiramiento', im)
    cv.waitKey()

def ecualizacion(im):
    #ECUALIZACIÓN
    im2=cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    im2=cv.equalizeHist(im2)
    hist4=cv.calcHist([im2], [0], None, [256], [0, 256])
    plt.plot(hist4, color='gray' )
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('Ecualización', im2)
    cv.waitKey()

def principal():
    im=cv.imread("Imagen1.jpg")
    im2=cv.imread("Imagen1.jpg")
    hist=cv.calcHist([im2], [0], None, [256], [0, 256])
    a=50
    
    #Histograma de la imagen original
    hist=h_original(im)
    #Histograma desplazado a la derecha
    desplazamiento_d(im,a)
    #Histograma desplazado a la izquierda
    desplazamiento_i(im2,a)
    #Estiramiento del histograma
    estiramiento(hist,im2)
    #Histograma de la imagen ecualizada
    ecualizacion(im)