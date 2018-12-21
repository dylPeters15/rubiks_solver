#Immutable class
class ThreeByThreeModel:
    solved = "ooooooooogggwwwbbbgggwwwbbbgggwwwbbbrrrrrrrrryyyyyyyyy"

    def __init__(self, data=None, dist=0, prev=None, in_edge=None):
        if data == None:
            self.data = ThreeByThreeModel.solved
        else:
            self.data = data

        self.distance_from_solved = 0
        for i in range(len(self.data)):
            if self.data[i] != ThreeByThreeModel.solved[i]:
                self.distance_from_solved += 1

        self.dist = dist
        self.prev = prev
        self.in_edge = in_edge

    def get_dist(self):
        return self.dist

    def set_dist(self, new_dist):
        self.dist = new_dist

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def is_solved(self):
        return self.data == ThreeByThreeModel.solved

    def get_neighbors(self):
        return [
            self._left_up(),
            self._left_two(),
            self._left_down(),

            self._right_up(),
            self._right_two(),
            self._right_down(),

            self._top_right(),
            self._top_two(),
            self._top_left(),

            self._bottom_right(),
            self._bottom_two(),
            self._bottom_left(),

            self._front_clockwise(),
            self._front_two(),
            self._front_counter_clockwise(),

            self._back_clockwise(),
            self._back_two(),
            self._back_counter_clockwise()
        ]

######################################################################

    def _left_up(self):
        after_move = list(self.data)
        after_move[0] = self.data[12]
        after_move[3] = self.data[21]
        after_move[6] = self.data[30]
        after_move[12] = self.data[36]
        after_move[21] = self.data[39]
        after_move[30] = self.data[42]
        after_move[36] = self.data[45]
        after_move[39] = self.data[48]
        after_move[42] = self.data[51]
        after_move[45] = self.data[0]
        after_move[48] = self.data[3]
        after_move[51] = self.data[6]
        after_move = "".join(after_move)
        return after_move

    def _left_two(self):
        left_up_1 = ThreeByThreeModel(data=self._left_up())
        return left_up_1._left_up()

    def _left_down(self):
        left_two = ThreeByThreeModel(data=self._left_two())
        return left_two._left_up()

######################################################################

    def _right_up(self):
        after_move = list(self.data)
        # after_move[0] = self.data[12]
        # after_move[3] = self.data[21]
        # after_move[6] = self.data[30]
        # after_move[12] = self.data[36]
        # after_move[21] = self.data[39]
        # after_move[30] = self.data[42]
        # after_move[36] = self.data[45]
        # after_move[39] = self.data[48]
        # after_move[42] = self.data[51]
        # after_move[45] = self.data[0]
        # after_move[48] = self.data[3]
        # after_move[51] = self.data[6]
        after_move = "".join(after_move)
        return after_move

    def _right_two(self):
        right_up_1 = ThreeByThreeModel(data=self._right_up())
        return right_up_1._right_up()

    def _right_down(self):
        right_two = ThreeByThreeModel(data=self._right_two())
        return right_two._right_up()

######################################################################

    def _top_right(self):
        after_move = list(self.data)
        # after_move[0] = self.data[12]
        # after_move[3] = self.data[21]
        # after_move[6] = self.data[30]
        # after_move[12] = self.data[36]
        # after_move[21] = self.data[39]
        # after_move[30] = self.data[42]
        # after_move[36] = self.data[45]
        # after_move[39] = self.data[48]
        # after_move[42] = self.data[51]
        # after_move[45] = self.data[0]
        # after_move[48] = self.data[3]
        # after_move[51] = self.data[6]
        after_move = "".join(after_move)
        return after_move

    def _top_two(self):
        top_right_1 = ThreeByThreeModel(data=self._top_right())
        return top_right_1._top_right()

    def _top_left(self):
        top_two = ThreeByThreeModel(data=self._top_two())
        return top_two._top_right()

######################################################################

    def _bottom_right(self):
        after_move = list(self.data)
        # after_move[0] = self.data[12]
        # after_move[3] = self.data[21]
        # after_move[6] = self.data[30]
        # after_move[12] = self.data[36]
        # after_move[21] = self.data[39]
        # after_move[30] = self.data[42]
        # after_move[36] = self.data[45]
        # after_move[39] = self.data[48]
        # after_move[42] = self.data[51]
        # after_move[45] = self.data[0]
        # after_move[48] = self.data[3]
        # after_move[51] = self.data[6]
        after_move = "".join(after_move)
        return after_move

    def _bottom_two(self):
        bottom_right_1 = ThreeByThreeModel(data=self._bottom_right())
        return bottom_right_1._bottom_right()

    def _bottom_left(self):
        bottom_two = ThreeByThreeModel(data=self._bottom_two())
        return bottom_two._bottom_right()

######################################################################

    def _front_clockwise(self):
        after_move = list(self.data)
        # after_move[0] = self.data[12]
        # after_move[3] = self.data[21]
        # after_move[6] = self.data[30]
        # after_move[12] = self.data[36]
        # after_move[21] = self.data[39]
        # after_move[30] = self.data[42]
        # after_move[36] = self.data[45]
        # after_move[39] = self.data[48]
        # after_move[42] = self.data[51]
        # after_move[45] = self.data[0]
        # after_move[48] = self.data[3]
        # after_move[51] = self.data[6]
        after_move = "".join(after_move)
        return after_move

    def _front_two(self):
        front_clockwise_1 = ThreeByThreeModel(data=self._front_clockwise())
        return front_clockwise_1._front_clockwise()

    def _front_counter_clockwise(self):
        front_two = ThreeByThreeModel(data=self._front_two())
        return front_two._front_clockwise()

######################################################################

    def _back_clockwise(self):
        after_move = list(self.data)
        # after_move[0] = self.data[12]
        # after_move[3] = self.data[21]
        # after_move[6] = self.data[30]
        # after_move[12] = self.data[36]
        # after_move[21] = self.data[39]
        # after_move[30] = self.data[42]
        # after_move[36] = self.data[45]
        # after_move[39] = self.data[48]
        # after_move[42] = self.data[51]
        # after_move[45] = self.data[0]
        # after_move[48] = self.data[3]
        # after_move[51] = self.data[6]
        after_move = "".join(after_move)
        return after_move

    def _back_two(self):
        back_clockwise_1 = ThreeByThreeModel(data=self._back_clockwise())
        return back_clockwise_1._back_clockwise()

    def _back_counter_clockwise(self):
        back_two = ThreeByThreeModel(data=self._back_two())
        return back_two._back_clockwise()