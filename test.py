from ThreeByThreeModel import ThreeByThreeModel
from queue import PriorityQueue
from heapdict.heapdict import heapdict

initial_data = "ooooooooogggwwwbbbgggwwwbbbgggwwwbbbrrrrrrrrryyyyyyyyy"
# print(len(set(ThreeByThreeModel(initial_data).get_neighbors())))
# print(ThreeByThreeModel(initial_data).get_neighbors())
# print(len(set(ThreeByThreeModel(initial_data).get_neighbors_data_only())))
# print(ThreeByThreeModel(initial_data).get_neighbors_data_only())

model = ThreeByThreeModel(data=initial_data)
print(model)
neighbors = model.get_neighbors()
print(neighbors)
neighbors_of_neighbors = []
for neighbor in neighbors:
    neighbors_of_neighbors.extend(neighbor.get_neighbors())
    print(neighbor)

all = []
all.append(model)
all.extend(neighbors)
all.extend(neighbors_of_neighbors)

print("Length of all: {}".format(len(all)))
print("Length of set(all): {}".format(len(set(all))))

hd = heapdict()
for current in all:
    if current in hd:
        if hd[current] > current.dist + current.distance_from_solved:
            hd[current] = current.dist + current.distance_from_solved
    else:
        hd[current] = current.dist + current.distance_from_solved


print("size of hd: {}".format(len(hd)))
while len(hd) != 0:
    print(hd.popitem())

# pq = PriorityQueue()
# for current in all:
#     pq.put(current)
#     print(current)
#
# print("PQ Size: {}".format(pq.qsize()))
# while not pq.empty():
#     print(pq.get())
