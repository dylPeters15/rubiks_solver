from Tkinter import *
from ThreeByThreeModel import ThreeByThreeModel
from rubiks_square import rubiks_square

class ThreeByThreeView():
    def __init__(self):

        self.square_size = 25
        self.padding = 5

        self.rubiks_squares = []

        self.window = None
        self.canvas = None

        self.createWindowAndCanvas()
        self.createRubiksGrid()
        self.packAndStart()

    def createWindowAndCanvas(self):
        self.window = Tk()
        self.window.title("Rubik's Cube Solver")

        self.canvas = Canvas(self.window, width=self.square_size*9+self.padding*14, height=self.square_size*12+self.padding*18)

    def createRubiksGrid(self):

        for r in range(3):
            for c in range(3):
                x = (self.padding*3) + (self.square_size+self.padding)*3 + (self.square_size+self.padding)*c
                y = (self.padding*2) + (self.square_size+self.padding)*r
                fill = "orange"
                self.rubiks_squares.append(rubiks_square(canvas=self.canvas, x=x, y=y, size=self.square_size, fill=fill))
                #print "(x,y): ({}, {})".format(x,y)

        #print

        for r in range(3):
            for c in range(9):
                x = (self.padding*2) + (self.square_size+self.padding)*c
                y = (self.padding*3) + (self.square_size+self.padding)*3 + (self.square_size+self.padding)*r
                if c < 3:
                    fill = "green"
                elif c >= 3 and c < 6:
                    fill = "white"
                    x += self.padding
                else:
                    fill = "blue"
                    x += self.padding*2
                self.rubiks_squares.append(rubiks_square(canvas=self.canvas, x=x, y=y, size=self.square_size, fill=fill))
                #print "(x,y): ({}, {})".format(x,y)

        #print

        for r in range(3):
            for c in range(3):
                x = (self.padding*3) + (self.square_size+self.padding)*3 + (self.square_size+self.padding)*c
                y = (self.padding*4) + (self.square_size+self.padding)*6 + (self.square_size+self.padding)*r
                fill = "red"
                self.rubiks_squares.append(rubiks_square(canvas=self.canvas, x=x, y=y, size=self.square_size, fill=fill))
                #print "(x,y): ({}, {})".format(x,y)

        #print

        for r in range(3):
            for c in range(3):
                x = (self.padding*3) + (self.square_size+self.padding)*3 + (self.square_size+self.padding)*c
                y = (self.padding*5) + (self.square_size+self.padding)*9 + (self.square_size+self.padding)*r
                fill = "yellow"
                self.rubiks_squares.append(rubiks_square(canvas=self.canvas, x=x, y=y, size=self.square_size, fill=fill))
                #print "(x,y): ({}, {})".format(x,y)

    def packAndStart(self):
        self.canvas.pack()
        self.window.mainloop()