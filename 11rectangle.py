class Rectangle:
    def getValues(self):
        self.l=int(input("Enter Length:"))
        self.b=int(input("Enter Breadth:"))
    def putValues(self):
        print("Length=",self.l) 
        print("Breadth=",self.b) 
    def carea(self):
        return self.l*self.b   
R=Rectangle()
R.getValues()
R.putValues() 
print("Area of Rectangle=",R.carea())  