#Multipath inheritance
class A:
    def fofca(self):
        print("Function of Class A")
class B(A):
    def fofcb(self):
        print("Function of Class B")
class D(A):
    def fofcd(self):
        print("Function of Class D") 
class C(B,D):
    def fofcc(self):
        print("Function of Class C")                     
objC=C() 
objC.fofca()
objC.fofcb() 
objC.fofcc() 
objC.fofcd()
  