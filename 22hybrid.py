#Hybrid inheritance
class A:
    def fofca(self):
        print("Function of Class A")
class B(A):
    def fofcb(self):
        print("Function of Class B")
class C:
    def fofcc(self):
        print("Function of Class C") 
class D(B,C):
    def fofcd(self):
        print("Function of Class D")                     
objD=D() 
objD.fofca()
objD.fofcb() 
objD.fofcc() 
objD.fofcd()
  