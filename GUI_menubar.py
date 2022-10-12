from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")
    
# creating tkinter window
root = Tk()
root.title('Menu Demonstration')

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0) #Tearoff property makes the menus in the window as tearable
menubar.add_cascade(label ="File",menu=file)

file.add_command(label="Open",command=openFile)
file.add_command(label="Save",command=saveFile)
file.add_separator() # creates separate section
file.add_command(label ="Exit", command =quit)

# Adding Edit Menu and commands
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut",command=None)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_command(label="Select All",command=None)
edit.add_separator()
edit.add_command(label="Find",command=None)
edit.add_command(label="Find again",command=None)

# Adding Help Menu
help_=Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Help",menu= help_)
help_.add_command(label="Tk Help",command= None)
help_.add_command(label="Demo",command= None)
help_.add_separator()
help_.add_command(label="About Tk",command=None)

# display Menu
root.config(menu=menubar)
mainloop()


