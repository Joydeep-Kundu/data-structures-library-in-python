import cutomexeption as ce
class Node:
    def __init__(self,value) -> None:
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self) -> None:
        self.root=None
    def d(self,nd,data):
        if data<nd.data:
            if nd.left==None:
                nd.left=Node(data)
                return
            return self.d(nd.left,data)
        if nd.right==None:
            nd.right=Node(data)
            return
        return self.d(nd.right,data)
    def createBST(self,lst):
        for i in lst:
            if self.root==None:
                self.root=Node(i)
            else:
                temp=self.root
                par=None
                while temp!=None:
                    par=temp
                    if i<temp.data:
                        temp=temp.left
                    else:
                        temp=temp.right
                if i<par.data:
                    par.left=Node(i)
                else:
                    par.right=Node(i)
    def create_BST(self,*lst):
        if lst==():
            ce.Empty('list is empty')
        for i in lst:
            if self.root==None:
                self.root=Node(i)
            else:
                self.d(self.root,i)
    def insert_a_node(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.d(self.root,data)
    def inorder(self):
        def g(nd):
            if nd==None:
                return
            g(nd.left)
            print(nd.data,end=' > ')
            g(nd.right)
        g(self.root)
        print()
    def postorder(self):
        def g(nd):
            if nd==None:
                return
            g(nd.left)
            g(nd.right)
            print(nd.data,end=' > ')
        g(self.root)
        print()
    def preoreder(self):
        def g(nd):
            if nd==None:
                return
            print(nd.data,end=' > ')
            g(nd.left)
            g(nd.right)
        g(self.root)
        print()
    def hight(self):
        def d(t):
            if t==None:
                return 0
            return max(d(t.left),d(t.right))+1
        print(d(self.root))


    def maxHeight(self):
        op=[0]
        n=0
        def d(nd,o,n=0):
            if nd==None:
                if n>o[0]:
                    o[0]=n
                return
            d(nd.left,o,n+1)
            d(nd.right,o,n+1)
        d(self.root,op,n)
        print(op[0])
    def search(self,item):
        def se(nd,par=None):
            if nd==None:
                print("item not found")
                return (nd,par)
            if nd.data==item:
                print('item found')
                return (nd,par)
            if nd.data>item:
                return se(nd.left,nd)
            return se(nd.right,nd)
        return se(self.root)
    def single(self,a,b):
            if a.data<b.data:
                if a.left!=None:
                    b.left=a.left
                elif a.right!=None:
                    b.left=a.right
                else:
                    b.left=None
            else:
                if a.left!=None:
                    b.right=a.left
                elif a.right!=None:
                    b.right=a.right
                else:
                    b.right=None
    def deletion(self,item):
        a,b=self.search(item)
        if a==None:
            print('not found')
            return

        if a.left==None or a.right==None:
            if b==None:
                if a.left==None:
                    self.root=a.right
                    return
                if a.right==None:
                    self.root=a.left
                    return
                if a.right==None and a.left==None:
                    self.root==None
                    return
            else:
                self.single(a,b)
        else:
            tempnd=a.right
            par=a
            b=None
            while tempnd.left!=None:
                par=tempnd
                tempnd=tempnd.left
            suc=tempnd.data
            print(tempnd.data,par.data)
            self.single(tempnd,par)
            a.data=suc
        
        
                
o=BST()
o.createBST([100,12,120,11,90,110,130])
# o.insert_a_node(180)
# o.preoreder()
# o.postorder()
o.inorder()
o.maxHeight()
print(o.search(120))
o.hight()
o.deletion(100)
o.inorder()
o.preoreder()