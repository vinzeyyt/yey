import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

socool = tk.Tk() #makes the window

socool.geometry("500x500") #sets the size of the window

pil = Image.open("DSCF7903.JPG") #lets jpeg imgs be used cuz u cant use jpeg img only png in tinker
pill = pil.resize((150, 150)) # resized image
pilll = pill.rotate(90) # rotates image
imgg = ImageTk.PhotoImage(pilll) #this is the image that will be shown stored iin imgg
img = tk.PhotoImage(file="Screenshot 2026-02-12 134241.png") #adds an image to the program

socool.config(bg="#de95c5") #background color

socool.iconphoto(True,img) #sets the icon

def inpu():
    word = inp.get()
    if word == "lol":
         dang = Label(socool, text = "you are a bitch",font=("Aptos", 20, "bold"))
         dang.pack()
    else:
            socool.destroy()

inp = Entry()

inp.config(width=30) #how many characters can be inputed 

inp.pack()

def welp():
    texx = Label(socool, text="you are a bitch",
         font=("Aptos", 20, "bold"), #font style and size
         bg="#de95c5", #backrgound color
         fg="red", #text color
         relief=RAISED, #border
         bd=10, #border size
         padx=10, #how far the text is from border vertical
         pady=10, #how far the text is from border horizontal
         image=imgg, #adds an image
         compound=BOTTOM) #position of image from the text
    texx.place(x=150,y=200)

def wul():
    sunod = Label(socool,
        image=imgg)
    sunod.place(x=150,y=200)

choi = [welp, wul]
ind = 0

def biatch():
    global ind

    if ind == 0:
        choi[ind]() 
        ind += 1
    elif ind == 1:
        choi[ind]()
        ind += 1
    else:
        socool.destroy()

inpbut = Button(socool, text="type 'lol'", command=inpu)
inpbut.pack(side=BOTTOM)

button = Button(socool, text="click if you are a bitch", command=biatch, font=("Aptos", 15, "bold"), relief=RAISED, bd=10, padx=5, pady=5, bg="black", fg="blue", activebackground="green", activeforeground="white")
button.pack()

socool.bind("<Alt-l>", lambda event: socool.destroy()) #lambda is basically def but for keys/one time functions

socool.mainloop() #shows the window and keeps it open until you close it