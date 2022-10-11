from tkinter import*

# label-->an area widget that holds text/image within a window..
# fg-->foreground
# relief--> border around label
# bd--> border width
# padding --> padx & pady
# compound--> where we want to place the image

window=Tk()
photo=PhotoImage(file="logo.png")
label=Label(window,
            text="Welcome to Bangalore",
            font=("Arial",40,"bold"),
            fg="green",
            bg="black",
            relief=RAISED,
            bd=10,
            padx=20,
            pady=20,
            image=photo,
            compound="bottom") # image appears at the bottom
label.pack()
label.place(x=100,y=300) # where you can place text or images...


window.mainloop()

