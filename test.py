import CircularQueue as cqu
ob=cqu.CQueue(size=100)

ob.Enqueue(12)

print(ob.Dequeue())

ob.Display()

ob.Empty()

ob.Full()