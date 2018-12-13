from Tkinter import *
from ThreeByThreeModel import ThreeByThreeModel

window = None
canvas = None

def createWindowAndCanvas():
    global window
    global canvas

    window = Tk()
    window.title("Rubik's Cube Solver")

    canvas = Canvas(window, width=300, height=300)

def createRubiksGrid():
    id = canvas.create_rectangle(100, 100, 201, 201, fill="grey", tags="asdf")
    canvas.tag_bind("asdf","<Button-1>",rectangleClicked)

def packAndStart():
    canvas.pack()
    window.mainloop()


def rectangleClicked(*args):
    print("You clicked rectangle {}".format(args))


createWindowAndCanvas()
createRubiksGrid()
packAndStart()

model = ThreeByThreeModel()
print model.string_value()