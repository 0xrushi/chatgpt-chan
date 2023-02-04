

import tkinter as tk
from tkinter import Label
import time
import os
import tkinter as tk
from tkinter import Label
from time import sleep
from PIL import Image, ImageTk
import random
import threading

root = tk.Tk()
root.geometry("450x650")

label = None

def show_slideshow(image):
    global index, label
    img = Image.open(image)
    img = img.resize((450, 650), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    if label is None:
        label = Label(root, image=photo)
        label.pack()
    else:
        label.config(image=photo)
    root.update()

# show_slideshow(image)
# sleep(5)
# show_slideshow(1)
# sleep(5)

def run_gui():
    root.mainloop()
thread = threading.Thread(target=run_gui)
thread.start()