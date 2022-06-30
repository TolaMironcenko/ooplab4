
class Fraction:
    def __init__(self, a, b):
        self.A = a
        self.B = b
        self.cut()

    def cut(self):
        if self.B < 0:
            self.A *= -1
            self.B *= -1
        for i in range(1, self.__B):
            if (self.A % i == 0) and (self.B % i == 0):
                self.A = int(self.A/i)
                self.B = int(self.B/i)

    def __str__(self):
        self.cut()
        if self.A >= self.B:
            if self.A % self.B == 0:
                return '{}'.format(self.A//self.B)
            else:
                return '{} and {}/{}'.format(self.A // self.B, self.A % self.B, self.B)
        else:
            return '{}/{}'.format(self.A, self.B)

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
        self.cut()
        return self

    def __sub__(self, other):
        if self.B == other.B:
            return Fraction(self.A-other.A, self.B)
        else:
            return Fraction(self.A*other.B-other.A*self.B, self.B*other.B)

    def __isub__(self, other):
        if self.B == other.B:
            self.A -= other.A
        else:
            self.A = self.A*other.B-other.A*self.B
            self.B *= other.B
        self.cut()
        return self

    def __mul__(self, fraction):
        return Fraction(self.A*fraction.A, self.B*fraction.B)

    def __truediv__(self, other):
        return Fraction(self.A*other.B, self.B*other.A)
