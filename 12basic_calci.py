#Basic Calculator
class Calculator:
    def getValues(self):
        self.a=int(input("Enter the Value of a:"))
        self.b=int(input("Enter the Value of b:"))
    def putValues(self):
        print("Values of a=",self.a) 
        print("Values of b=",self.b) 
    def mysum(self):
        return self.a+self.b 
    def mysub(self):
        return self.a-self.b 
    def mymul(self):
        return self.a*self.b
    def mydiv(self):
        return self.a/self.b
    def mymod(self):
        return self.a%self.b
    def myexp(self):
        return self.a**self.b
casio=Calculator()
casio.getValues()
casio.putValues()
print("______________________________________")
print("MENU")
print("____________________________________")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.Floordiv")
print("6.Mod")
print("7.exp")
print("______________________________________")
x=int(input("Select on option from the above"))
print("__________________________________")
if(x==1):
    print("Add=",casio.mysum())
elif(x==2):
    print("Sub=",casio.mysub()) 
elif(x==3):
    print("Mul=",casio.mymul()) 
elif(x==4):
    print("Div=",casio.mydiv())
elif(x==5):
    print("Floordiv=",casio.mydiv())
elif(x==6):
    print("Mod=",casio.mymod())
elif(x==7):
    print("Exp=",casio.myexp())
else:
    print("Invalid option")              