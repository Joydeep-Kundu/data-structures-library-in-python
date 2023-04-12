class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self) -> None:
        self.start=None
    def display(self):
        tempNode1=self.start
        while tempNode1!=None:
            print(tempNode1.data,end=' >')
            tempNode1=tempNode1.next
        print(None)
    def create_list(self,*a):
        self.start=Node(a[0])
        tempNode1=self.start
        for i in a[1:]:
            tempNode1.next=Node(i)
            tempNode1=tempNode1.next
    def reverse(self,tempNode1,tempNode2):
        if tempNode2==None:
            self.start=tempNode1
        else:
            temp=tempNode2.next
            tempNode2.next=tempNode1
            self.reverse(tempNode2,temp)
def main():
    li=linkedlist()
    li.create_list(0,1,2,3,4)
    li.display()
    li.reverse(None,li.start)
    li.display()
if __name__=='__main__':
    main()