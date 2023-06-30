class Queue:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return self.item==[]

    def Enqueue(self,item):
        self.item.append(item)

    def Dequeue(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[0]

    def Display(self):
        for  i in self.item:
            print(i,end=' ')
        print()
from sys import maxsize
def Stack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()

def peek(stack):
    return stack[len(stack)-1]


def KReverse(q,k):
    stack=Stack()

    for i in range(k):
        temp=q.Dequeue()
        push(stack,temp)

    while not isEmpty(stack):
        temp=pop(stack)
        q.Enqueue(temp)

    q.Display()

    n=len(q.item)-k
    for i in range(n):
        temp=q.Dequeue()
        q.Enqueue(temp)

    q.Display()



q=Queue()
q.Enqueue(34)
q.Enqueue(45)
q.Enqueue(89)
q.Enqueue(32)
q.Enqueue(43)
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Display()
KReverse(q,7)



