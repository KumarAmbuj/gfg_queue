class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularQueue:
    def __init__(self):
        self.front=None
        self.rear=None

def isEmpty(q):
    return q.front==None

def Enqueue(q,data):
    newnode=Node(data)

    if q.front==None:
        q.front=q.rear=newnode
        q.rear.next=q.front
    else:
        q.rear.next=newnode
        q.rear=newnode
        q.rear.next=q.front
def Dequeue(q):
    if q.front==None:
        print('Queue is Empty')
        return
    temp=None
    if q.front==q.rear:
        temp=q.front.data
        q.front=q.rear=None
    else:
        temp=q.front.data
        q.front=q.front.next
        q.rear.next=q.front

    return temp


def Front(q):
    if q.front==None:
        return
    return q.front.data
def Rear(q):
    if q.rear==None:
        return
    return q.rear.data

def Display(q):
    t=q.front
    while(t.next!=q.front):
        print(t.data,end=' ')
        t=t.next
    print(t.data)
    print()

queue=CircularQueue()
print(isEmpty(queue))
Enqueue(queue,56)
Enqueue(queue,89)
Display(queue)
Enqueue(queue,45)
Enqueue(queue,86)
Display(queue)
print(Dequeue(queue))
Display(queue)
print(Front(queue))
print(Rear(queue))
print(Dequeue(queue))
print(Dequeue(queue))
print(Dequeue(queue))
print(Dequeue(queue))
print(Dequeue(queue))

