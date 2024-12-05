from tkinter import *
from PIL import ImageTk,Image

def on_click(event):
    txt.configure(state="normal")
    txt.delete(0,END)

def on_click2(event):
    txt2.configure(state="normal")
    txt2.delete(0,END)
    txt2.configure(show="*")

root=Tk()
root.geometry("500x500")
photo=Image.open(r"E:\projects\login\batman-nawpic-32.jpg")
resize=photo.resize((500,500),Image.Resampling.LANCZOS)
pic=ImageTk.PhotoImage(resize)
root.configure(bg="black")
back=Label(root,image=pic)
back.pack()
txt=Entry(root,width=40,bd=0,selectforeground="black")
txt2=Entry(root,width=40,bd=0,selectforeground="black")
txt.insert(0,"Enter Name")
txt.configure(state="disabled")
txt2.insert(0,"Enter Password")
txt2.configure(state="disabled")
txt.bind("<Button-1>",on_click)
txt2.bind("<Button-1>",on_click2)
txt.place(x=150,y=400)
txt2.place(x=150,y=425)
bton=Button(root,text="LogIn",background="black",foreground="white",activebackground="black")
bton.place(x=240,y=450)
root.mainloop()