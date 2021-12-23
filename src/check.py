import heapq
from queue import PriorityQueue

if __name__ == '__main__':
    q = PriorityQueue()
    q.put(5)
    q.put(2)
    q.put()

    print(list)
    heapq.heapify(list)
    print(list)
    list.pop(0)
    print(list)
    print(len(list))

    def myFunc(e):
        return len(e)


    cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

    cars.sort(key=myFunc)
    print(cars)
    while not q.empty():
        print(q.get())
