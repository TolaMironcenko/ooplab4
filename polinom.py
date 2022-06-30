from itertools import count
from termcolor import cprint

DEGREESTR = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹"
}


class Polinom:

    def __init__(self, n: int, array: list):
        try:
            if len(array) == n+1:
                self.array = array
                self.n = n
            else:
                cprint('Error: Длинна массива array должна быть равной n+1', 'red')
        except Exception as e:
            cprint(str(e)+'\nError: array должен быть массивом длинна которого должна быть равной n+1', 'red')

    def __str__(self):
        result = ''
        for i in range(self.n+1):
            if i == 0:
                if self.array[0] == 0:
                    pass
                else:
                    result += ' {} '.format(self.array[i])
                    if i != self.n and self.array[i+1] != 0 and self.array[i+1] > 0:
                        result += '+'
                    elif i != self.n and self.array[i+1] != 0 and self.array[i+1] < 0:
                        result += '-'   
            elif i == 1 and self.array[i] != 0:
                if self.array[i] > 0:
                    result += ' {}·x '.format(self.array[i])
                else: 
                    result += ' {}·x '.format(-self.array[i])
                if i != self.n and self.array[i+1] != 0 and self.array[i+1] > 0:
                    result += '+' 
                elif i != self.n and self.array[i+1] != 0 and self.array[i+1] < 0:
                    result += '-' 
            elif self.array[i] != 0:
                if self.array[i] > 0:
                    result += ' {}·x{} '.format(self.array[i], DEGREESTR[str(i)])
                else:
                    result += ' {}·x{} '.format(-self.array[i], DEGREESTR[str(i)])
                if i < self.n and self.array[i+1] != 0 and self.array[i+1] > 0:
                    result += '+'
                elif i < self.n and self.array[i+1] != 0 and self.array[i+1] < 0:
                    result += '-'
        return result

    def __add__(self, other):
        # if other.n >= self.n:
        #     result_n = other.n
        #     result_array = [0]*(result_n+1)
        #     for i in range(self.n+1):
        #         result_array[i] = self.array[i] + other.array[i]
        #     result_array[result_n] = other.array[result_n]
        # else:
        #     result_n = self.n
        #     result_array = [0] * (result_n + 1)
        #     for i in range(other.n + 1):
        #         result_array[i] = self.array[i] + other.array[i]
        #     result_array[result_n] = self.array[result_n]

        res = self
        res+=other
        return  res# Polinom(result_n, result_array)

    def __iadd__(self, other):
        if other.n >= self.n:
            result_n = other.n
            result_array = [0]*(result_n+1)
            for i in range(self.n+1):
                result_array[i] = self.array[i] + other.array[i]
            result_array[result_n] = other.array[result_n]
            self.n = result_n
            self.array = result_array
        else:
            result_n = self.n
            result_array = [0] * (result_n + 1)
            for i in range(other.n + 1):
                result_array[i] = self.array[i] + other.array[i]
            result_array[result_n] = self.array[result_n]
            self.n = result_n
            self.array = result_array
        return self

    def __sub__(self, other):
        if other.n > self.n:
            result_n = other.n
            result_array = [0]*(result_n+1)
            for i in range(self.n+1):
                result_array[i] = self.array[i] - other.array[i]
            result_array[result_n] = -other.array[result_n]
            return Polinom(result_n, result_array)
        elif self.n == other.n:
            result_array = [0]*(self.n+1)
            for i in range(self.n+1):
                result_array[i] = self.array[i] - other.array[i]
            return Polinom(self.n, result_array)
        else:
            result_n = self.n
            result_array = [0] * (result_n + 1)
            for i in range(other.n + 1):
                result_array[i] = self.array[i] - other.array[i]
            result_array[result_n] = self.array[result_n]
            return Polinom(result_n, result_array)

    def __isub__(self, other):
        if other.n > self.n:
            result_n = other.n
            result_array = [0]*(result_n+1)
            for i in range(self.n+1):
                result_array[i] = self.array[i] - other.array[i]
            result_array[result_n] = -other.array[result_n]
            self.n = result_n
            self.array = result_array
        elif self.n == other.n:
            result_array = [0]*(self.n+1)
            for i in range(self.n+1):
                result_array[i] = self.array[i] - other.array[i]
            self.array = result_array
        else:
            result_n = self.n
            result_array = [0] * (result_n + 1)
            for i in range(other.n + 1):
                result_array[i] = self.array[i] - other.array[i]
            result_array[result_n] = self.array[result_n]
            self.n = result_n
            self.array = result_array
        return self

    def __mul__(self, other):
        newn = self.n + other.n
        arr = [0]*(newn+1)
        for i in range(self.n+1):
            for j in range(other.n+1):
                arr[i+j] = self.array[i] * other.array[j] + arr[i+j]

        return Polinom(newn, arr)

    def __truediv__(self, other):
        if self.n < other.n:
            cprint('Error: Нельзя делить меньший полином на больший', 'red')
            return Polinom(-1, [])
        count = self.n - other.n
        arr = [0]*(count+1)
        for i in range(self.n, other.n, -1):
            arr[count] = self.array[i] / other.array[other.n]
            for j in range(other.n):
                self.array[i-j] -= other.array[other.n-j] * arr[count]
            count -= 1
        return Polinom(self.n-other.n, arr)
