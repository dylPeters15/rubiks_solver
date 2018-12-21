from ThreeByThreeModel import ThreeByThreeModel
from heapdict.heapdict import heapdict


def a_star(initial_config):
    hd = heapdict()
    solved_config = None
    hd[initial_config] = initial_config.get_a_star_weight()

    num_iterations = 0
    while len(hd) > 0 and solved_config is None:
        current = hd.popitem()[0]
        num_iterations += 1
        if num_iterations % 1000 == 0:
            print(current)
            print("num_iterations: {}".format(num_iterations))
        if num_iterations > 50000:
            print(current)
            return a_star(current)
        # print("Current: {}".format(current))
        if current.is_solved():
            solved_config = current
            break

        for neighbor in current.get_neighbors():
            # print("Neighbor: {}".format(neighbor))
            if neighbor in hd:
                if neighbor.get_a_star_weight() < hd[neighbor]:
                    hd[neighbor] = neighbor.get_a_star_weight()
            else:
                if neighbor.dist < 50:
                    hd[neighbor] = neighbor.get_a_star_weight()
                # else:
                #     print("Found too high distance")

            if neighbor.is_solved():
                solved_config = neighbor
                break
        # return []

    return _get_path(initial_config, solved_config)


def _get_path(initial_config, solved_config):
    print("Initial: {}".format(initial_config))
    print("Solved: {}".format(solved_config))

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