class ComplexNumbers:
    i = (-1)**(1/2)

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.num = a + b * ComplexNumbers.i

    def __add__(self, other):
        return ComplexNumbers((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return ComplexNumbers((self.a * other.a - self.b * other.b), (self.a * other.b + other.a * self.b))

    def __str__(self):
        return f'{self.a} + {self.b}i'


n1 = ComplexNumbers(2, 4)
n2 = ComplexNumbers(1, 3)
n3 = n1 + n2
n4 = n1 * n2
print(n3)
print(n4)
