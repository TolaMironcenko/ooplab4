from fraction import Fraction
from polinom import Polinom
from termcolor import cprint


def main():
    pol1 = Polinom(3, [2, 4, 6, 8])
    pol2 = Polinom(2, [1, 3, 5])
    print(pol1, pol2, sep='\n')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit('byby')
    except Exception as e:
        cprint('Error: ' + str(e), 'red')
