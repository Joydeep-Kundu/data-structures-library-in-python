class Node:
    def __init__(self,val,bf=0) -> None:
        self.key=val
        self.left=None
        self.right=None
        self.bf=bf;
class AVLtree:
    def __init__(self):
        self.root=None
    def insert_a_node(self,data):
        if self.root==None:
            self.root=Node(data)
            self.balfactor()
        else:
            self.__d(self.root,data)
            self.balfactor()
            s=self.__spivot(self.root,None,data,None,None)
            while s[0]!=None:
                print("unbalance",s[0].key)
                self.preoreder()
                if (((s[1].bf<=-2 )and  (s[0].bf>=2)) or (s[0].bf<=-2)):
                # if ((self.root.left !=None and self.root.left.key==s[0].key)or(s[1] !=None and s[1].left!=None and s[1].left.key==s[0].key)):
                    print('ll')
                    self.llRotation(s[0],s[1])
                elif s[0]. bf>=2:
                # elif((self.root.right !=None and self.root.right.key==s[0].key)or(s[1] !=None and s[1].right!=None and s[1].right.key==s[0].key)):
                    print('rr')
                    self.rrRoration(s[0],s[1])
                s=self.__spivot(self.root,None,data,None,None)
                self.balfactor()
    def rrRoration(self,nd,p):
        if p!=None:
            s=nd
            p.right=nd.right
            nd=p.right
            h=nd.left
            nd.left=s
            s.right=h
        else:
            s=nd
            self.root=nd.right
            nd=self.root
            h=nd.left
            nd.left=s
            s.right=h
        self.balfactor()
    def llRotation(self,nd,p):
        if p!=None:
            s=nd
            p.left=nd.left
            nd=p.left
            h=nd.right
            nd.right=s
            s.left=h
        else:
            s=nd
            self.root=nd.left
            nd=self.root
            h=nd.right
            nd.right=s
            s.left=h
        self.balfactor()
    def __spivot(self,nd,par,item,par2,p):
        if nd==None:
            print("item not found")
            return (par,p)
        if nd.bf in [2,-2]:
            p=par2
            par=nd
        if nd.key==item:
            print('item found')
            return (par,p)
        if nd.key>item:
            return self.__spivot(nd.left,par,item,nd,p)
        return self.__spivot(nd.right,par,item,nd,p)
        
    def __d(self,nd,data):
        if data<nd.key:
            if nd.left==None:
                nd.left=Node(data)
                return
            return self.__d(nd.left,data)
        if nd.right==None:
            nd.right=Node(data)
            return
        return self.__d(nd.right,data)
    def inorder(self):
        def g(nd):
            if nd==None:
                return
            g(nd.left)
            print(nd.key,nd.bf,end=' > ')
            g(nd.right)
        g(self.root)
        print()
    def postorder(self):
        def g(nd):
            if nd==None:
                return
            g(nd.left)
            g(nd.right)
            print(nd.key,end=' > ')
        g(self.root)
        print()
    def preoreder(self):
        def g(nd):
            if nd==None:
                return
            print(nd.key,nd.bf,end=' > ')
            g(nd.left)
            g(nd.right)
        g(self.root)
        print()
    def hight(self,t):
        if t==None:
            return 0
        return max(self.hight(t.left),self.hight(t.right))+1
    def balfactor(self):
        def bf(t):
            if t==None:
                return
            t.bf=self.hight(t.left)-self.hight(t.right)
            bf(t.left)
            bf(t.right)
        bf(self.root)

            
def main():
    t=AVLtree();
    t.insert_a_node(1)
    t.preoreder()
    t.insert_a_node(-1)
    t.preoreder()
    t.insert_a_node(3)
    t.preoreder()
    t.insert_a_node(-3)
    t.preoreder()
    t.insert_a_node(2)
    t.preoreder()
    t.insert_a_node(90)
    t.preoreder()
    t.insert_a_node(23)
    t.preoreder()
    t.insert_a_node(34)
    t.preoreder()
    t.insert_a_node(8)
    t.preoreder()
main()