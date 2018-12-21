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

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "ThreeByThreeModel: data={}, dist+dist_from_solved: {}, dist={}, in_edge={}".format(self.data, self.dist+self.distance_from_solved, self.dist, self.in_edge)

    #Methods used for sorting:
    def __lt__(self, other):
        return self.dist + self.distance_from_solved < other.dist + other.distance_from_solved

    def __le__(self, other):
        return self.dist + self.distance_from_solved <= other.dist + other.distance_from_solved

    def __eq__(self, other):
        return self.data == other.data
        # return self.dist + self.distance_from_solved == other.dist + other.distance_from_solved

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.dist + self.distance_from_solved > other.dist + other.distance_from_solved

    def __ge__(self, other):
        return self.dist + self.distance_from_solved >= other.dist + other.distance_from_solved

    def __hash__(self):
        return self.data.__hash__()

    def get_a_star_weight(self):
        return self.dist + self.distance_from_solved

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
            self._back_counter_clockwise(),

            self._middle_right_1(),
            self._middle_right_2(),
            self._middle_left_1(),

            self._middle_up_1(),
            self._middle_up_2(),
            self._middle_down_1(),

            self._middle_clockwise_1(),
            self._middle_clockwise_2(),
            self._middle_counterclockwise_1()
        ]

    def get_neighbors_data_only(self):
        return [neighbor.data for neighbor in self.get_neighbors()]

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
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Left Up")

    def _left_two(self):
        left_up_1 = self._left_up()
        left_two = left_up_1._left_up()
        return ThreeByThreeModel(data=left_two.data, dist=self.dist+1, prev=self, in_edge="Left 2")

    def _left_down(self):
        left_two = self._left_two()
        left_down = left_two._left_up()
        return ThreeByThreeModel(data=left_down.data, dist=self.dist+1, prev=self, in_edge="Left Down")

######################################################################

    def _right_up(self):
        after_move = list(self.data)
        after_move[2] = self.data[14]
        after_move[5] = self.data[23]
        after_move[8] = self.data[32]
        after_move[14] = self.data[38]
        after_move[23] = self.data[41]
        after_move[32] = self.data[44]
        after_move[38] = self.data[47]
        after_move[41] = self.data[50]
        after_move[44] = self.data[53]
        after_move[47] = self.data[2]
        after_move[50] = self.data[5]
        after_move[53] = self.data[8]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Right Up")

    def _right_two(self):
        right_up_1 = self._right_up()
        right_2 = right_up_1._right_up()
        return ThreeByThreeModel(data=right_2.data, dist=self.dist+1, prev=self, in_edge="Right 2")

    def _right_down(self):
        right_two = self._right_two()
        right_down = right_two._right_up()
        return ThreeByThreeModel(data=right_down.data, dist=self.dist+1, prev=self, in_edge="Right Down")

######################################################################

    def _top_right(self):
        after_move = list(self.data)
        after_move[9] = self.data[53]
        after_move[10] = self.data[52]
        after_move[11] = self.data[51]
        after_move[12] = self.data[9]
        after_move[13] = self.data[10]
        after_move[14] = self.data[11]
        after_move[15] = self.data[12]
        after_move[16] = self.data[13]
        after_move[17] = self.data[14]
        after_move[53] = self.data[15]
        after_move[52] = self.data[16]
        after_move[51] = self.data[17]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Top Right")

    def _top_two(self):
        top_right_1 = self._top_right()
        top_2 = top_right_1._top_right()
        return ThreeByThreeModel(data=top_2.data, dist=self.dist+1, prev=self, in_edge="Top 2")

    def _top_left(self):
        top_two = self._top_two()
        top_left = top_two._top_right()
        return ThreeByThreeModel(data=top_left.data, dist=self.dist+1, prev=self, in_edge="Top Left")

######################################################################

    def _bottom_right(self):
        after_move = list(self.data)
        after_move[27] = self.data[47]
        after_move[28] = self.data[46]
        after_move[29] = self.data[45]
        after_move[30] = self.data[27]
        after_move[31] = self.data[28]
        after_move[32] = self.data[29]
        after_move[33] = self.data[30]
        after_move[34] = self.data[31]
        after_move[35] = self.data[32]
        after_move[47] = self.data[33]
        after_move[46] = self.data[34]
        after_move[45] = self.data[35]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Bottom Right")

    def _bottom_two(self):
        bottom_right_1 = self._bottom_right()
        bottom_2 = bottom_right_1._bottom_right()
        return ThreeByThreeModel(data=bottom_2.data, dist=self.dist+1, prev=self, in_edge="Bottom 2")

    def _bottom_left(self):
        bottom_two = self._bottom_two()
        bottom_left = bottom_two._bottom_right()
        return ThreeByThreeModel(data=bottom_left.data, dist=self.dist+1, prev=self, in_edge="Bottom Left")

######################################################################

    def _front_clockwise(self):
        after_move = list(self.data)
        after_move[6] = self.data[29]
        after_move[7] = self.data[20]
        after_move[8] = self.data[11]
        after_move[15] = self.data[6]
        after_move[24] = self.data[7]
        after_move[33] = self.data[8]
        after_move[38] = self.data[15]
        after_move[37] = self.data[24]
        after_move[36] = self.data[33]
        after_move[29] = self.data[38]
        after_move[20] = self.data[37]
        after_move[11] = self.data[36]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Front Clockwise")

    def _front_two(self):
        front_clockwise_1 = self._front_clockwise()
        front_2 = front_clockwise_1._front_clockwise()
        return ThreeByThreeModel(data=front_2.data, dist=self.dist+1, prev=self, in_edge="Front 2")

    def _front_counter_clockwise(self):
        front_two = self._front_two()
        front_cc = front_two._front_clockwise()
        return ThreeByThreeModel(data=front_cc.data, dist=self.dist+1, prev=self, in_edge="Front Counterclockwise")

######################################################################

    def _back_clockwise(self):
        after_move = list(self.data)
        after_move[0] = self.data[17]
        after_move[1] = self.data[26]
        after_move[2] = self.data[35]
        after_move[17] = self.data[44]
        after_move[26] = self.data[43]
        after_move[35] = self.data[42]
        after_move[44] = self.data[27]
        after_move[43] = self.data[18]
        after_move[42] = self.data[9]
        after_move[27] = self.data[0]
        after_move[18] = self.data[1]
        after_move[9] = self.data[2]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Back Clockwise")

    def _back_two(self):
        back_clockwise_1 = self._back_clockwise()
        back_2 = back_clockwise_1._back_clockwise()
        return ThreeByThreeModel(data=back_2.data, dist=self.dist+1, prev=self, in_edge="Back 2")

    def _back_counter_clockwise(self):
        back_two = self._back_two()
        back_cc = back_two._back_clockwise()
        return ThreeByThreeModel(data=back_cc.data, dist=self.dist+1, prev=self, in_edge="Back Counterclockwise")

######################################################################

    def _middle_right_1(self):
        after_move = list(self.data)
        after_move[18] = self.data[50]
        after_move[19] = self.data[49]
        after_move[20] = self.data[48]
        after_move[21] = self.data[18]
        after_move[22] = self.data[19]
        after_move[23] = self.data[20]
        after_move[24] = self.data[21]
        after_move[25] = self.data[22]
        after_move[26] = self.data[23]
        after_move[50] = self.data[24]
        after_move[49] = self.data[25]
        after_move[48] = self.data[26]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Middle Right")

    def _middle_right_2(self):
        middle_right_1 = self._middle_right_1()
        middle_2 = middle_right_1._middle_right_1()
        return ThreeByThreeModel(data=middle_2.data, dist=self.dist+1, prev=self, in_edge="Middle Right 2")

    def _middle_left_1(self):
        middle_right_2 = self._middle_right_2()
        middle_left = middle_right_2._middle_right_1()
        return ThreeByThreeModel(data=middle_left.data, dist=self.dist+1, prev=self, in_edge="Middle Left")

######################################################################

    def _middle_up_1(self):
        after_move = list(self.data)
        after_move[1] = self.data[13]
        after_move[4] = self.data[22]
        after_move[7] = self.data[31]
        after_move[13] = self.data[37]
        after_move[22] = self.data[40]
        after_move[31] = self.data[43]
        after_move[37] = self.data[46]
        after_move[40] = self.data[49]
        after_move[43] = self.data[52]
        after_move[46] = self.data[1]
        after_move[49] = self.data[4]
        after_move[52] = self.data[7]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Middle Up")

    def _middle_up_2(self):
        middle_up_1 = self._middle_up_1()
        middle_2 = middle_up_1._middle_up_1()
        return ThreeByThreeModel(data=middle_2.data, dist=self.dist+1, prev=self, in_edge="Middle Up 2")

    def _middle_down_1(self):
        middle_up_2 = self._middle_up_2()
        middle_down = middle_up_2._middle_up_1()
        return ThreeByThreeModel(data=middle_down.data, dist=self.dist+1, prev=self, in_edge="Middle Down")

######################################################################

    def _middle_clockwise_1(self):
        after_move = list(self.data)
        after_move[3] = self.data[28]
        after_move[4] = self.data[19]
        after_move[5] = self.data[10]
        after_move[16] = self.data[3]
        after_move[25] = self.data[4]
        after_move[34] = self.data[5]
        after_move[41] = self.data[16]
        after_move[40] = self.data[25]
        after_move[39] = self.data[34]
        after_move[28] = self.data[41]
        after_move[19] = self.data[40]
        after_move[10] = self.data[39]
        after_move = "".join(after_move)
        return ThreeByThreeModel(data=after_move, dist=self.dist+1, prev=self, in_edge="Middle Clockwise")

    def _middle_clockwise_2(self):
        middle_clockwise_1 = self._middle_clockwise_1()
        middle_2 = middle_clockwise_1._middle_clockwise_1()
        return ThreeByThreeModel(data=middle_2.data, dist=self.dist+1, prev=self, in_edge="Middle Clockwise 2")

    def _middle_counterclockwise_1(self):
        middle_clockwise_2 = self._middle_clockwise_2()
        middle_cc = middle_clockwise_2._middle_clockwise_1()
        return ThreeByThreeModel(data=middle_cc.data, dist=self.dist+1, prev=self, in_edge="Middle Counterclockwise")