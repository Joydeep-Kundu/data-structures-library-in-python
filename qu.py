class queue:
    def __init__(self,size):
        self.__qu=[0 for i in range(size)]
        self.size=size;
        self.rear=-1;
        self.front=-1;
    def enqueue(self,item):
        if self.rear==self.size-1:
            print("queue full")
            return 
        self.rear+=1
        self.__qu[self.rear]=item
        if self.front==-1:
            self.front=0
    def dequeue(self):
        if self.rear==-1 and self.front==-1:
            print("queue is empty")
            return 
        item=self.__qu[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front+=1
        return item
    def display(self):
        if self.front==-1 and self.rear==-1:
            print('queue is empty')
            return
        idx=self.front;
        while idx<=self.rear:
            print(self.__qu[idx])
            idx+=1
    def peek(self):
        return self.__qu[self.rear]
if __name__=="__main__":
    q=queue(2)
    q.enqueue(1)
    q.enqueue(2)
    print(q.peek())
    q.display()
    q.dequeue()
    q.dequeue()
    q.dequeue()
        