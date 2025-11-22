#Multiple inheritance
class A:
    def fofca(self):
        print("Function of Class A")
class B:
    def fofcb(self):
        print("Function of Class B")
class C(A,B):
    def fofcc(self):
        print("Function if Class C")              
objC=C() 
objC.fofca()
objC.fofcb() 
objC.fofcc() 
  