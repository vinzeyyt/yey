import tkinter as tk
from tkinter import simpledialog
import numpy as np
import cv2

# Tkinter input
opcam = tk.Tk()          # create the root window
opcam.withdraw()          # hide it

thisit = simpledialog.askstring(
    title="bittttccchh",
    prompt="Say 'please' if you want to open the camera:"
) 

# Open camera
cam = cv2.VideoCapture(0)

if thisit == "please":
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        height, width = frame.shape[:2]

        # Create black canvas
        iwan = np.zeros((height, width, 3), dtype=np.uint8)

        # Resize frame
        mal = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Create 7x7 grid
        row = np.hstack([mal]*7)
        son = np.vstack([row]*7)

        # Place grid on canvas
        iwan[0:son.shape[0], 0:son.shape[1]] = son

        # Show image
        cv2.imshow("lall", iwan)

        # Press 'l' to exit
        if cv2.waitKey(1) == ord('l'):
            break

    cam.release()
    cv2.destroyAllWindows()
else:
    print("\n" * 20)
    print("how dare you not say please")
