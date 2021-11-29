from tkinter import *
from pynput.mouse import Listener
from pyautogui import pixel
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk

root = Tk()
root.config(bg="#EFE4B0")
root.attributes("-topmost", True)

color = StringVar()
counter = 1
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)

history = Listbox(root, font=("Times New Roman", 20, "bold"), bg="#A349A4", fg="white")
history.pack(side="right", fill=Y)
history.insert(0, "History")
history.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=history.yview)

Entry(root, textvariable=color, font=("Times New Roman", 20, "bold"),
bg="#99D9EA").pack(padx=20, side="top")

Button(root,text="Copy Color",bg="#99D9EA",
    font=("Times New Roman", 20, "bold"),
    command = lambda: root.clipboard_append(color.get())).pack(side="top")

Label(root,text="Click Anywhere To View Color",
font=("Times New Roman", 20, "bold"),bg="#EFE4B0").pack(padx=30, pady=30)

fr = Frame(root, bg="black", bd=2)
fr.pack()


def on_click(x, y, _, pressed):
    global history, counter
    a = pixel(x, y)
    if pressed:
        color_code = f"""{a} {'#%02x%02x%02x' % (a[0], a[1], a[2])} """
        color.set(color_code)
        history.insert(counter, color_code)
        counter += 1


def tk_webcam():
    global label, cap, chk
    cap = cv2.VideoCapture(0)
    label = Label(root)
    label.pack(side="bottom")
    messagebox.showinfo("Webacam Started", "Press Q to stop webcam !")
    show_frames()


Button(fr,text="Turn on Webcam",bg="#7092BE",
    font=("Times New Roman", 20, "bold"),
    command=tk_webcam).grid(row=0, column=0)

Button(fr,text="Clear History", bg="#7092BE",
    font=("Times New Roman", 20, "bold"),
    command=lambda: history.delete(1, END)).grid(row=0, column=1)


def stop_webcam(tmp):
    cap.release
    label.pack_forget()


def show_frames():
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(20, show_frames)


with Listener(on_click=on_click) as listener:
    root.bind("q", stop_webcam)
    root.mainloop()
    listener.join()
