import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def h_original(im):
    #Histograma de imagen original
    im2=cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    hist=cv.calcHist([im2], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray' )
    plt.title("Histograma Original")
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('Original', im)
    cv.waitKey()
    
    return hist
    
# Función que muestra histogramas de los canales RGB
# Recibe como parámetro la ruta de la imagen
def histogramas_RGB(r_img):
    
    img = cv.imread(r_img)
    # Lista con los 3 histogramas
    histogramas = []
    # Histograma canal azul
    histogramas.append(cv.calcHist([img], [0], None, [256], [0, 256]))
    # Histograma canal Verde
    histogramas.append(cv.calcHist([img], [1], None, [256], [0, 256]))
    #Histograma canal Azul
    histogramas.append(cv.calcHist([img], [2], None, [256], [0, 256]))
    
    # Imprime los histogramas
    colores = ["blue", "green", "red"]
    for i in range (0,3):
        plt.plot(histogramas[i], color=colores[i] )
    plt.title("Histogramas Canales RGB")
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()

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
    plt.title("Histograma Desplazamiento Derecha")
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
    plt.title("Histograma Desplazamiento Izquierda")
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
    plt.title("Histograma Estiramiento")
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
    plt.title("Histograma Ecualización")
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    cv.imshow('Ecualización', im2)
    cv.waitKey()
    
# Función que realiza estrechamiento del histograma
# Recibe como parámetros la ruta de la imagen y los valores deseados de compresión
# Devuelve una nueva imagen (matriz numpy) con los cambios realizados
def estrechamiento(r_img, Cmin, Cmax):
    
    #Abre la imagen original
    img = cv.imread(r_img)
    
    #Crea una copia de la imagen en escala de grises
    nueva_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Valores de la formula
    rmin = np.amin(img)
    rmax = np.amax(img)

    # Cambio de valores a la imagen de acuerdo a la fórmula
    for i in range(0, nueva_img.shape[0]):
        for j in range(0, nueva_img.shape[1]):
            nueva_img[i,j] = round(((Cmax-Cmin)/(rmax-rmin))*nueva_img[i,j] + Cmin)
    
    # Calcula el histograma con estrechamiento
    nhistograma = cv.calcHist([nueva_img], [0], None, [256], [0, 256])
    # Muestra el histograma
    plt.plot(nhistograma, color='gray' )
    plt.title("Histograma Estrechamiento")
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    plt.show()
    
    # Muestra los cambios realizados en la imagen
    cv.imshow('Estrechamiento', nueva_img)
    cv.waitKey()
    
    return nueva_img

def principal():
    im=cv.imread("Imagen1.png")
    im2=cv.imread("Imagen1.png")
    hist=cv.calcHist([im2], [0], None, [256], [0, 256])
    a=50
    
    #Histograma de la imagen original
    hist=h_original(im)
    #Histogramas RGB
    histogramas_RGB("Imagen1.png")
    #Histograma desplazado a la derecha
    desplazamiento_d(im,a)
    #Histograma desplazado a la izquierda
    desplazamiento_i(im2,a)
    #Estiramiento del histograma
    estiramiento(hist,im2)
    #Histograma de la imagen ecualizada
    ecualizacion(im)
    # Estrechamiento de Histograma
    estrechamiento("Imagen1.png", 50, 150)
    
principal()