class Queue:
    def __init__(self):
        self.queue=[]
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        return len(self.queue)==0
    def Enqueue(self,item):
        if self.front==-1:
            self.front=0
        self.rear = self.rear + 1
        self.queue.append(item)

    def Dequeue(self):
        if self.front==-1:
            return
        temp=self.queue[self.front]
        self.front=self.front+1
        return temp

    def Front(self):
        return self.queue[self.front]
    def Rear(self):
        return self.queue[self.rear]

    def Display(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=' ')

queue=Queue()
print(queue.isEmpty())
queue.Enqueue(3)
queue.Enqueue(90)
print(queue.Dequeue())
queue.Display()


