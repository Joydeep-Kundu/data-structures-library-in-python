import cutomexeption as ce

class stack:
    def __init__(self,size=10) -> None:
        if size <=0:
            raise ce.size('size error')
        self.__size=size
        self.__top=-1
        self.__arr=[0 for i in range(self.__size)]
    def isEmpty(self):
        if self.__top==-1:
            return True
        return False
    def isFull(self):
        if self.__top==self.__size-1:
            return True
        return False
    def getSize(self):
        return self.__size
    def display(self):
        if self.__top==-1:
            return
        idx=self.__top
        while idx>=0:
            print(self.__arr[idx],end=' >')
            idx+=1
        print(None)
    def push(self,item):
        if self.__top==self.__size-1:
            raise ce.OverFlow('stack is full error')
        self.__top+=1
        self.__arr[self.__top]=item
    def pop(self):
        if self.__top==-1:
            raise ce.UnderFlow('stack is empty error')
        item=self.__arr[self.__top]
        self.__top-=1
        return item
    def peek(self):
        if self.__top==-1:
            raise ce.Empty('stack empty error')
        return self.__arr[self.__top]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Lstack:
    def __init__(self):
        self.start=None
        self.__top=None
    def push(self,item):
        if self.__top==None:
            self.__top=self.start=Node(item)
        else:
            self.__top.next=Node(item)
            self.__top=self.__top.next
    def pop(self):
        if self.start==None:
            raise ce.UnderFlow("can't delete from stack is empty")
        temp=self.start
        if self.start.next=None:
            self.start=None
            item=temp.data
            del temp
            return item
    def diplay(self):
        if self.__top==None:
            return
        temp=self.start
        while temp!=None:
            print(temp.data,end=' >')
            temp=temp.next
        print(None)
            
def main():
    st=stack(-10)
    st.peek()
    st.push(10)
    st.push(20)
    st.push(100)
    print(st.pop())
    st.display()
if __name__=="__main__":
    main()


