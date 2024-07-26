import tkinter as tk 
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Exersice 06")
canvas = tk.Canvas(frame)
x1 = 175
y1 = 275
x2 = 225
y2 = 325
for i in range(5):
    canvas.create_oval(x1, y1, x2, y2, fill="red")
    x1 += 50
    x2 += 50
    y1 -= 60
    y2 -= 60
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()