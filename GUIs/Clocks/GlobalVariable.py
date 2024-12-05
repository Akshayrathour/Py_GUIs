#this piece of code explains how you can change a global variable from a function in python 
a=1
def run():
    if a:
        print("hi")

def pause():
    global a
    a=0

run()
run()
pause()
run()