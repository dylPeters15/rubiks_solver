class ThreeByThreeModel:

    def __init__(self, initial_config=None):
        white = "white"
        red = "red"
        blue = "blue"
        orange = "orange"
        green = "green"
        yellow = "yellow"
        if initial_config == None:
            self.squares = [
                [[white, white, white], [white, white, white], [white, white, white]],
                [[red, red, red], [red, red, red], [red, red, red]],
                [[blue, blue, blue], [blue, blue, blue], [blue, blue, blue]],
                [[orange, orange, orange], [orange, orange, orange], [orange, orange, orange]],
                [[green, green, green], [green, green, green], [green, green, green]],
                [[yellow, yellow, yellow], [yellow, yellow, yellow], [yellow, yellow, yellow]]
            ]
        else:
            squares = initial_config

    #simplified instruction set:

    def left_down(self):
        #TODO
        return

    def right_down(self):
        #TODO
        return

    def top_right(self):
        #TODO
        return

    def bottom_right(self):
        #TODO
        return

    def front_clockwise(self):
        #TODO
        return

    def back_clockwise(self):
        #TODO
        return

    def distance_from_solved(self):
        return

    def value(self):
        value = []
        for face in self.squares:
            for row in face:
                for square in row:
                    value.append(square)
        return value

    def string_value(self):
        value = ""
        for face in self.squares:
            for row in face:
                for square in row:
                    value += square
        return value