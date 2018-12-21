from ThreeByThreeModel import ThreeByThreeModel
from a_star import a_star

def test_left_down():
    print("Test Left Down")
    do_test("woowoowoogggrwwbbbgggrwwbbbgggrwwbbbyrryrryrroyyoyyoyy")

def test_right_down():
    print("Test Right Down")
    do_test("oowoowoowgggwwrbbbgggwwrbbbgggwwrbbbrryrryrryyyoyyoyyo")

def test_5_step():
    print("Test 5 Step")
    do_test("goyroyrwbogwggowbbygwrwowbbygrybbryogwworrbyyoggoyrwbr")

def test_7_step():
    print("Test 7 Step")
    do_test("obooowgwrbbrwobwgyygrgwbwbyyggorygybwwrorrryyboobygwrg")

def test_unknown():
    print("Test Unknown")
    do_test("roooooowgbwgwbrwyygggrwrwbbbyygbrwgbrobrrwwryoboyyyygg")

def do_test(data):
    model = ThreeByThreeModel(data=data)
    path = a_star(model)
    print(path)
    for state in path:
        print(state.in_edge)


test_left_down()
print("\n")
test_right_down()
print("\n")
test_5_step()
print("\n")
test_7_step()
print("\n")
test_unknown()
print("\n")
