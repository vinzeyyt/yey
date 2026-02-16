import tkinter as tk
from tkinter import simpledialog
import numpy as np
import cv2

opcam = tk.Tk() # this is the root window for the tkinter application, it is necessary to create it before using simpledialog
opcam.withdraw() # this hides the root window, we only want to show the dialog box

thisit = simpledialog.askstring(title="bittttccchh", prompt="Say 'please' if you want to open the camera:") 

cam = cv2.VideoCapture(0) # this opens the first cam device "0" if u have more webcam it can be 1, 2, etc.
width = int(cam.get(3)) # 3 is width
height = int(cam.get(4)) # 4 is height

#if thisit in ["please", "rotate"]: # can also be used instead of the if statement below
if thisit == "please" or thisit == "rotate":
     while True:
         ret, frame = cam.read() # ret ir return it returns if another app is using cam, frame is the captured image,
         if not ret:
            print("you are a bitch")
         mal = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # this resizes the "frame" to 1/4 of its original size, 0, 0 is just the parameter or placeholder for the fx and fy
         duh = np.hstack([mal] * 1)# np.hstack is horizontal stacking
         son = np.vstack([duh] * 1) # np.vstack is verltica stacking
         
         iwan = np.zeros((son.shape[0], son.shape[1], 3), dtype=np.uint8) # this is the holder for the image its just black without the code below but its essential for the shape
           # this used to be (height, width, 3) but i changed it to this to always fit the image regardless of the height and width of the image that will be shown

         iwan[0:son.shape[0], 0:son.shape[1]] = son # this takes "son" and places it to the "iwan" which is the black canvas

         if thisit == "rotate":
             iwan[0:son.shape[0], 0:son.shape[1]] = cv2.rotate(son, cv2.ROTATE_180) # this rotates the image 180 degrees

         cv2.imshow("lall", iwan) # "lall" is the window name, imshow shows the image, dang is the image
         if cv2.waitKey(1) == ord('l'): # waitkey is the delay in this case 1 millisecond so it captures an image every 1 millisecond, ord takes the ascii value of l and if pressed it proceeds to break
             break
else:
    print("\n" * 20)
    print("how dare you not say please")
    