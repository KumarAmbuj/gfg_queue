class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def isEmpty(self):
        return self.front==None

    def Enqueue(self,item):
        newnode=Node(item)
        if self.rear==None:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode
    def Dequeue(self):
        if self.isEmpty():
            return
        temp=self.front.data
        self.front=self.front.next
        if self.front==None:
            self.rear=None
        return temp

    def Front(self):
        return self.front.data

    def Rear(self):
        return self.rear.data

    def Display(self):
        p=self.front
        while(p):
            print(p.data,end=' ')
            p=p.next
        print()

queue=Queue()
print(queue.isEmpty())
queue.Enqueue(45)
queue.Enqueue(78)
queue.Display()
print(queue.Dequeue())