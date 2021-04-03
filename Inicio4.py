import cv2
from tkinter import *
import tkinter
import numpy as np
from PIL import Image, ImageTk

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)


window = Tk()

imagen = ImageTk.PhotoImage(Image.fromarray(cv2.imread('imagen1.jpg')))
#cv2.imshow('Prueba de imagen',imagen)
#imagen2 = cv2.imread('imagen2.png')
#cv2.imshow('Prueba de imagen 2',imagen2)
#cv2.waitKey(0)
lbl = tkinter.Label(window, image=imagen)
lbl.pack()
botonNuevo1 = tkinter.Button(width=500, height=500, image=imagen,justify="right")
botonNuevo1.place(x=500, y=100)

label2 = Label(window,image=imagen,width=100,height=150)
label2.place(x=100,y=100)

botonNuevo1.bind("<Button-1>",drag_start)
botonNuevo1.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()