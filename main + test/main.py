import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg='white', width=600, height=400, highlightcolor='blue', state='disabled')

canvas.pack()


def create_house(x, y):
    canvas.create_rectangle(x + 10, y + 30, x + 40, y + 60)
    canvas.create_polygon(x + 0, y + 30, x + 50, y + 30, x + 25, y + 10, fill='white', outline='black')

for i in range(5):
    create_house(50+i*100, 100)

root.mainloop()
