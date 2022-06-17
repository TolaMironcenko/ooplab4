
class Fraction:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def display(self):
        if self.A >= self.B:
            if self. A % self.B == 0:
                print(self. A // self.B)
            else:
                print(self.A // self.B, " and ", self. A % self.B, '/', self.B)
        else:
            print(self.A, '/', self.B)

    def __mul__(self, fraction):
        self.A *= fraction.A
        self.B *= fraction.B


