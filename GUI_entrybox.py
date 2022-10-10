from tkinter import*

# entry widget= textbox that accepts a single line of user input

def submit():
    username=entry.get() # return a string
    print("Hello "+username)
    
def delete():
    entry.delete(0,END) # delete all the characters within entry box
    
def backspace():
    entry.delete(len(entry.get())-1,END) # delete characters one by one (last)
    

window=Tk()

entry=Entry(window,
            font=("Arial",50),
            fg="green",
            bg="black",
            show="*") # characters showed in * mark

entry.pack(side=LEFT)

submit_button=Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button=Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button=Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()