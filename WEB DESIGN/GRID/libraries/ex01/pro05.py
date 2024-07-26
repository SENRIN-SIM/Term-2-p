import tkinter as tk
import random
# Vreat an empty window
root = tk.Tk()
# Set TK window size to with 600 pz and height 200 px
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Exerice 01")
canvas = tk.Canvas(frame)
x1 = y1 = 0
x2 = y2 = 60

for i in range(10):
    for i in range(10):
        colors = ["red", "blue", "green", "yellow", "green"]
        canvas.create_rectangle(x1, y1, x2, y2, fill=colors[random.randrange(1,len(colors))])
        y1 += 60
        y2 += y1 +60
    x1 += 60
    x2 += x1 + 60
    y1 = 0
    y2 += y1 + 60

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
# Disply all
root.mainloop()

# import tkinter as tk
# import random

# root = tk.Tk()
# root.geometry("600x600")
# root.title("Exercise 3")

# frame = tk.Frame(root)
# frame.pack(expand=True, fill="both")

# canvas = tk.Canvas(frame)
# canvas.pack(expand=True, fill="both")

# x1 = 10
# x2 = 65
# colors = ["red", "blue", "green", "yellow", "green", "black", "purple"]
# for i in range(50):
#     row = i // 10  # Calculate the row index
#     col = i % 10  # Calculate the column index
#     rect_x1 = x1 + col * 60  # Adjust the x-coordinate based on the column
#     rect_y1 = x1 + row * 60  # Adjust the y-coordinate based on the row
#     rect_x2 = x2 + col * 60  # Adjust the x-coordinate based on the column
#     rect_y2 = x2 + row * 60  # Adjust the y-coordinate based on the row
#     canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=random.choice(colors))

# root.mainloop()