from tkinter import *

root = Tk()
root.title("me.com")
root.geometry("600x600")

def clicker(events):
    myLabel = Label(root, text="You click a Button" + str(events.x) + ":" + str(events.y))
    # myLabel = Label(root, text="You click a Button" + events.char)
    myLabel.pack()

myButton = Button(root, text="Click this", command="clicker")
myButton.bind("<Enter>", clicker)
myButton.bind("<Leave>", clicker)
myButton.bind("<Button-1>", clicker)
myButton.pack(pady=20)

root.mainloop()