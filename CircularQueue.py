import cutomexeption as ce
class CQueue:
    def __init__(self,size=20):
        if size<=0:
            raise ce.size("size error")
        else:
            self.__qu=[0 for i in range(size)]
            self.__size=size;
            self.__rear=-1;
            self.__front=-1;
    def Enqueue(self,item):
        if (self.__rear+1)%self.__size==self.__front:
            raise ce.OverFlow()
        self.__rear=(self.__rear+1)%self.__size
        self.__qu[self.__rear]=item
        if self.__front==-1 :
            self.__front=0
    def Dequeue(self):
        if self.__rear==-1 and self.__front==-1:
            raise ce.UnderFlow()
            return
        item=self.__qu[self.__front]
        if self.__front==self.__rear:
            self.__front=-1
            self.__rear=-1
        else:
            self.__front=(self.__front+1)%self.__size
        return item
    def Display(self):
        if self.__front==-1 and self.__rear==-1:
            print('empty')
            return
        idx=self.__front;
        if idx>self.__rear:
            while(idx<self.__size):
                print(self.__qu[idx])
                idx+=1
            idx=0
        while idx<=self.__rear:
            print(self.__qu[idx])
            idx+=1
    def Full(self):
        if (self.__rear+1)%self.__size==self.__front:
            return True
        return False;
    def Empty(self):
        if self.__rear==-1 and self.__front==-1:
            return True
        return False
    
if __name__=="__main__":
    q=CQueue(3)
    q.Enqueue(1)
    # q.Dequeue()
    q.Enqueue(2)
    q.Enqueue(3)
    q.Enqueue(4)
    # print(q.peek())
    q.Display()
    q.Dequeue()
    q.Enqueue(2)
    q.Display()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()
    q.Dequeue()










        