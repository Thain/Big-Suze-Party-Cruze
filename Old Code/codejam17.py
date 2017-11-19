from tkinter import *
import pandas as pd
#import matplotlib.pyplot as plt
import pygal
from PIL import Image, ImageTk

root = Tk()

topFrame = Frame(root, width = 1000, height=1000)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
root.resizable(width=False, height=False)
root.geometry('520x500')


def button_pressed(borough):
    print(borough)
    label = Label(root, text=borough)
    label.pack(side=TOP)
    load = Image.open("/Users/raphaelletseng/Desktop/Screen Shot 2017-11-18 at 2.31.54 PM.png")
    load = load.resize((520,400), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    label_img = Label(root, image=render)
    label_img.image = render
    label_img.place(x=0, y=100)

button1 = Button(topFrame, text ='Brooklyn', command = lambda: button_pressed('Brooklyn'))
button2 = Button(topFrame, text = 'Queens', command = lambda: button_pressed('Queens'))
button3 = Button(topFrame, text = 'Bronx',command = lambda: button_pressed('Bronx'))
button4 = Button(topFrame, text = 'Manhattan',command = lambda: button_pressed ('Manhattan'))
button5 = Button(topFrame, text = 'Staten Island',command = lambda: button_pressed ('Staten Island'))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)

root.mainloop()
