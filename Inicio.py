from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image,ImageTk
from numpy import *
from prueba import *

def drag_start(event):
    global img_sel,seleccion_anterior
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    if seleccion_anterior!=-1:
        imagenesLabel[seleccion_anterior].config(bd=0)
    img_sel = imagenesLabel.index(widget)
    imagenesLabel[img_sel].config(bd=10,relief="groove")
    seleccion_anterior = img_sel

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

#Funcion con la que se pide una imagen al usuario
def addImg():
    global nomb_imagenes,imagenes,imagenesLabel,img_sel,seleccion_anterior
    #Pedir nombre del archivo
    nom_img = filedialog.askopenfilename(title="Seleccione archivo",filetypes=(("jpeg files",".jpg"),("png files",".png"),("all files",".*")))
    #Las siguientes 2 líneas utilizan PIL
    img = Image.open(nom_img)
    #img.size[0] #Esto es el número de columnas
    #img.size[1] #Esto es el número de filas
    nomb_imagenes.append(nom_img)
    imagenes.append(ImageTk.PhotoImage(file=nom_img))
    #label = Label(frame,image=imagenes[0],width=100,height=150)
    label = Label(frame,image=imagenes[len(imagenes)-1],width=img.size[0]-4,height=img.size[1]-4,bg="gray")
    label.place(x=100,y=100)
    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)
    imagenesLabel.append(label)
    img_sel = len(imagenes)-1
    imagenesLabel[img_sel].config(bd=10,relief="groove")
    if seleccion_anterior!=-1:
        imagenesLabel[seleccion_anterior].config(bd=0)
    seleccion_anterior = img_sel

def verHist():
    im=cv.imread(nomb_imagenes[img_sel])
    hist=cv.calcHist([im], [0], None, [256], [0, 256])
    #Histograma de la imagen original
    hist=h_original(im)

def despIzqHist():
    pass

def despDerHist():
    pass

#Raíz
root=Tk()
root.title("Ventana de pruebas")
root.geometry("900x700")
root.config(bd=20)

w=700
h=500
x=w/2
y=h/2
imagenes = list()
imagenesLabel = list()
nomb_imagenes = list()
seleccion_anterior = -1
img_sel = -1

bAddImg=Button(root,text="Abrir Imagen",command=lambda:addImg(),font=(18))
bAddImg.pack(pady=10)

#Tenemos que descubrir qué imagen se seleccionó con anterioridad y la pasamos a la funcion ver histograma
bVerHist=Button(root,text="Ver histograma",command=lambda:verHist(),font=(18))
bVerHist.pack(pady=10)

#Desplazamiento del histograma a la izquierda
bPrueba=Button(root,text="Desplazar histograma a la izquierda",command=lambda:despIzqHist(),font=(18))
bPrueba.pack(pady=10)

#Desplazamiento del histograma a la derecha
bPrueba=Button(root,text="Desplazar histograma a la derecha",command=lambda:despDerHist(),font=(18))
bPrueba.pack(pady=10)

frame=Frame(root,height=h,width=w,bg="gray")
frame.pack(pady=20,fill='both',expand=1)

root.mainloop()