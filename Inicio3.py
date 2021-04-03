from tkinter import *
import tkinter

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

img = PhotoImage(file='imagen1.jpg')
botonNuevo1 = tkinter.Button(width=500, height=500, image=img,justify="right")
botonNuevo1.place(x=500, y=100)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

botonNuevo1.bind("<Button-1>",drag_start)
botonNuevo1.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()