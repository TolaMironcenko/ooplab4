from fraction import Fraction
from polinom import Polinom


def main():
    pol1 = Polinom(3, [4, 3, 2, 9])
    pol2 = Polinom(4, [1, 2, 3, 4, 5])
    print(pol1, pol2, sep='\n')
    print(pol1-pol2)
    pol1 -= pol2
    print(pol1)


if __name__ == '__main__':
    main()
