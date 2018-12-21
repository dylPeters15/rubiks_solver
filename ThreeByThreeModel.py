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

    def set_prev(self, prev, in_edge):
        self.prev = prev
        self.in_edge = in_edge

    # def get_cost(self):
    #     return self.get_path_length() + self.distance_from_solved

    def __hash__(self):
        return self.data.__hash__()
        #TODOreturn self.data
#Need to define hash function so that the priority queue will only hold one instance of each model object

    def __cmp__(self, other):
        return self.dist - other.dist
        #TODO
#Need to