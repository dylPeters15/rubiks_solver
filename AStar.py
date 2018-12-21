from ThreeByThreeModel import ThreeByThreeModel
from AStarPQ import AStarPQ

def AStar(initialConfig):
    pq = AStarPQ(ThreeByThreeModel(data=initialConfig))
    while not pq.is_empty() and not pq.is_solved():
        current = pq.pop_min()
        for neighbor in pq.get_neighbors(current):
            if (neighbor.get_dist() > current.get_dist() + 1):
                neighbor.set_dist(current.get_dist() + 1)
                neighbor.set_prev(current)
                pq.decrease_key(neighbor)

    return pq.path_to_solved()

if __name__ == "__main__":
    print("Running")