from fraction import Fraction


def print_hi():
    number1 = Fraction(3, 2)
    number1.display()
    number2 = Fraction(1, 2)
    number2 = number2*number1
    print(number2)


if __name__ == '__main__':
    print_hi()
