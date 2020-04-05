__author__ = 'Pavlo Chaikovskyi 125B'

import random
import sys
import time
from functools import reduce
import pickle

class InvalidMethod(Exception): pass
class InvalidArguments(Exception): pass

class capsule():
    def __init__(self, init_method, *args, **kwargs):
        if init_method == 0:
            if len(kwargs) == 3:
                self.array = self.init_array(values=kwargs['values'], text=kwargs['text'], array_type=kwargs['array_type'])
            else:
                raise InvalidArguments("Amount of args is not valid.")
        elif init_method == 1:
            if len(args) == 3:
                self.array = self.rand_array(*args)
            else:
                raise InvalidArguments("Amount of args is not valid.")
        elif init_method == 2:
                self.array = kwargs['array']
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
        print(f'ARRAY : {array}')
        return array

    def rand_array(self, left, right, len):
        array = []
        for i in range(len):
            array.append(random.randint(left, right))
        print(f'ARRAY : {array}')
        return array

    def getArray(self):
        return self.array

    def count(self, str):
        key = lambda x: eval(str)
        j = len(tuple(filter(key, self.array)))
        return j

    def sum(self, str='x'):
        key = lambda x: eval(str)
        j = sum(tuple(filter(key, self.array)))
        return j

    def product(self, str):
        key = lambda x: eval(str)
        j = reduce(lambda x, y: x * y, filter(key, self.array))
        return j

    def avg(self):
        return sum(self.array)/len(self.array)

    def min(self):
        return min(self.array)

    def max(self):
        return max(self.array)

    def find(self, value):
        massive = self.array
        low = 0
        high = len(massive) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = massive[mid]
            if guess == value:
                return mid
            if guess > value:
                high = mid - 1
            if guess < value:
                low = mid + 1
        return -1