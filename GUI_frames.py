# frame= a rectangular container to group and hold widgets

from tkinter import*


window=Tk()

frame=Frame(window,bg="pink",bd=4,relief=SUNKEN)
frame.pack(side=BOTTOM) # frame will be in bottom of the window

Button(frame,text="W",font=("Consolas",30),width=5).pack(side=TOP)
Button(frame,text="A",font=("Consolas",30),width=5).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",30),width=5).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",30),width=5).pack(side=LEFT)

window.mainloop()