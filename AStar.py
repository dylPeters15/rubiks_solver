from AStarPQ import AStarPQ

def AStar(initialConfig):
    pq = AStarPQ(initialConfig)
    while not pq.is_empty():
        current = pq.pop_min()
        for neighbor in pq.get_neighbors(current):
            if (neighbor.get_dist() > current.get_dist() + 1):
                neighbor.set_dist(current.get_dist() + 1)
                neighbor.set_prev(current)
                pq.decrease_key(neighbor)