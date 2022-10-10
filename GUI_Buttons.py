# button --> you click it, then it does stuff

from tkinter import*

count=0

def click():
    global count
    count+=1
    print(count)

window=Tk()

photo=PhotoImage(file="logo.png")

button=Button(window,
              text="Click me!",
              command=click,
              font=("Comic Sans",30),
              fg="green",
              bg="black",
              activeforeground="green",  # to avoid flash
              activebackground="black",
              state="active",
              image=photo,
              compound="left") # to avoid somebody clicking a button (disabled)
button.pack()



window.mainloop()