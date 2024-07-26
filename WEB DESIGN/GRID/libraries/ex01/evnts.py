import tkinter as tk
def myEventTrigger(event):
    print("User click oval :", event.x, event.y)
def myEventTrigge(event):
    print("User click ractangle :", event.x, event.y)
def myEventTrigg(event):
    print("User click square :", event.x, event.y)
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Ex1")
canvas = tk.Canvas(frame)

canvas = tk.Canvas(frame)
canvas.create_oval(50, 50, 300,300, fill="red", tags="PNCTarget")
canvas.create_rectangle(350, 50, 500,300, fill="red", tags="PNCTarge")
canvas.create_rectangle(50, 350, 500,450, fill="red", tags="PNCTarg")
canvas.tag_bind("PNCTarget", "<Button-1>", myEventTrigger)
canvas.tag_bind("PNCTarge", "<Button-1>", myEventTrigge)
canvas.tag_bind("PNCTarg", "<Button-1>", myEventTrigg)
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()


