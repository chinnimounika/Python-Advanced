class calculator:
    def PutValues(self):
        print("Value of a=",self.a)
        print("Value of b=",self.b)
    def add(self):
        return self.a+self.b
casio=calculator()
casio.a=5
casio.b=3
casio.PutValues()
print("Sum=",casio.add())