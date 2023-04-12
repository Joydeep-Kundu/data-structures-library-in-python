class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.prev=None
        self.next=None
class dlist:
    def __init__(self) -> None:
        self.head=None
    def createlist(self,*a):
        self.head=None
        tempNode1=None
        tempNode2=None
        for i in a:
            if self.head==None:
                self.head=Node(i)
                tempNode1=self.head
            else:
                tempNode1.next=Node(i)
                tempNode2=tempNode1
                tempNode1=tempNode1.next
                tempNode1.prev=tempNode2
                # print(tempNode1.data,tempNode1.prev.data)
    def display(self):
        if self.head==None:
            print("list is empty")
            return
        tempNode1=self.head
        while tempNode1!=None:
            print(tempNode1.data,end=' >')
            tempNode1=tempNode1.next
        print(None)
    def insert_at_begining(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            tempNode1=self.head
            self.head=Node(data)
            self.head.next=tempNode1
            tempNode1.prev=self.head
    def insert_at_last(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            tempNode1=self.head
            while tempNode1.next!=None:
                tempNode1=tempNode1.next
            tempNode2=tempNode1
            tempNode1.next=Node(data)
            tempNode1=tempNode1.next
            tempNode1.prev=tempNode2
    def insert_at_sepecific_position(self,pos,data):
        if pos<0:
            raise IndexError;
        if self.head==None:
            self.head=Node(data)
        elif pos==0:
            tempNode1=self.head
            self.head=Node(data)
            self.head.next=tempNode1
            tempNode1.prev=self.head
        else:
            ipos=0
            tempNode1=self.head
            while tempNode1.next!=None:
                if ipos==pos-1:
                    tempNode3=tempNode1.next
                    tempNode1.next=Node(data)
                    tempNode4=tempNode1.next
                    tempNode4.prev=tempNode1
                    tempNode4.next=tempNode3
                    tempNode3.prev=tempNode4
                    return
                tempNode1=tempNode1.next
                ipos+=1
            print(tempNode1.data)
            tempNode2=tempNode1
            tempNode1.next=Node(data)
            tempNode1=tempNode1.next
            tempNode1.prev=tempNode2
            
    def delete_begining(self):
        if self.head==None:
            return
        tempNode1=self.head
        if self.head.next==None:
            item=tempNode1.data
            self.head=None
            del tempNode1
            return item
        item=self.head.data
        self.head=self.head.next
        self.head.prev=None
        del tempNode1
        return item
    def delete_last(self):
        if self.head==None:
            print('list is empty')
        tempNode1=self.head
        if self.head.next==None:
            item=tempNode1.data
            self.head=None
            del tempNode1
            return item
        while tempNode1.next!=None:
            tempNode1=tempNode1.next
        tempNode2=tempNode1.prev
        tempNode2.next=None
        item=tempNode1.data
        del tempNode1
        return item

def main():
    p=dlist()
    p.createlist(0,1,2,3,4,5,6,77)
    # p.insert_at_begining(1)
    # p.insert_at_begining(0)
    # p.insert_at_begining(99)
    # p.insert_at_last(2)
    p.display()
    # p.delete_last()
    print('ds>>')
    p.insert_at_sepecific_position(89,333)
    p.display()
if __name__=="__main__":
    main()
        