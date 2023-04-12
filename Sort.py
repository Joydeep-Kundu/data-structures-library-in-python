class Sort:
    def selectionSort(self,data,decending=False):
        #this function take list 'data' optional parameter decending set to false
        # this function sort the list accending order
        # if decending is True sort the list denending oreder
        size=len(data)
        self.data=data
        idx1=0
        idx2=0
        if not decending:
            while idx1<size-1:
                idx2=idx1+1
                while idx2<size:
                    if self.data[idx2]<self.data[idx1]:
                        temp=self.data[idx1]
                        self.data[idx1]=self.data[idx2]
                        self.data[idx2]=temp
                    idx2+=1
                idx1+=1
        else:
            while idx1<size-1:
                idx2=idx1+1
                while idx2<size:
                    if self.data[idx2]>self.data[idx1]:
                        temp=self.data[idx1]
                        self.data[idx1]=self.data[idx2]
                        self.data[idx2]=temp
                    idx2+=1
                idx1+=1
    def bubleSort(self,data,decending=False):
        idx=0
        size=len(data)
        if decending:
            while idx<size-1:
                idx2=0
                cnt=0
                while idx2<size-idx-1:
                    if data[idx2]<data[idx2+1]:
                        temp=data[idx2]
                        data[idx2]=data[idx2+1]
                        data[idx2+1]=temp
                        cnt+=1
                    idx2+=1
                if cnt==0:
                    break
                idx+=1
        else:
            while idx<size-1:
                idx2=0
                cnt=0
                while idx2<size-idx-1:
                    if data[idx2]>data[idx2+1]:
                        temp=data[idx2]
                        data[idx2]=data[idx2+1]
                        data[idx2+1]=temp
                        cnt+=1
                    idx2+=1
                if cnt==0:
                    break
                idx+=1
    def insertionSort(self,data,decending=False):
        size=len(data)
        idx=1
        while idx<size:
            idx2=idx-1
            item=data[idx]
            while idx2!=-1 and data[idx2]>item:
                data[idx2+1]=data[idx2]
                idx2-=1
            data[idx2+1]=item
            idx+=1
    def quickSort(self,data,low,high):
        if low<=high:
            pivot=self.quick(data,low,high)
            self.quickSort(data,low,pivot-1)
            self.quickSort(data,pivot+1,high)
    def quick(self,data,low,high):
        piv=low
        rt=high
        lt=low+1
        while True:
            while lt<=rt and data[piv]<=data[rt]:
                rt-=1
            if data[piv]>data[rt]:
                data[piv],data[rt]=data[rt],data[piv]
                piv=rt
                rt-=1
            if lt>rt:
                return piv;
            while lt<=rt and data[piv]>=data[lt]:
                lt+=1
            if data[piv]<data[lt]:
                data[piv],data[lt]=data[lt],data[piv]
                piv=lt
                lt+=1
            if lt>rt:
                return piv;
    def merge(self,arr1,arr2):
        len1,len2=len(arr1),len(arr2)
        i=j=0
        c=[]
        while i<len1 and j<len2:
            if arr1[i]>arr2[j]:
                c.append(arr2[j])
                j+=1
            else:
                c.append(arr1[i])
                i+=1
        while i<len1:
            c.append(arr1[i])
            i+=1
        while j<len2:
            c.append(arr2[j])
            j+=1
        return c
    def mergeSort(self,data):
        le=len(data)
        if le==1:
            return data
        mid=(le)//2
        a=self.mergeSort(data[:mid])
        b=self.mergeSort(data[mid:])
        return self.merge(a,b)
if "__main__"==__name__:
    l=[1,4,95,1,3,5,32,-1,92]
    s=Sort()
    # print(s.merge([3, 5],[32, -1]))
    print("sfda",s.mergeSort(l))
    # print(l)
    del l