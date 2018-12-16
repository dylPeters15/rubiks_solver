class ThreeByThreeModel:
    solved = "ooooooooogggwwwbbbgggwwwbbbgggwwwbbbrrrrrrrrryyyyyyyyy"

    def __init__(self, initial_config=None):
        if initial_config == None:
            self.data = ThreeByThreeModel.solved
        else:
            self.data = initial_config

        self.distance_from_solved = 0
        for i in range(len(self.data)):
            if self.data[i] != ThreeByThreeModel.solved[i]:
                self.distance_from_solved += 1

    def get_all_next_moves(self):
        #TODO
        return

    #simplified instruction set:

    def _left_down(self):
        #TODO
        return

    def _right_down(self):
        #TODO
        return

    def _top_right(self):
        #TODO
        return

    def _bottom_right(self):
        #TODO
        return

    def _front_clockwise(self):
        #TODO
        return

    def _back_clockwise(self):
        #TODO
        return