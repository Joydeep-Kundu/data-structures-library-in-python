class Node:
    def __init__(self,val=0) -> None:
        self.data=val
        self.next=None
class Clink_list:
    def __init__(self) -> None:
        self.head=None
    def insert_at_begining(self,item):
        if self.head==None:
            self.head=Node(item)
            self.head.next=self.head
        else:
            m=n=self.head
            while n.next!=self.head:
                n=n.next
            self.head=Node(item)
            self.head.next=m
            n.next=self.head
    def insert_at_end(self,item):
        if self.head==None:
            self.head=Node(item)
            self.head.next=self.head
        else:
            tempNode1=self.head
            while tempNode1.next!=self.head:
                tempNode1=tempNode1.next
            tempNode1.next=Node(item)
            tempNode1.next.next=self.head

    def insert_after_item(self,item,val):
        if self.head==None:
            print("list is empty")
            return
        tempNode1=self.head
        tempNode2=None
        while tempNode1.next!=self.head:
            if tempNode1.data==item:
                tempNode2=tempNode1.next
                tempNode1.next=Node(val);
                tempNode1.next.next=tempNode2
                return
            tempNode1=tempNode1.next
        if tempNode1.data==item:
            tempNode1.next=Node(val)
            tempNode1.next.next=self.head
            return
        print("item not Found on the list")

    def insert_at_nth_position(self,nth_pos,val):
        if self.head==None or nth_pos==0:
            self.insert_at_begining(val)
        list_counter=0
        tempNode1=self.head
        tempNode2=None
        while tempNode1.next!=self.head:
            if list_counter==nth_pos-1:
                tempNode2=tempNode1.next
                tempNode1.next=Node(val)
                tempNode1.next.next=tempNode2
                return
            tempNode1=tempNode1.next
            list_counter+=1
        self.insert_at_end(val)

        
    def delete_first(self):
        if self.head==None:
            print("list is empty")
            return 
        tempNode1=self.head
        item=tempNode1.data
        if self.head==self.head.next:
            self.head=None
            del tempNode1
            return item
        
        tempNode2=tempNode1
        while tempNode2.next!=self.head:
            tempNode2=tempNode2.next
        self.head=self.head.next
        tempNode2.next=self.head
        del tempNode1
        return item
    def delete_last(self):
        if self.head==None:
            print("list is empty")
            return 
        tempNode1=self.head
        item=tempNode1.data
        if self.head==self.head.next:
            self.head=None
            del tempNode1
            return item
        tempNode2=tempNode1
        tempNode3=None
        while tempNode2.next!=self.head:
            tempNode3=tempNode2
            tempNode2=tempNode2.next
        tempNode3.next=self.head
        item=tempNode2.data
        del tempNode1
        return item
    def delete_specific_item(self,item):
        if self.head==None:
            print("list is empty")
        tempNode1=self.head
        tempNode2=tempNode3=None;
        if self.head.data==item:
            return self.delete_first()
            
        while tempNode1.next!=self.head:
            if tempNode1.data==item:
                tempNode2.next=tempNode1.next
                item=tempNode1.data
                del tempNode1
                return item
            tempNode2=tempNode1
            tempNode1=tempNode1.next
        if tempNode1.data== item:
            tempNode2.next=self.head
            item=tempNode1.data
            del tempNode1
            return item
        print('item not found in the list')
    def delete_item_in_specific_position(self,pos):
        if self.head==None:
            print('List is empty')
            return
        if self.head.next==self.head:
            tempNode1=self.head
            item=self.head.data
            self.head=None
            del tempNode1
            return item
        tempNode2=self.head
        tempNode3=None
        if pos==0:
            tempNode3=self.head
            while tempNode3.next!=self.head:
                tempNode3=tempNode3.next
            self.head=self.head.next
            tempNode3.next=self.head
            item=tempNode2.data
            del tempNode2
            return item
        # ipos=0
        # if tempNode2.next!=self.head:
        #     if ipos==pos-1:
        #         tempNode3=tempNode2
        #         tempNode2=tempNode2.next
        #         tempNode3.next=tempNode2.next
        #         item=tempNode2.data
        #         del tempNode2
        #         return item
        #     tempNode2=tempNode2.next
        # print(tempNode2.data)
        # tempNode3.next=self.head
        # item=tempNode2.data
        # del tempNode2
        # return item



    def display(self):
        if self.head==None:
            print("list is empty")
            return
        tempNode1=self.head
        while tempNode1.next!=self.head:
            print(tempNode1.data,end=' >')
            tempNode1=tempNode1.next
        print(tempNode1.data)
            
def main():
    list1=Clink_list()
    list1.insert_at_begining(3)
    list1.insert_at_begining(2)
    list1.insert_at_begining(1)
    list1.insert_at_begining(0)
    list1.insert_at_end(5)
    list1.insert_at_end(6)
    list1.display()
    print()
    print(list1.delete_last())
    list1.display()
    print()
    list1.insert_after_item(5,7)
    list1.display()
    list1.insert_after_item(5,6)
    list1.display()
    print('s>>')
    list1.delete_item_in_specific_position(1)
    list1.display()
    list1.insert_at_nth_position(3,2222)
    list1.display()
    list1.delete_specific_item(-12)
    list1.display()
if __name__=="__main__":
    main()
            