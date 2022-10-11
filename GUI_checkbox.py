from tkinter import*

def display():
    if(x.get()==1):
        print("you agree!")
    else:
        print("you doesn't agree!")
    

window=Tk()

x=IntVar()

python_photo=PhotoImage(file="logo.png")

check_button=Checkbutton(window,
                         text="I agree to something",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         font=("Arial",20),
                         fg="blue",
                         bg="black",
                         activeforeground="blue", # to avoid flash
                         activebackground="black",
                         padx=25,
                         pady=10,
                         image=python_photo,
                         compound="left")

check_button.pack()


window.mainloop()