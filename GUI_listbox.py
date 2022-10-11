# listbox= a listing of selectable text items within its own container..

from tkinter import *

def submit():
    print("You have ordered: ")
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
    
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())
    

window=Tk()

listbox=Listbox(window,
                bg="violet",
                font=("Arial",40),
                width=20)
listbox.pack()

listbox.insert(1,"grapes")
listbox.insert(2,"mango")
listbox.insert(3,"apple")
listbox.insert(4,"papaya")
listbox.insert(5,"guava")

listbox.config(height=listbox.size())

entryBox=Entry(window)
entryBox.pack()

submitButton=Button(window,text="submit",command=submit)
submitButton.pack()

addButton=Button(window,text="add",command=add)
addButton.pack()

deleteButton=Button(window,text="delete",command=delete)
deleteButton.pack()




window.mainloop()