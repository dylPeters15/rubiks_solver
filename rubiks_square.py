from tkinter import *

class rubiks_square():
    def __init__(self, canvas, x, y, size=10, fill="grey"):
        self.canvas = canvas
        self.fill = fill
        self.rect = canvas.create_rectangle(x, y, x+size, y+size, fill=fill)
        canvas.tag_bind(self.rect, "<Button-1>", self.rectangle_clicked)
        self.modifiable = True

    def set_modifiable(self, modifiable):
        self.modifiable = modifiable

    def rectangle_clicked(self,event):
        if (self.modifiable):
            if (self.fill == "orange"):
                self.fill = "green"
            elif (self.fill == "green"):
                self.fill = "white"
            elif (self.fill == "white"):
                self.fill = "blue"
            elif (self.fill == "blue"):
                self.fill = "red"
            elif (self.fill == "red"):
                self.fill = "yellow"
            else:
                self.fill = "orange"
            self.canvas.itemconfig(self.rect, fill=self.fill)
