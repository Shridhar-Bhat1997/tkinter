from tkinter import*

# widgets--> GUI elements buttons,textboxes,labels,images..
# windows--> serves as a container to hold or contain these widgets...

window=Tk() # instantiate an instance of a window..
window.geometry("300x400") # width&height
window.title("First GUI Program") # to change title of the window

# to change icon
# tkinter.PhotoImage only support GM, PPM, GIF, PNG image.
icon=PhotoImage(file='logo.png')
window.iconphoto(False,icon)

window.config(background="blue")

window.mainloop() # place window on computer screen.