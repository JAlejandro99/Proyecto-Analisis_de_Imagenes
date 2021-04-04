from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image,ImageTk
from numpy import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

#Funcion con la que se pide una imagen al usuario
def addImg():
    global imagenes
    #Pedir nombre del archivo
    nom_img = filedialog.askopenfilename(title="Seleccione archivo",filetypes=(("jpeg files",".jpg"),("png files",".png"),("all files",".*")))
    #Las siguientes 2 líneas utilizan cv2
    img = cv2.imread(nom_img)
    imagenes = append(ImageTk.PhotoImage(Image.fromarray(img)),imagenes)
    label = Label(frame,image=imagenes[0],width=100,height=150)
    label.place(x=100,y=100)
    label.bind("<Button-1>",drag_start)
    label.bind("<B1-Motion>",drag_motion)

#Raíz
root=Tk()
root.title("Ventana de pruebas")
#root.config(bd=15,cursor="hand2")
root.geometry("900x700")
w=700
h=500
x=w/2
y=h/2
imagenes = array(0)

frame=Frame(root,height=h,width=w,bg="gray")
frame.pack(pady=50)

bAddImg=Button(root,text="Añadir Imagen",command=lambda:addImg(),font=(18))
bAddImg.pack()

root.mainloop()