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
        #TODO
        return

    def set_dist(self):
        #TODO
        return

    def set_prev(self):
        #TODO
        return