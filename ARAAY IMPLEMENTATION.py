class Queue:
    def __init__(self,size):
        self.size=size
        self.front=-1
        self.rear=-1
        self.queue=[None]*self.size

    def isFull(self):

        return (self.rear+1)%self.size==self.front
    def isEmpty(self):
        return self.front==-1


    def Enqueue(self,item):


        if (self.rear+1)%self.size==self.front:
            print('Queue is Full')

        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=item
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=item
    def Dequeue(self):

        if self.front==-1:
            print('Queue is Empty')
            return

        elif self.front==self.rear:
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp

    def Front(self):
        if self.front==-1:
            print('Queue is empty')
            return
        return self.queue[self.front]

    def Rear(self):
        if self.front==-1:
            print('Queue is empty')
            return
        return self.queue[self.rear]

    def display(self):
        if self.front==-1:
            print('Queue is Empty')
        elif self.rear>=self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
        else:
            for i in range(self.front,self.size):
                print(self.queue[i],end=' ')
            for i in range(0,self.rear+1):
                print(self.queue[i],end=' ')
        print()

queue=Queue(5)
print(queue.isEmpty())
queue.display()
queue.Enqueue(4)
queue.Enqueue(8)
queue.Enqueue(6)
queue.Enqueue(9)
queue.Enqueue(10)
queue.display()
print(queue.Front())
print(queue.Rear())
print(queue.Dequeue())
queue.display()
print(queue.Dequeue())
queue.display()
print(queue.Front())
print(queue.Rear())








        