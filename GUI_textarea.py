# text widget= functions like a text area, you can enter multiple lines of text...

from tkinter import*

def submit():
    input=text.get("1.0",END)   # here 1.0--> first index 
    print(input)

window=Tk()

text=Text(window,
          bg="yellow",
          font=("Arial",20),
          height=8,
          width=20,
          padx=20,
          pady=23)
text.pack()

button=Button(window,text="submit",command=submit)
button.pack()




window.mainloop()