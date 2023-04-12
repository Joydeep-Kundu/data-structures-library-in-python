from stack import stack
class postfix:
    def __init__(self,size=20):
        self.stack=stack(size)
        self.post=''
    def convertToPostfix(self,expr):
        expr=expr.split(' ');
        for i in expr:
            if i.isalpha() or i.isnumeric():
                self.post+=i+' '

            elif i=='(':
                self.stack.push(i)


            elif i==')':
                while self.stack.peek()!='(':
                    self.post+=self.stack.pop()+' '
                self.stack.pop()


            elif i=='+' or i=='-':
                while self.stack.peek()!=None and self.stack.peek()!='(' :
                    self.post+=self.stack.pop()+' '
                self.stack.push(i)


            elif i=='*' or i=='/':
                while self.stack.peek()!=None and self.stack.peek()!='('and (self.stack.peek()=='*' or self.stack.peek()=='/' or self.stack.peek()=='^'):
                    self.post+=self.stack.pop()+' '
                self.stack.push(i)


            elif i=='^':
                while self.stack.peek()!=None and self.stack.peek()!='('and self.stack.peek()=='^':
                    self.post+=self.stack.pop()+' '
                self.stack.push(i)


        while self.stack.peek()!=None:
            self.post+=self.stack.pop()+' '
        print(self.post)
        self.evaluatepostfix(self.post)


    def evaluatepostfix(self,exp):
        a=0
        b=0
        exp=exp.split()
        for i in exp:
            if i=='^':
                a=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(b**a)
            elif i=='+':
                a=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(b+a)
            elif i=='-':
                a=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(b-a)
            elif i=='/':
                a=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(b/a)
            elif i=='*':
                a=self.stack.pop()
                b=self.stack.pop()
                self.stack.push(b*a)
            else:
                self.stack.push(int(i))
        print(self.stack.pop())



if __name__=="__main__":
    post=postfix()
    post.convertToPostfix('( 12 * 8 ) - ( 14 * 9 ) + ( 18 * 8 ) - ( 8 * 6 )')
    # post.evaluatepostfix('')