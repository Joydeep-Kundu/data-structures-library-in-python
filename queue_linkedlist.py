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
def main():
    qu=lqueue()
    qu.enqueue(0)
    qu.enqueue(1)
    qu.enqueue(2)
    qu.display()
    print(qu.dequeue())    
    qu.display()
if __name__=='__main__':
    main()