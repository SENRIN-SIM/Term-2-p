from tkinter import *

root = Tk()
root.title("codemy.com - learn To Code!")
root.iconbitmap()
root.geometry("600x600")

def clicker(events):
    myLabel = Label(root, text="You clicked a button")
    myLabel.pack()

myButton = Button(root, text="Click Me", command=clicker)
myButton.bind("<Button-3>", clicker)
myButton.pack(pady=20)

root.mainloop()





