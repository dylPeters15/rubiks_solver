from tkinter import *
from rubiks_square import rubiks_square
from a_star import a_star
from ThreeByThreeModel import ThreeByThreeModel


class ThreeByThreeView:
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

        middle_squares = [4, 19, 22, 25, 40, 49]
        for square_index in middle_squares:
            self.rubiks_squares[square_index].set_modifiable(False)

        Button(self.window,
                  text="Solve", command=self.solve).place(x=0, y=0)

    def packAndStart(self):
        self.canvas.pack()
        self.window.mainloop()

    def solve(self):
        data = ""
        for square in self.rubiks_squares:
            data += square.fill[0]
        print("Starting search")
        path = a_star(ThreeByThreeModel(data=data))
        print(path)
        for state in path:
            print(state.in_edge)
        print("Finished search")

if __name__ == "__main__":
    ThreeByThreeView()