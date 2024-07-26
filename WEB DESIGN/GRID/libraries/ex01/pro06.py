import tkinter as tk 
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Exersice 06")
canvas = tk.Canvas(frame)
x1 = 250
y1 = 50
x2 = 300
y2 = 100
for i in range(5):
    canvas.create_oval(x1, y1, x2, y2, fill="red")
    y1 += 50
    y2 += 50
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
