#this is a digital clock,not so stylish with a stopwatch and alarm fearture.

from tkinter import *
import time
import threading
import sys
from plyer import notification

def timer():
    hr=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    ampm=time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%Y")
    day=time.strftime("%A")
    week_no=time.strftime("%U")
    # print(f"{hr}:{min}:{sec}")
    times.configure(text=f"{hr}:{min}:{sec} {ampm}")
    daylabel.configure(text=day)
    datelabel.configure(text=f"Date:{date}.{month}.{year}")
    times.after(1,timer)

mcount=0
scount=0
hrcount=0
stopthread=1
def strartcount(mincount=0,seccount=0,hourcount=0):
    if(seccount==60):
        seccount=0
        mincount+=1
    if(mincount==60):
        mincount=0
        hourcount+=1
    global mcount,scount,hrcount
    mcount=mincount
    scount=seccount
    hrcount=hourcount

    counterlabel.configure(text=f"{hourcount}:{mincount}:{seccount}")
    seccount+=1
    if stopthread:
        time.sleep(1)
        strartcount(mincount,seccount,hourcount)
    else:
        sys.exit(0)
def run():
    global stopthread
    stopthread=1
    t1=threading.Thread(target=strartcount,args=(mcount,scount,hrcount)).start()
    def flush(self):
       pass
def pause():
    global stopthread
    stopthread=0
    # t1.join()
def restart():
    global mcount,scount,hrcount,stopthread
    mcount=0
    scount=0
    hrcount=0
    stopthread=1
    counterlabel.configure(text=f"{hrcount}:{mcount}:{scount}")
def alarm():
    hr=int(time.strftime("%H"))
    min=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))
    cur=(hr*3600)+(min*60)+(sec)
    dest=(int(hrentry.get())*3600)+(int(minentry.get())*60)+int(secentry.get())
    altime=dest-cur
    time.sleep(altime)
    notification.notify(
        title="Alarm Completed!!",
        message="It is a reminder do to something, time's up.",
        app_icon="E:\projects\Clocks\Iconsmind-Outline-Clock.ico",
        timeout=5
    )
def alarmthread():
    threading.Thread(target=alarm).start()
    def flush(self):
       pass
main_screen=Tk()
# w=main_screen.winfo_screenwidth()     #thses lines used to check the systems screen resolution
# h=main_screen.winfo_screenheight()
# print(w,h)
main_screen.title("DigitalClock")
main_screen.geometry("250x200+1236+20")
# main_screen.minsize("250","200")
main_screen.maxsize("250","200")
c=Canvas(main_screen)
# c.place(x=0,y=60)
image1=PhotoImage(file=r"C:\Users\Akshay Rathour\Downloads\Untitled design (19).png")
lowerbg=Label(main_screen,image=image1)
daylabel=Label(main_screen,font="ZapCfiancey 15",fg="yellow",bg="#03989e")
datelabel=Label(main_screen,font="ZapCfiancey 15",fg="yellow",bg="#03989e")
c.place(x=0,y=30)
line=c.create_line(0,10,250,10,fill="black")
times=Label(main_screen,font="ZapCfiancey 20",fg="#ADD8E6",bg="black")
startbton=Button(main_screen,borderwidth=0,text="START",command=run)
pausebton=Button(main_screen,borderwidth=0,text="PAUSE",command=pause)
restartbton=Button(main_screen,borderwidth=0,text="RESTART",command=restart)
alarmbton=Button(main_screen,borderwidth=0,text="ALARM",width=8,command=alarmthread)
counterlabel=Label(main_screen,font="ZapCfiancey 20",fg="black",bg="#03989e")
hrentry=Entry(main_screen,width=3)
minentry=Entry(main_screen,width=3)
secentry=Entry(main_screen,width=3)
times.pack(fill="both")
lowerbg.pack()
daylabel.place(x=13,y=52)
datelabel.place(x=60,y=92)
startbton.place(x=63,y=120)
pausebton.place(x=113,y=120)
restartbton.place(x=163,y=120)
alarmbton.place(x=168,y=60)
counterlabel.place(x=15,y=155)
hrentry.place(x=130,y=160)
minentry.place(x=155,y=160)
secentry.place(x=180,y=160)
timer()
main_screen.mainloop()

