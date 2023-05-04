import Sort
class create_list:
    def __init__(self,lst=[]):
        #This construction will initialize the list of items.
        #User may pass this list 'lst' or can take input through keyboard
        #User will input size of this list
        #then user will input the items
        self.data=[]
        if lst==[]:
            self.size=int(input("enter size for list: "))
            for i in range(self.size):
                self.data.append(int(input("enter item for postion {} : ".format(i+1))))
        else:
            self.data=lst
            self.size=len(lst)
    def display(self):
        #This function display list 'data' 
        print(self.data)

    def linerSearch(self,item):
        #this function search 'item' in the list 'data' 
        # if 'item' in the list then return position of the 'item'
        # otherwise return -1
        # This function search start to last one by one items
        idx=0
        while idx<self.size:
            if self.data[idx]==item:
                return idx
            idx+=1
        return -1
    def binarySearch(self,item):
        #this function will search the item 'item' form the list 'data'
        # if 'item' in the list then return position of the 'item'
        # otherwise return -1
        if not self.isAcending():
            s=Sort.Sort()
            s.selectionSort(self.data)    
        low=0
        high=self.size-1
        while low<=high:
            mid=(low+high)//2
            if self.data[mid]==item:
                return mid
            if self.data[mid]<item:
                low=mid+1
            else:
                high=mid-1
        return -1

if __name__=="__main__":
    ob=create_list([1,12,14,15,3])
    print(ob.binarySearch(15))