import copy
class heap:
    def heapTree(self,t,min=False):
        ind=len(t)//2-1
        for i in range(ind,-1,-1):
            self.heapify(t,i,len(t),min)
    def heapify(self,a,i,size,min=False):
        l=2*i+1
        r=2*i+2
        if min:
            minimum=i
            if l<size and a[l]<a[minimum]:
                minimum=l
            if r<size and a[r]<a[minimum]:
                minimum=r
            if minimum!=i:
                a[minimum],a[i]=a[i],a[minimum]
                self.heapify(a,minimum,size,True)        
        else:
            largest=i
            if l<size and a[l]>a[largest]:
                largest=l
            if r<size and a[r]>a[largest]:
                largest=r
            if largest!=i:
                a[largest],a[i]=a[i],a[largest]
                self.heapify(a,largest,size)


