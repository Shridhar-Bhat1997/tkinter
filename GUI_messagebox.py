from tkinter import*
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="This is an info message box",message="You are a person")
    #messagebox.showwarning(title="WARNING!!!",message="You have a virus!!")
    #messagebox.showerror(title="ERROR!!",message="something went wrong!!")
    
    if messagebox.askokcancel(title="ask ok cancel",message="Do you want to continue"): # same as askretrycancel/askyesno/askquestion
        print("You did a thing")
    else:
        print("You cancelled a thing")

window=Tk()

button=Button(window,command=click,text="click me!")
button.pack()

window.mainloop()