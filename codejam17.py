from tkinter import *
import pandas as pd
import pygal
from PIL import Image, ImageTk
import Response as rsp

root = Tk()

topFrame = Frame(root, width = 1100, height=1200)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
root.resizable(width=False, height=False)
root.geometry('520x500')


def button_pressed(borough):
    load = Image.open("./piechart.png")
    load = load.resize((520,400), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    label_img = Label(root, image=render)
    label_img.image = render
    label_img.place(x=0, y=100)

    label = Label(root, text=rsp.getBoro(borough))
    label.pack(side=TOP)

button1 = Button(topFrame, text ='BROOKLYN', command = lambda: button_pressed('BROOKLYN'))
button2 = Button(topFrame, text = 'QUEENS', command = lambda: button_pressed('QUEENS'))
button3 = Button(topFrame, text = 'BRONX',command = lambda: button_pressed('BRONX'))
button4 = Button(topFrame, text = 'MANHATTAN',command = lambda: button_pressed ('MANHATTAN'))
button5 = Button(topFrame, text = 'STATEN ISLAND',command = lambda: button_pressed ('STATEN ISLAND'))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)

root.mainloop()
