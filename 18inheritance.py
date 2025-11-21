#Single
class A:
    def funca(self):
        print("This is function A")
class B(A):
    def funcb(self):
        print("This is function B")
obj=B() 
obj.funca()
obj.funcb()               
        