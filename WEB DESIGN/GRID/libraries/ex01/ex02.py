import tkinter as tk

# Vreat an empty window
root = tk.Tk()
# Set TK window size to with 600 pz and height 200 px
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("Hello pnc")
canvas = tk.Canvas(frame)
canvas.create_oval(25, 50, 125, 100, fill = "#fff")
canvas.create_oval(50, 50, 100, 100, fill = "blue")
canvas.create_oval(475, 50, 575, 100, fill = "#fff") 
canvas.create_oval(500, 50, 550, 100, fill = "blue") 
canvas.create_oval(275, 275, 325, 325, fill = "red") 
canvas.create_rectangle(50, 450, 550, 500, fill = "red") 
canvas.create_rectangle(50, 350, 100, 500, fill = "red") 
canvas.create_rectangle(475, 400, 550, 500, fill = "red") 

 
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
# Disply all
root.mainloop()