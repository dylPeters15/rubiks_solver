from ThreeByThreeView import ThreeByThreeView
from ThreeByThreeModel import ThreeByThreeModel
# ThreeByThreeView()
from Queue import PriorityQueue

a = ThreeByThreeModel()
b = ThreeByThreeModel("ogooooooogogwwwbbbgggwwwbbbgggwwwbbbrrrrrrrrryyyyyyyyy",prev=a,dist=a.dist+1)
print(a.__hash__())
print(b.__hash__())
print(a.__cmp__(b))
pq = PriorityQueue()
pq.put(b)
pq.put(a)
pq.put(b)
pq.put(a)
pq.put(b)
print ("printing")
print pq.co
print(pq.get().__hash__())
print(pq.get().__hash__())
print(pq.get().__hash__())