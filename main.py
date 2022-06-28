from fraction import Fraction
from polinom import Polinom
from termcolor import cprint


def main():
    pol1 = Polinom(2, [1, 5, 2])
    pol2 = Polinom(3, [6, 1, 4, 3])
    print(pol1, pol2, sep='\n')
    print(pol2/pol1)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit('byby')
    except Exception as e:
        cprint('Error: ' + str(e), 'red')
