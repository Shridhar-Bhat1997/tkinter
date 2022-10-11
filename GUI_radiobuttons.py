# radio button=similar to checkbox, but you can only select one from a group...

from tkinter import*

food=["pizza","burger","bel"]

def order():
    if(x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("you ordered burger")
    elif(x.get()==2):
        print("you ordered bel")
    else:
        print("done")

window=Tk()

pizzaImage=PhotoImage(file="pizza.png")
burgerImage=PhotoImage(file="burger.png")
belImage=PhotoImage(file="bel.png")

foodImages=[pizzaImage,burgerImage,belImage]

x=IntVar()

for index in range(len(food)):
    radiobutton=Radiobutton(window,
                            text=food[index], # adds text to radio button
                            variable=x, # groups radio button together if they share same variable
                            value=index, # assigns each radio button a different value
                            padx=23,
                            font=("Impact",40),
                            image=foodImages[index], # adds image to radiobutton
                            compound="left",  # adds image & text left side
                            indicatoron=0, # eliminate circle indicators
                            width=350, # sets width of radiobuttons
                            command=order) # set command of radiobutton to a function
    radiobutton.pack(anchor=W)


window.mainloop()