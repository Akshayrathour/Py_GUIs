#this is a stylish clock which can become transparent

from tkinter import *
import tkinter.ttk as ttk
import time
import random

def brightness(b):         #this is to make transparent
    b=slider.get()
    root.attributes('-alpha',b)

def timer():
    hr=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    ampm=time.strftime("%p")
    # print(f"{hr}:{min}:{sec}")
    times.configure(text=f"{hr}:{min}:{sec} {ampm}")
    times.after(1,timer)

def close():
    root.destroy()

def changecolor():
    l=["orange","red","yellow","purple","#0492C2"]
    color=random.randint(0,4)
    times.configure(fg=l[color])

root=Tk()
root.geometry("250x70+1236+20")
# main_screen.minsize("250","200")
root.maxsize("250","70")
root.title("DigiClock")
root.configure(bg="black")
slider=ttk.Scale(root,from_=0.1, to=1.0,orient=HORIZONTAL,value=1.0,command=brightness)
closebton=Button(root,text="X",command=close,width=3,bg="black",fg="#0492C2")
colorbton=Button(root,text="Light",command=changecolor,width=3,bg="black",fg="#0492C2")
times=Label(root,font="italic 20",bg="black",fg="#0492C2")
slider.pack()
times.pack()
closebton.place(x=205,y=7)
colorbton.place(x=10,y=7)
root.overrideredirect(True)
timer()
root.mainloop()