class adjMatrix:
    def __init__(self,no) -> None:
        self.mat=[[0 for i in range(no)] for j in range(no)]
        self.noOfVertex=no
    def createAdjMat(self,*a,dir=False):
        if dir:
            for i,j in a:
                self.mat[i][j]=1
        else:
            for i,j in a:
                self.mat[i][j]=1
                self.mat[j][i]=1
            print(i)
                    
    def display(self):
        for i in self.mat:
            print(i)
    def degree(self):
        de=[0 for i in range(self.noOfVertex)]
        for i,j in enumerate(self.mat):
            de[i]=j.count(1)
        return de
    def outDegree(self):
        de=[0 for i in range(self.noOfVertex)]
        for i,j in enumerate(self.mat):
            de[i]=j.count(1)
        return de
    def inDegree(self):
        de=[0 for i in range(self.noOfVertex)]
        for i in range(self.noOfVertex):
            de[i]=[r[i] for r in self.mat].count(1)
        return de

if __name__=='__main__':
    s=adjMatrix(6)
    # s.createAdjMat((0,1),(0,2),(1,2),(1,3),(1,4),(2,4),(3,5),(4,5))/
    s.createAdjMat((0,1),(0,2),(1,2),(1,3),(2,4),(3,5),(4,5),(4,1),dir=True)
    # print(s.degree())
    print()
    print(s.inDegree())
    print(s.outDegree())
    print()

    s.display()