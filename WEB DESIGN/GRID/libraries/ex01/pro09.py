import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Exercise 09")
canvas = tk.Canvas(frame)
x1 = y1 = 50
x2 = y2 = 100
rani = random.randint(0,9)
for i in range(10):
    if rani == i:
        canvas.create_oval(x1, y1, x2, y2, fill="red")
    else:
        canvas.create_oval(x1, y1, x2, y2, fill="blue")
    x1 += 50
    x2 += 50
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()