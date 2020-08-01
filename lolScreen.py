import time
import pyautogui
from tkinter import *
from PIL import Image, ImageTk
import os
import cv2

def window_capture():
	img = pyautogui.screenshot(region=[1642, 802,278,278]) # x,y,w,h
	img.save('lol.png')

tk=Tk()
canvas=Canvas(tk,width=600,height=600,bg = 'white')

while True:
	window_capture()
	img1 = cv2.imread('lol.png')
	x,y = img1.shape[0:2]
	img1 = cv2.resize(img1, (int(y*2), int(x*2)))
	im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))	
	img = ImageTk.PhotoImage(image = im1)
	#img = ImageTk.PhotoImage(file = filename)
	itext = canvas.create_image((300,300),image = img)
	canvas.pack()
	tk.update()
	tk.after(1000)
tk.mainloop()