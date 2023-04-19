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
            self.root==Node(data)
        else:
            self.d(self.root,data)
    def inorder(self):
        def g(nd):
            if nd==None:
                return
            g(nd.left)
            print(nd.data,end='>')
            g(nd.right)
        g(self.root)
        print()
    def postorder(self):
        def g(nd):
            if nd==None:
                return
            g(nd.left)
            g(nd.right)
            print(nd.data,end='>')
        g(self.root)
        print()
    def preoreder(self):
        def g(nd):
            if nd==None:
                return
            print(nd.data,end='>')
            g(nd.left)
            g(nd.right)
        g(self.root)
        print()
    def maxHeight(self):
        op=[0]
        n=0
        def d(nd,o,n=0):
            if nd==None:
                if n<o[0]:
                    o[0]=n
                return
            d(nd.left,o,n+1)
            d(nd.right,o,n+1)
        d(self.root,op,n)
        print(op)
    def search(self,item):
        def se(nd):
            if nd==None:
                print("item not found")
                return
            if nd.data==item:
                print('item found')
                return
            if nd.data<item:
                return se(nd.left)
            return se(nd.right)
        se(self.root)
                
o=BST()
o.createBST([120,50,150,60,30,170,130])
o.preoreder()
o.postorder()
o.inorder()
o.maxHeight()
o.search(120)