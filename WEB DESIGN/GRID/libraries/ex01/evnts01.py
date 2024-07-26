# import tkinter as tk

# import random
# def myEventTrigger_win(event):
#     print("You win! :", event.x, event.y)
#     canvas.create_text(300,400,text="YOU WIN!",font=("Purisa",26))
# def myEventTrigger_lost(event):
#     print("You win! :", event.x, event.y)
#     canvas.create_text(300,400,text="YOU LOST",font=("Purisa",26))
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("Ex2")
# canvas = tk.Canvas(frame)
# x1 = y1 = 50
# x2 = y2 = 100
# rani = random.randint(0,9)
# for i in range(10):
#     if rani == i:
#         canvas.create_oval(x1, y1, x2, y2, fill="blue",tags="wintaget")
#     else:
#         canvas.create_oval(x1, y1, x2, y2, fill="blue", tags="lost")
#     x1 += 50
#     x2 += 50
# canvas.tag_bind("wintaget", "<Button-1>", myEventTrigger_win)
# canvas.tag_bind("lost", "<Button-1>", myEventTrigger_lost)
# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
# root.mainloop()



# import tkinter as tk
# import random
# def myEventTrigger(event):
#     print("You win! :", event.x, event.y)
#     canvas.create_text(300,400,text="YOU WIN!",font=("Purisa",26))

# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("Ex1")
# canvas = tk.Canvas(frame)
# x1 = 50
# x2 = 100
# y1 = 275
# y2 = 325
# random_index = random.randint(0, 8)
# for i in range(9):
#     if i == random_index:
#         canvas.create_oval(x1, y1, x2, y2, fill="#0000FF",tags="Wintaget")
#     else:
#         canvas.create_oval(x1, y1, x2, y2, fill="#0000FF")
#     x1 += 60
#     x2 += 60

# canvas.tag_bind("Wintaget", "<Button-1>", myEventTrigger)
# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
# root.mainloop()

