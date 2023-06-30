class Node:
    def __init__(self,data,datapr):
        self.data=data
        self.priority=datapr
        self.prev=None
        self.next=None
class PriorityQueue:
    def __init__(self):
        self.head=None

def isEmpty(q):
    return q.head==None

def Enqueue(q,data,datapr):
    newnode=Node(data,datapr)
    if isEmpty(q) or datapr<q.head.priority:
        newnode.next=q.head
        q.head.prev=newnode
        q.head=newnode
        newnode.prev=None
        return

    p=q.head
    while p!=None and p.next.priority<datapr:
        p=p.next
    newnode.next=p.next
    p.next.prev=newnode
    newnode.prev=p
    p.next=newnode

def Dequeue(q):
    x=q.head.data
    q.head=q.head.next
    q.head.prev=None
    return x

def Display(q):
    if q.isEmpty():
        print('queue is Empty')
        return

    t=q.head
    while(t):
        print(t.data,end=' ')
        print(t.priority)
        print()
        t=t.next
    print()





q=PriorityQueue()
print(isEmpty(q))
Enqueue(q,34,8)
Enqueue(q,56,4)
Enqueue(q,43,9)
Display(q)



