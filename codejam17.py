from tkinter import *
import pandas as pd
import pygal
from PIL import Image, ImageTk
import Response as rsp

root = Tk()

root.resizable(width=False, height=False)
root.geometry('600x600')

topFrame = Frame(root, width = 3000, height=3000)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


def button_pressed(borough):

    label = Label(root, text=rsp.getBoro(borough))
    label.grid(row = 1, sticky=W+E)

    load = Image.open("./piechart.png")
    load = load.resize((520,400), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    label_img = Label(root, image=render)
    label_img.image = render
    label_img.grid(row = 2, column = 0)

    place_holder = Label(root)
    place_holder.grid(row=0, column = 0)

button1 = Button(topFrame, text ='BROOKLYN', command = lambda: button_pressed('BROOKLYN'))
button2 = Button(topFrame, text = 'QUEENS', command = lambda: button_pressed('QUEENS'))
button3 = Button(topFrame, text = 'BR   ONX',command = lambda: button_pressed('BRONX'))
button4 = Button(topFrame, text = 'MANHATTAN',command = lambda: button_pressed ('MANHATTAN'))
button5 = Button(topFrame, text = 'STATEN ISLAND',command = lambda: button_pressed ('STATEN ISLAND'))

label_1=Label(bottomFrame, text = "Where do you live? Insert a zipcode.")
entry_1 =Entry(bottomFrame)
button6 = Button(bottomFrame, text ='GO')

button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
button4.grid(row = 0, column = 3)
button5.grid(row = 0, column = 4)

label_1.grid(row = 3, column = 0)
entry_1.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)

root.mainloop()
