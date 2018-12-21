from ThreeByThreeModel import ThreeByThreeModel
initial_data = "ooooooooogggwwwbbbgggwwwbbbgggwwwbbbrrrrrrrrryyyyyyyyy"
print(len(set(ThreeByThreeModel(initial_data).get_neighbors())))
print(ThreeByThreeModel(initial_data).get_neighbors())
print(len(set(ThreeByThreeModel(initial_data).get_neighbors_data_only())))
print(ThreeByThreeModel(initial_data).get_neighbors_data_only())