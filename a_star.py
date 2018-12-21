from ThreeByThreeModel import ThreeByThreeModel
from heapdict.heapdict import heapdict

def a_star(initial_config):
    hd = heapdict()
    solved_config = None
    hd[initial_config] = initial_config.get_a_star_weight()

    while len(hd) > 0 and solved_config is None:
        current = hd.popitem()[0]
        if current.is_solved():
            solved_config = current
            break

        for neighbor in current.get_neighbors():
            if neighbor in hd:
                if neighbor.get_a_star_weight < hd[neighbor]:
                    hd[neighbor] = neighbor.get_a_star_weight
            else:
                hd[neighbor] = neighbor.get_a_star_weight()

            if neighbor.is_solved():
                solved_config = neighbor
                break

    return _get_path(initial_config, solved_config)

def _get_path(initial_config, solved_config):
    print(initial_config)
    print(solved_config)

    reverse_path = [solved_config]
    while reverse_path[len(reverse_path) - 1].prev is not None and reverse_path[len(reverse_path) - 1].prev.data != initial_config.data:
        reverse_path.append(reverse_path[len(reverse_path) - 1].prev)
    reverse_path.append(initial_config)
    path = []
    for i in range(len(reverse_path)):
        path.append(reverse_path[len(reverse_path)-i-1])
    return path


if __name__ == "__main__":
    print("Running")