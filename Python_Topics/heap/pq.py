from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, "B"))
pq.put((4, "D"))
pq.put((1, "A"))
pq.put((3, "C"))

while not pq.empty():
    print(pq.get())
