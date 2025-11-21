#Parameterized Constructor
class Calculator:
    def __init__(self,x,y):
        self.a=x
        self.b=y 
    def putvalues(self):
        print("Value of a=",self.a) 
        print("Value of b=",self.b) 
    def mysum(self):
        return self.a+self.b  
c=Calculator(100,50) 
c.putvalues() 
print("Sum=",c.mysum())      