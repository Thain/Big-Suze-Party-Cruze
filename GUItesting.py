from tkinter import *
import pandas as pd
import pygal
from PIL import Image, ImageTk
import Response as rsp

root = Tk()
cv = Canvas(root, width=200, height=150)

topFrame = Frame(root, relief=RIDGE, borderwidth=5)
topFrame.pack(padx=4,pady=3)
botFrame = Frame(root)
botFrame.pack(side=BOTTOM,padx=4,pady=3)

def boro_pressed(borough):
	
	top = Toplevel()
	top.title("Borough Information…")
	msg = Message(top, text=rsp.getBoro(borough))
	msg.pack(side=TOP)
	load = Image.open("./piechart.png")
	load = load.resize((520,400), Image.ANTIALIAS)
	render = ImageTk.PhotoImage(load)
	label_img = Label(top, image=render)
	label_img.image = render
	label_img.pack(side=TOP)
	button = Button(top, text="Dismiss", padx=3, pady=1, command=top.destroy)
	button.pack(side=BOTTOM)

    #place_holder = Label(root)
    #place_holder.grid(row=0, column = 0)

def go_pressed(zc):
	nH = rsp.getNeighborhood(int(zc))
	cas = rsp.getCasualties(int(zc))
	zcnH = 'Your zip code ' + zc + ' is ' + nH + ' and has had ' + str(cas) + ' casualties in the period of January 2015 to February 2017.'
	top = Toplevel()
	top.title('Zip Code Info…')
	msg = Message(top, text=zcnH)
	msg.pack()
	button = Button(top, text="Dismiss", padx=3, pady=1, command=top.destroy)
	button.pack()

button1 = Button(botFrame, text ='Brooklyn', padx=4, command = lambda: boro_pressed('BROOKLYN'))
button2 = Button(botFrame, text = 'Queens', padx=4, command = lambda: boro_pressed('QUEENS'))
button3 = Button(botFrame, text = 'The Bronx', padx=4, command = lambda: boro_pressed('BRONX'))
button4 = Button(botFrame, text = 'Manhattan', padx=4, command = lambda: boro_pressed ('MANHATTAN'))
button5 = Button(botFrame, text = 'Staten Island', padx=4, command = lambda: boro_pressed ('STATEN ISLAND'))

label_1=Label(topFrame, text = "Where do you live? Insert a zipcode.")
entry_1 =Entry(topFrame)
button6 = Button(topFrame, text ='GO', command = lambda: go_pressed(entry_1.get()))

button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
button4.grid(row = 0, column = 3)
button5.grid(row = 0, column = 4)

label_1.grid(row = 3, column = 0)
entry_1.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)

root.mainloop()
