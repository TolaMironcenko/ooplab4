from fraction import Fraction
from polinom import Polinom


def main():
    pol1 = Polinom(2, [1,5,2])
    pol2 = Polinom(3, [6,1,4,3])
    print(pol1, pol2, sep='\n')
    print(pol1+pol2)
    print(pol1-pol2)


if __name__ == '__main__':
    main()
