
class Fraction:
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def __str__(self):
        if self.A >= self.B:
            if self. A % self.B == 0:
                return '{}'.format(self.A//self.B)
            else:
                return '{} and {}/{}'.format(self.A // self.B, self. A % self.B, self.B)
        else:
            return '{}/{}'.format(self.A, self.B)
        return

    def __add__(self, other):
        if self.B == other.B:
            return Fraction(self.A+other.A, self.B)
        else:
            return Fraction(self.A*other.B+other.A*self.B, self.B*other.B)

    def __iadd__(self, other):
        if self.B == other.B:
            self.A += other.A
        else:
            self.A = self.A*other.B+other.A*self.B
            self.B *= other.B
        return self

    def __mul__(self, fraction):
        return Fraction(self.A*fraction.A, self.B*fraction.B)

