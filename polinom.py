from termcolor import cprint


class Polinom:

    def __init__(self, n: int, array: list):
        try:
            if len(array) == n+1:
                self.array = array
                self.n = n
                self.degreestr = {
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
            else:
                cprint('Error: Длинна массива array должна быть равной n', 'red')
        except Exception as e:
            cprint(str(e)+'\nError: array должен быть массивом длинна которого должна быть равной n', 'red')

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
            elif i == 1 and self.array[i] != 0:
                result += ' {}·x '.format(self.array[i])
                if i != self.n and self.array[i+1] != 0 and self.array[i+1] > 0:
                    result += '+'
            elif self.array[i] != 0:
                result += ' {}·x{} '.format(self.array[i], self.degreestr[str(i)])
                if i != self.n and self.array[i+1] != 0 and self.array[i+1] > 0:
                    result += '+'
        return result

    def __add__(self, other):
        if other.n >= self.n:
            result_n = other.n
            result_array = [0]*(result_n+1)
            for i in range(self.n+1):
                result_array[i] = self.array[i] + other.array[i]
            result_array[result_n] = other.array[result_n]
        else:
            result_n = self.n
            result_array = [0] * (result_n + 1)
            for i in range(other.n + 1):
                result_array[i] = self.array[i] + other.array[i]
            result_array[result_n] = self.array[result_n]
        return Polinom(result_n, result_array)

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