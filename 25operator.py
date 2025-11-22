class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # Adding 2 objects
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def __str__(self):
        return f"{self.a} + {self.b}i"
obj1 = Complex(4, 2)
obj2 = Complex(11, 3)
result = obj1 + obj2
print(result)