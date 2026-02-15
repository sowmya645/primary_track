class A:
    def display(self):
        print("A")
class B:
    def display(self):
        print("B")
class C(A,B):
    def display(self):
        return super(A,self).display()
    
c=C()
c.display()