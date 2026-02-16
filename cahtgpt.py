import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

label = tk.Label(root)
label.pack()

img1 = Image.open("DSCF7903.jpg")
img11 = img1.resize((150, 150))
img111 = ImageTk.PhotoImage(img11)
img2 = Image.open("DSCF7936.jpg")
img22 = img2.resize((150, 150))
img222 = ImageTk.PhotoImage(img22)

current = 0
images = [img111, img222]

def change_image():
    global current
    current += 1
    if current < len(images):
        label.config(image=images[current])
        label.image = images[current]  # keep reference

button = tk.Button(root, text="Next", command=change_image)
button.pack()

label.config(image=images[0])
label.image = images[0]

root.mainloop()
