import tkinter as tk
win = tk.Tk()

def mover():
    canvas.move(o1,5,0)
    canvas.after(10,mover)

def drticka(e):
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in zozob:
        canvas.move(o1,5,5)
        if canvas.itemcget(o1,"fill")=="red":
            canvas.itemconfig(o1,fill="turquoise")
        else:
            canvas.itemconfig(o1,fill="red")

def destilator(e):
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in zozob:
        canvas.move(o1,-5,-5)
        if canvas.itemcget(o1,"fill")=="red":
            canvas.itemconfig(o1,fill="turquoise")
        else:
            canvas.itemconfig(o1,fill="red")

canvas = tk.Canvas(win,width=500,height=500, bg="white")
o1= canvas.create_rectangle(50,50,250,250,fill="turquoise")
k1 = canvas.create_oval(250,250,500,500,fill="magenta")

canvas.bind("<Button-1>",drticka)
canvas.bind("<Button-3>",destilator)

print(o1)
canvas.pack()
mover()
win.mainloop()
