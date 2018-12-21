from queue import PriorityQueue


class AStarPQ:

    def __init__(self, initial_config):
        self.pq = PriorityQueue()
        self.initial = initial_config
        self.final = None

    def is_empty(self):
        return self.pq.empty()

    def is_solved(self):
        return self.final is not None

    def pop_min(self):
        #TODO
        return None

    def get_neighbors(self, model):
        #TODO
        return None

    def decrease_key(self, model):
        #TODO
        return

    def path_to_solved(self):
        reverse_path = [self.final]
        while reverse_path[len(reverse_path)-1].prev.data != self.initial.data:
            reverse_path.append(reverse_path[len(reverse_path)-1].prev)
        reverse_path.append(self.initial)
        path = []
        while len(reverse_path) != 0:
            path.append(reverse_path[len(reverse_path)-1])
        return path


if __name__ == "__main__":
    print("Running")
