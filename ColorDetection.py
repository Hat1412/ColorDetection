from tkinter import *
from pyautogui import pixel
from pynput.mouse import Listener

root = Tk()
root.config(bg = "#99d9ea")
root.attributes("-topmost",True)

RGB = IntVar()
HEX = IntVar()
switch = False

def on_click(x,y,_,pressed):
    global switch
    data = []
    if RGB.get():
        data.append(pixel(x,y))
    if HEX.get():
        color = '#%x%x%x' % pixel(x,y)
        data.append(color)

    if switch:
        root.clipboard_clear()
        root.clipboard_append(data)
        switch = False        


def get_color():
    global switch
    switch = True

Button(root,text = "Get Color",fg = "#FFFFFF",command = get_color,bg = "#22b14c",font = ("Times New Roman",15)).pack(padx = 10,pady = 10)
Checkbutton(root, text="RGB VALUE", variable=RGB,fg = "#ff7f27", onvalue=1, offvalue=0,
bg = "#88015c",font = ("Times New Roman",20)).pack(side = "left",padx = 10,pady = 10)

Checkbutton(root, text="HEX VALUE", variable=HEX,fg = "#ff7f27", onvalue=1, offvalue=0,state = "active",
bg = "#88015c",font = ("Times New Roman",20)).pack(side = "left",padx = 10,pady = 10)

with Listener(on_click=on_click) as listener:
    root.mainloop()
    listener.join()

