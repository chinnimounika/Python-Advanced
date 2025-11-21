class Calculator:
    def __init__(self):      # default constructor
        self.a = 3
        self.b = 5
    def putvalues(self):
        print("Value of a =", self.a)
        print("Value of b =", self.b)
    def mysum(self):
        return self.a + self.b
c = Calculator()
c.putvalues()
print("Sum =", c.mysum())






