class EmptyQueueError(Exception):
    pass

class Dequeue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue==[]

    def size(self):
        return len(self.queue)

    def InsertFront(self,item):
        self.queue.insert(0,item)

    def InsertRear(self,item):
        self.queue.append(item)

    def DeleteFront(self):
        if self.isEmpty():
            raise EmptyQueueError('Queue is Empty')
        return self.queue.pop(0)

    def DeleteRear(self):
        if self.isEmpty():
            raise EmptyQueueError('Queue is Empty')
        return self.queue.pop()

    def First(self):
        if self.isEmpty():
            raise EmptyQueueError('Queue is Empty')
        return self.queue[0]

    def Last(self):
        if self.isEmpty():
            raise EmptyQueueError('Queue is Empty')
        return self.queue[-1]

    def Display(self):
        for i in range(len(self.queue)):
            print(self.queue[i],end=' ')
        print()

queue=Dequeue()
print(queue.isEmpty())
queue.InsertFront(2)
queue.InsertFront(8)
queue.InsertRear(7)
queue.InsertRear(3)
queue.Display()
print(queue.DeleteRear())
queue.Display()
print(queue.DeleteFront())
queue.Display()
print(queue.DeleteFront())
print(queue.DeleteFront())


