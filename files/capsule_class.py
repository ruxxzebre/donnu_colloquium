__author__ = 'Pavlo Chaikovskyi 125B'

import random
import sys
import time
from functools import reduce
import pickle

# here i just made few exceptions to call if needed
class InvalidMethod(Exception): pass
class InvalidArguments(Exception): pass

class capsule():
    """
    So, when we initialize an instance of capsule class, we should pass an arguments.
    First argument will be like a flag, what we want to do :
        1) Initialize array that takes input from user
        2) Init. array with random numbers.
        3) Just pass array into argument, and use class methods as well.

    *args, **kwargs - it's arguments, that __init__ method passes to init_array or rand_array.
    init_array - is array, that takes user input, with text, type, and amount or variables.
    rand_array - just making an array of numbers or letters with fixed length.
    """

    def __init__(self, init_method, *args, **kwargs):
        if init_method == 0:
            if len(kwargs) == 3:
                self.array = self.init_array(values=kwargs['values'], text=kwargs['text'], array_type=kwargs['array_type'])
            else:
                raise InvalidArguments("Amount of args is not valid.")
            print (f'ARRAY : {self.array}')
        elif init_method == 1:
            if len(args) == 3:
                self.array = self.rand_array(*args)
            else:
                raise InvalidArguments("Amount of args is not valid.")
            print (f'ARRAY : {self.array}')
        elif init_method == 2:
            self.array = kwargs['array']
            print (f'ARRAY : {self.array}')
        else:
            raise InvalidMethod("Invalid initialization method")


    def init_array(self, values=5, text='Enter 5 values separated by gap', array_type=int):
        array = None
        while True:
            try:
                if array_type != str:
                    array = tuple(map(array_type, input(text + '\n').split()))
                else:
                    array = tuple(input(text + '\n').split())
            except ValueError:
                continue
            else:
                if len(array) == values:
                    break
        return array

    def rand_array(self, left, right, length, type=int):
        array = []
        random_func = None
        string = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
        if type == int:
            random_func = random.randint
        elif type == float:
            random_func = random.random
        elif type == str:
            random_func = random.choice
        if type in (int, float):
            for i in range(length):
                array.append(random_func(left, right))
        elif type == str:
            for i in range (length):
                array.append(random_func(string))
        return array

    #@property
    def getArray(self):
        # simple getter
        return self.array

    #getArray, philter, count, sum, product, avg

    def setArray(self):
        pass

    def philter(self, str, returnn = False):
        key = lambda x: eval (str)
        j = tuple (filter (key, self.array))
        self.array = j
        if returnn == True:
            return self.array

    def count(self, str, mode=0, type=str):
        if mode == 0:
            key = lambda x: eval(str)
            j = len(tuple(filter(key, self.array)))
            return j
        elif mode == 1:
            var = type(str)
            result = self.array.count(var)
            return result

    def sum(self, str='x'):
        key = lambda x: eval(str)
        j = sum(tuple(filter(key, self.array)))
        return j

    def product(self, str):
        key = lambda x: eval(str)
        j = reduce(lambda x, y: x * y, filter(key, self.array))
        return j

    def avg(self):
        if len(self.array) > 0:
            return sum (self.array) / len (self.array)
        return "Dividing by ZERO"

    def min(self):
        return min(self.array)

    def max(self):
        return max(self.array)

    def sort(self, str='x', b00l=True):
        key = lambda x: eval (str)
        return sorted(self.array, key=key, reverse=b00l)

    def remove(self, value):
        while value in self.array:
            self.array.remove(value)


    @staticmethod
    def stfind(value, array):
        low = 0
        high = len (array) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = array[mid]
            if guess == value:
                return mid
            if guess > value:
                high = mid - 1
            if guess < value:
                low = mid + 1
        return -1

    def find(self, value):
        return capsule.stfind(value, self.array)

