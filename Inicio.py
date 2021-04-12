from tkinter import *
from tkinter import filedialog
import cv2 as cv
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
    #print(img_sel)
    imagenesLabel[img_sel].config(bd=10,relief="groove")
    seleccion_anterior = img_sel

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

def button_hover(e):
    widget = e.widget
    if widget==b1:
        status_label.config(text="Ver histograma")
    elif widget==b2:
        status_label.config(text="Ver histograma RGB")
    elif widget==b3:
        status_label.config(text="Desplazar histograma a la izquierda")
    elif widget==b4:
        status_label.config(text="Desplazar histograma a la derecha")
    elif widget==b5:
        status_label.config(text="Estiramiento del histograma")
    elif widget==b6:
        status_label.config(text="Histograma de la imagen ecualizada")
    elif widget==b7:
        status_label.config(text="Estrechamiento del histograma")

def button_hover_leave(e):
    status_label.config(text="")

#Funcion con la que se pide una imagen al usuario
def addImg():
    global nomb_imagenes,im,imagenes,imagenesLabel,img_sel,seleccion_anterior
    #Pedir nombre del archivo
    nom_img = filedialog.askopenfilename(title="Seleccione archivo",filetypes=(("jpeg files",".jpg"),("png files",".png"),("all files",".*")))
    nomb_imagenes.append(nom_img)
    img = cv.imread(nom_img)
    h = img.shape[0]
    w = img.shape[1]
    im.append(img)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imagenes.append(ImageTk.PhotoImage(Image.fromarray(img)))
    label = Label(frame,image=imagenes[len(imagenes)-1],width=w,height=h,bg="gray")
    label.place(x=100,y=100)
    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)
    imagenesLabel.append(label)
    img_sel = len(imagenes)-1
    imagenesLabel[img_sel].config(bd=10,relief="groove")
    if seleccion_anterior!=-1:
        imagenesLabel[seleccion_anterior].config(bd=0)
    seleccion_anterior = img_sel

def agregar_img(img):
    global nomb_imagenes,im,imagenes,imagenesLabel,img_sel,seleccion_anterior
    #Pedir nombre del archivo
    nom_img = "nueva"
    nomb_imagenes.append(nom_img)
    h = img.shape[0]
    w = img.shape[1]
    im.append(img)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imagenes.append(ImageTk.PhotoImage(Image.fromarray(img)))
    label = Label(frame,image=imagenes[len(imagenes)-1],width=w,height=h,bg="gray")
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
    #Histograma de la imagen original
    print(img_sel)
    hist = h_original(im[img_sel])
    
#Hacer que reciba imagenes en lugar de el nombre
def verHistRGB():
    histogramas_RGB(im[img_sel])

def despIzqHist():
    a = 50
    img = desplazamiento_i(im[img_sel],a)
    agregar_img(img)

def despDerHist():
    a = 50
    img = desplazamiento_d(im[img_sel],a)
    agregar_img(img)

def estHist():
    hist=cv.calcHist([im[img_sel]], [0], None, [256], [0, 256])
    img = estiramiento(hist,im[img_sel])
    agregar_img(img)

def histEcual():
    img = ecualizacion(im[img_sel])
    agregar_img(img)

#Hacer que reciba imagenes en lugar de un nombre
def histEstr():
    img = estrechamiento(im[img_sel],50, 150)
    agregar_img(img)

def leer_imagen(nombre):
    img = cv.imread(nombre)
    alto, w, channel = img.shape
    nuevo_alto = 80
    escala = nuevo_alto/alto
    img = PhotoImage(file=nombre)
    if (escala-int(escala))!=0:
        img = img.zoom(int(escala*10))
        img = img.subsample(10)
    else:
        img = img.zoom(escala)
    return img

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
im = list()
nomb_imagenes = list()
seleccion_anterior = -1
img_sel = -1

Grid.rowconfigure(root,2,weight=1)
Grid.columnconfigure(root,0,weight=1)
Grid.columnconfigure(root,1,weight=1)
Grid.columnconfigure(root,2,weight=1)
Grid.columnconfigure(root,3,weight=1)
Grid.columnconfigure(root,4,weight=1)
Grid.columnconfigure(root,5,weight=1)
Grid.columnconfigure(root,6,weight=1)

bAddImg=Button(root,text="Abrir Imagen",command=lambda:addImg())
bAddImg.grid(row=0,column=0)

#Tenemos que descubrir qué imagen se seleccionó con anterioridad y la pasamos a la funcion ver histograma
img1 = leer_imagen("histograma2.png")
b1=Button(root,image=img1,width=80,command=lambda:verHist())
b1.grid(row=1,column=0)
b1.bind("<Enter>",button_hover)
b1.bind("<Leave>",button_hover_leave)

#Ver histograma RGB
img2 = leer_imagen("histograma.png")
b2=Button(root,image=img2,width=80,command=lambda:verHistRGB())
b2.grid(row=1,column=1)
b2.bind("<Enter>",button_hover)
b2.bind("<Leave>",button_hover_leave)

#Desplazamiento del histograma a la izquierda
img3 = leer_imagen("izquierda.png")
b3=Button(root,image=img3,width=80,command=lambda:despIzqHist())
b3.grid(row=1,column=2)
b3.bind("<Enter>",button_hover)
b3.bind("<Leave>",button_hover_leave)

#Desplazamiento del histograma a la derecha
img4 = leer_imagen("derecha.png")
b4=Button(root,image=img4,width=80,command=lambda:despDerHist())
b4.grid(row=1,column=3)
b4.bind("<Enter>",button_hover)
b4.bind("<Leave>",button_hover_leave)

#Estiramiento del histograma
img5 = leer_imagen("estiramiento.png")
b5=Button(root,image=img5,width=80,command=lambda:estHist())
b5.grid(row=1,column=4)
b5.bind("<Enter>",button_hover)
b5.bind("<Leave>",button_hover_leave)

#Histograma de la imagen ecualizada
img6 = leer_imagen("ecualizacion.png")
b6=Button(root,image=img6,width=80,command=lambda:histEcual())
b6.grid(row=1,column=5)
b6.bind("<Enter>",button_hover)
b6.bind("<Leave>",button_hover_leave)

#Estrechamiento del histograma
img7 = leer_imagen("estrechamiento.png")
b7=Button(root,image=img7,width=80,command=lambda:histEstr())
b7.grid(row=1,column=6)
b7.bind("<Enter>",button_hover)
b7.bind("<Leave>",button_hover_leave)

frame=Frame(root,height=h,width=w,bg="gray")
frame.grid(row=2,column=0,columnspan=7,sticky="nsew")

status_label = Label(root,text='',bd=1,relief=SUNKEN,anchor=E,font=(18),pady=10)
status_label.grid(row=3,column=0,columnspan=7,sticky="nsew")

root.mainloop()