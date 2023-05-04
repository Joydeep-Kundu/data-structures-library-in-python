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

class Node:
    def __init__(self,val) -> None:
        self.data=val
        self.next=None
class lqueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,item):
        if self.front==None and self.rear==None:
            self.front=self.rear=Node(item)
        else:
            self.rear.next=Node(item)
            self.rear=self.rear.next
    def dequeue(self):
        if self.front==None:
            print('queue is empty')
            return
        if self.front==self.rear:
            temp=self.front
            item=temp.data
            self.front=self.rear=None
            del temp
            return item
        temp=self.front
        item=temp.data
        self.front=self.front.next
        del temp
        return item
    def display(self):
        if self.front==None:
            print('queue is empty')
            return
        temp=self.front
        while temp!=self.rear:
            print(temp.data,end=' >')
            temp=temp.next
        print(temp.data)

        