from tkinter import *
import time
import math

def updateclock():
    hr=int(time.strftime("%I"))
    min=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))
    
    sec_x=sechandlen*math.sin(math.radians(sec*6))+100
    sec_y=-1*sechandlen*math.cos(math.radians(sec*6))+100
    c.coords(sechand,100,100,sec_x,sec_y)

    min_x=minhandlen*math.sin(math.radians(min*6))+100
    min_y=-1*minhandlen*math.cos(math.radians(min*6))+100
    c.coords(minhand,100,100,min_x,min_y)

    hr_x=hrhandlen*math.sin(math.radians(hr*30))+100
    hr_y=-1*hrhandlen*math.cos(math.radians(hr*30))+100
    c.coords(hrhand,100,100,hr_x,hr_y)

    root.after(1,updateclock)

root=Tk()
bgi=PhotoImage(file=r"E:\projects\Clocks\Untitled design (21).png")
root.configure(bg="black")
root.geometry("200x200+1295+20")
# root.maxsize("200","200")
root.minsize("200","200")
root.title("AnalogWatch")
# blable=Label(root,image=bgi)
sechandlen=64
minhandlen=55
hrhandlen=42
# blable.place(x=0,y=0,relheight=1,relwidth=1)
c=Canvas(root)
c.create_image(100,100,image=bgi)
sechand=c.create_line(100,100,100+sechandlen,100+sechandlen,width=1.5,fill="red")
minhand=c.create_line(100,100,100+minhandlen,100+minhandlen,width=2,fill="white")
hrhand=c.create_line(100,100,100+hrhandlen,100+hrhandlen,width=2.5,fill="yellow")
c.place(x=0,y=0)
updateclock()
root.mainloop()