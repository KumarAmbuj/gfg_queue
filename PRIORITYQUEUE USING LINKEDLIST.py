class Node:
    def __init__(self,data,priority):
        self.data=data
        self.priority=priority
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=None

    def isEmpty(self):
        return self.front==None

    def Enqueue(self,data,datapr):
        newnode=Node(data,datapr)
        if self.isEmpty() or datapr<=self.front.priority:
            newnode.next=self.front
            self.front=newnode

            return

        p=self.front
        while p.next!=None and p.next.priority<datapr:
            p=p.next
        newnode.next=p.next
        p.next=newnode


    def Dequeue(self):
        if self.front==None:
            print('Queue is Empty')
            return
        x=self.front.data
        self.front=self.front.next
        return x

    def isEmpty(self):
        return self.front==None

    def Display(self):
        if self.isEmpty():
            print('Queue is Empty')
            return

        p=self.front

        while(p):
            print(p.data,end=' ')
            print(p.priority)
            print()
            p=p.next
        print()

queue=PriorityQueue()
print(queue.isEmpty())

queue.Enqueue(34,3)
queue.Enqueue(45,2)
queue.Enqueue(89,7)
queue.Enqueue(17,5)
queue.Enqueue(26,1)
queue.Enqueue(15,6)
queue.Enqueue(90,8)
queue.Enqueue(32,4)

queue.Display()
print(queue.Dequeue())
print(queue.Dequeue())
print(queue.Dequeue())
print(queue.Dequeue())
print(queue.Dequeue())







