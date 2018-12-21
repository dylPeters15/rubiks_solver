from ThreeByThreeModel import ThreeByThreeModel
from queue import PriorityQueue

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

print(len(all))

pq = PriorityQueue()
for current in all:
    pq.put(current)
    print(current)

print("PQ Size: {}".format(pq.qsize()))
while not pq.empty():
    print(pq.get())
