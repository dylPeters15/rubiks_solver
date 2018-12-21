from ThreeByThreeModel import ThreeByThreeModel
from a_star import a_star

def test_left_down():
    data = "woowoowoogggrwwbbbgggrwwbbbgggrwwbbbyrryrryrroyyoyyoyy"
    model = ThreeByThreeModel(data=data)
    path = a_star(model)
    print(path)
    for state in path:
        print(state.in_edge)

def test_right_down():
    data = "oowoowoowgggwwrbbbgggwwrbbbgggwwrbbbrryrryrryyyoyyoyyo"
    model = ThreeByThreeModel(data=data)
    path = a_star(model)
    print(path)
    for state in path:
        print(state.in_edge)

def test_5_step():
    data = "goyroyrwbogwggowbbygwrwowbbygrybbryogwworrbyyoggoyrwbr"
    model = ThreeByThreeModel(data=data)
    path = a_star(model)
    print(path)
    for state in path:
        print(state.in_edge)


test_left_down()
test_right_down()
test_5_step()