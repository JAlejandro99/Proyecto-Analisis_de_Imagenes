from tkinter import *
from PIL import Image,ImageTk

#Raíz
root=Tk()
root.title("Ventana de pruebas")
#root.config(bd=15,cursor="hand2")
root.geometry("800x600")
w=600
h=400
x=w/2
y=h/2

my_canvas=Canvas(root,width=w,heigh=h,bg="gray")
my_canvas.pack(pady=20)

#Agregando una imagen
#img = PhotoImage(file="imagen2.png")
#my_image=my_canvas.create_image(260,125,anchor=NW,image=img)
#
nom_img="imagen1.jpg"
imagen = Image.open(nom_img)
img = ImageTk.PhotoImage(file=nom_img)
my_image=my_canvas.create_image(0,0,anchor=NW,image=img)

def move(e,nom_img2):
    global img
    imagen = Image.open(nom_img)
    img = ImageTk.PhotoImage(file=nom_img)
    my_image=my_canvas.create_image(e.x,e.y,image=img)
    my_label.config(text="Coordinates: x: "+str(e.x)+"y: "+str(e.y))

my_label = Label(root,text="")
my_label.pack(pady=20)

my_canvas.bind('<B1-Motion>',move)

root.mainloop()