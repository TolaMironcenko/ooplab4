from fraction import Fraction


def main():
    number1 = Fraction(183, 18)
    number2 = Fraction(1, 3)
    number2 /= number1
    print(number1)


if __name__ == '__main__':
    main()
