from Tkinter import *
from ThreeByThreeModel import ThreeByThreeModel

class ThreeByThreeView():
    def __init__(self,initialModel=None):
        if initialModel == None:
            self.model = ThreeByThreeModel()
        else:
            self.model = initialModel

        self.window = None
        self.canvas = None

        self.createWindowAndCanvas()
        self.createRubiksGrid()
        self.packAndStart()

    def get_model(self):
        return self.model

    def createWindowAndCanvas(self):
        self.window = Tk()
        self.window.title("Rubik's Cube Solver")

        self.canvas = Canvas(self.window, width=300, height=300)

    def rectangleClicked(self,event):
        print("You clicked rectangle {}".format(event))

    def createRubiksGrid(self):
        id = self.canvas.create_rectangle(100, 100, 201, 201, fill="grey")
        self.canvas.tag_bind(id, "<Button-1>", self.rectangleClicked)

    def packAndStart(self):
        self.canvas.pack()
        self.window.mainloop()