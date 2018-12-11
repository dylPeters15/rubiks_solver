from Tkinter import *
from ttk import *

window = Tk()

canvas = Canvas(window, width=300, height=300)

window.title("Rubik's Cube Solver")

# window.geometry('350x200')

# combo = Combobox(window)
#
# combo['values'] = ("white", "red", "blue", "orange", "green", "yellow")
#
# combo.current(1)  # set the selected item
#
# combo.grid(column=1, row=1)

def clicked(*args):
    print("You clicked play!")

id = canvas.create_rectangle(100, 100, 201, 201, fill="blue", tags="asdf")
canvas.tag_bind("asdf","<Button-1>",clicked)

canvas.pack()
window.mainloop()