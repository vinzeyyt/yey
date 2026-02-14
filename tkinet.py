import tkinter as tk
from tkinter import simpledialog

nes = tk.Tk()

yes =  simpledialog.askstring(title="Be a bitch", prompt="Please say 'please' to be a bitch:")

if yes == "please":
    print("You are a bitch!")
else:
    print("You are not a bitch!")