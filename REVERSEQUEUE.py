class Queue:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return self.item==[]

    def Enqueue(self,item):
        self.item.append(item)

    def Dequeue(self):
        return self.item.pop(0)

    def Front(self):
        return self.item[0]

    def Display(self):
        for i in self.item:
            print(i,end=' ')
        print()

def reverse(q):
    if q.isEmpty():
        return

    temp=q.Dequeue()

    reverse(q)

    q.Enqueue(temp)


q=Queue()
q.Enqueue(23)
q.Enqueue(78)
q.Enqueue(34)
q.Enqueue(30)
q.Enqueue(42)
q.Display()

reverse(q)

q.Display()


