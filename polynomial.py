class term:
    def __init__(self,c=1,e=0):
        self.coff=c
        self.expo=e
        self.next=None
class polynomial:
    def __init__(self) -> None:
        self.start=None
    def add_term(self,coff,expo):
        if self.start==None:
            self.start=term(coff,expo)
            return
        temp=self.start
        if self.start.expo<expo:
            self.start=term(coff,expo)
            self.start.next=temp
            return
        prev=None
        while temp!=None:
            if temp.expo==expo:
                temp.coff+=coff
                return
            if temp.expo<expo:
                prev.next=term(coff,expo)
                prev=prev.next
                prev.next=temp
                return
            prev=temp
            temp=temp.next
        prev.next=term(coff,expo)
        return
    def multipy_term(self,coff,expo):
        if self.start==None:
            self.start=term(coff,expo)
            return
        temp=self.start
        if self.start.expo<expo:
            self.start=term(coff,expo)
            self.start.next=temp
            return
        prev=None
        while temp!=None:
            if temp.expo==expo:
                temp.coff*=coff
                return
            if temp.expo<expo:
                prev.next=term(coff,expo)
                prev=prev.next
                prev.next=temp
                return
            prev=temp
            temp=temp.next
        prev.next=term(coff,expo)
        return
                
    def display(self):
        if self.start==None:
            return
        temp=self.start
        while temp!=None:
            print((temp.coff,temp.expo),end=' >')
            temp=temp.next
        print(None)
    def multily_polynomial(self,p1,p2):
        temp=polynomial()
        n=p2
        while p1!=None:
            p2=n
            while p2!=None:
                temp.add_term(p1.coff*p2.coff,p1.expo+p2.expo)
                p2=p2.next
            p1=p1.next
        self.start=temp.start
                

    def join_polynomimal(self,polynomial1,multyply=False):
        if multyply:
            while polynomial1!=None:
                self.multipy_term(polynomial1.coff,polynomial1.expo)
                polynomial1=polynomial1.next
        else:
            while polynomial1!=None:
                self.add_term(polynomial1.coff,polynomial1.expo)
                polynomial1=polynomial1.next
def main():
    p1=polynomial()
    p1.add_term(1,1)
    p1.add_term(2,2)
    p1.display()

    p=polynomial()
    p.add_term(1,1)
    p.add_term(5,9)
    p.add_term(3,1)
    p.add_term(2,2)
    p.add_term(5,2)
    p.display()
    p2=polynomial()
    p2.multily_polynomial(p1.start,p.start)
    p2.display()
if __name__=="__main__":
    main()