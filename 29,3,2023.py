import tkinter as tk
win = tk.Tk()

def drticka(e):
    print("vykonala som sa ")
    print(e.x,e.y)
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in zozob:
        canvas.

canvas = tk.Canvas(win,width=500,height=500, bg="white")
o1= canvas.create_rectangle(50,50,250,250,fill="turquoise")
k1 = canvas.create_oval(250,250,500,500,fill="magenta")
canvas.bind("<Button-1>",drticka)

print(o1)
canvas.pack()
win.mainloop()
