from fraction import Fraction


def print_hi():
    number1 = Fraction(2, 3)
    print(number1)
    number2 = number1
    print(number2)
    number2 *= number1
    print(number2)
    number3 = number1 + number2
    print(number3)


if __name__ == '__main__':
    print_hi()
