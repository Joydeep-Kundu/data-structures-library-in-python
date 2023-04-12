class towerOfHonoi:
    def TOH(self,n,beg,aux,end):
        if n==1:
            print('{}=>{}'.format(beg,end))
        else:
            self.TOH(n-1,beg,end,aux)
            print('{}=>{}'.format(beg,end))
            self.TOH(n-1,aux,beg,end)
o=towerOfHonoi()
o.TOH(3,'beg','aux','end')