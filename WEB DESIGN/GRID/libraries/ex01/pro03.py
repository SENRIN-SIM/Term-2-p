import tkinter as tk

# Vreat an empty window
root = tk.Tk()
# Set TK window size to with 600 pz and height 200 px
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Exerice 01")
canvas = tk.Canvas(frame)
x1 = 100
x2 = 500
colors = ["red", "blue", "green", "yellow", "green"]
for i in range(5):
    canvas.create_rectangle(x1, x1, x2, x2, fill=colors[i])
    x1 +=43
    x2 -=43
 
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
# Disply all
root.mainloop()