__author__ = 'Pavlo Chaikovskyi 125B'

import random
import sys
import time
from functools import reduce
import pickle

class capsule(list):

    def __init__(self, init_method):
        if init_method == 1:


    @staticmethod
    def init_array(values=5, text='Enter 5 values separated by gap', array_type=int):
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

    @staticmethod
    def rand_array(left, right, len):
        array = []
        for i in range(len):
            array.append(random.randint(left, right))
        print(f'ARRAY : {array}')
        return array

    @staticmethod
    def count(array, key = lambda x: x):
        j = sum(filter(key, array))
        return j

def main(func):

    def t1():
        array = capsule.init_array(values=5, text='Enter 5 values separated by gap', array_type=int)

        print(*array, sep=", ")
        print(f"Array's avg - {sum(array)/len(array)}")

    def t2():
        array = capsule.init_array(values=5, text='Enter 5 values separated by gap', array_type=int)
        [print(f'Root of {i} - {i ** 0.5}') for i in array]
        [print(f'Square of {i} - {i * i}') for i in array]

    def t3():
        array = capsule.init_array(values=5, text='Enter 5 second names separated by gap', array_type=str)
        for i in array[::-1]:
            print(i.capitalize())
        #print(*array[::-1], sep="\n")

    def t4():
        array = capsule.init_array(values=5, text='Enter 5 second names separated by gap', array_type=str)
        array_first_letters = ''.join([i[0] for i in array])
        print('Enter arbitrary letter')
        try:
            for x in sys.stdin:
                x = x[0].capitalize()
                if array_first_letters.find(x) != -1:
                    print(array[array_first_letters.find(x)])
                else:
                    print("There's no such words that start on this letter")
        except EOFError:
            print('Goodbye...')

    def t5():
        A = capsule.rand_array(-100, 100, 7)
        for i in A:
            print(i, ', doubled : ' ,i*2)

    def t6():
        A = capsule.rand_array(-10, 10, 8)
        print(*A, sep=", ")
        print('Amount of negative nums :' ,sum(1 for i in A if i < 0))

    def t7():
        A = capsule.rand_array(-20, 10, 12)
        print(*A, sep=', ')
        for i in A:
            if i < 0:
                print('0' + ', ', end="", sep="")
            else:
                print(f'{i}' + ', ', end="", sep="")
        print('That"s all')

    def t8():
        A = capsule.rand_array(-15, 30, 15)
        print(*A, sep=', ')
        makx = max(A)
        print(makx, A.index(makx))

    def t9():
        while True:
            try:
                delta_temp = int(input('How much degrees does temperature gets lower every hour : '))
                default_temp = int(input('Default temperature for 8 o"clock : '))
            except (ValueError, TypeError):
                print('try again...')
            else:
                break
        for i in range(8, 20 + 1):
            default_temp -= delta_temp
            if default_temp < 0:
                print(i)
                break
        else:
                print('Never...')

    def t10():
        A = capsule.rand_array(-11, 0, 10)
        print(A.count(-10))

    def t11():
        A = capsule.rand_array(15, 30, 10)
        # придатна температура +- 22 градуси
        s = tuple(filter(lambda x: x >= 22, A))
        print(len(s))

    def t12():
        A = capsule.rand_array(-20, 10, 10)
        avg = sum(A)//len(A)
        s = tuple(filter(lambda x: x >= avg, A))
        print(len(s))

    def t13():
        A = capsule.rand_array(0, 10000, 15)
        print(min(A))

    def t14():
        t = tuple(range(1, 11))
        for i in t:
            h = round(9.81*(i*i)/2, 2)
            print(h, end=", ")
        print()

    def t15():
        A = capsule.rand_array(100, 200, 10)
        print(sum(filter(lambda x: x%2 == 0, A)))

    def t16():
        A = capsule.rand_array(10, 50, 15)
        reduced = reduce(lambda x, y: x*y, filter(lambda x: x % 2 == 0, A))
        print(reduced)

    def t17():
        A = capsule.rand_array(100, 200, 20)
        filtered = 0
        for i in range(len(A)):
            if i%2 != 1:
                filtered += A[i]
        print(filtered)

    def t18():
        A = capsule.init_array(values=10, text='Enter 10 values')
        reduced = reduce(lambda x, y: x * y, filter(lambda x: x < 0, A))
        print(reduced)

    def t19():
        A = capsule.rand_array(100, 200, 20)
        filtered = filter(lambda x: x%2 == 3, A)
        print(sum(filtered))

    def t20():
        n = int(input("Enter value : "))
        A = capsule.rand_array(50, 100, 20)
        filtered = filter(lambda x: x > n, A)
        print(sum(filtered))

    def t21():
        n = int(input("Enter value : "))
        A = capsule.rand_array(50, 100, 20)
        filtered = filter(lambda x: x < n, A)
        print(sum(filtered))

    def t22():
        A = capsule.rand_array(5, 500, 10)
        reduced = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0 and x % 9 == 0, A))
        print(reduced)

    def t23():
        A = capsule.rand_array(150, 300, 20)
        avg = sum(A)/len(A)
        filtered = filter(lambda x: x < avg, A)
        print(sum(filtered))

    def t24():
        A = capsule.rand_array(500, 1000, 30)
        filtered = filter(lambda x: x%5 == 0 and x%8 == 0, A)
        print(sum(filtered))

    def t25():
        A = capsule.rand_array(10, 100, 10)
        reduced = reduce(lambda x, y: x * y, filter(lambda x: x % 5 == 0, A))
        print(reduced)

    def t26():
        T = capsule.init_array(6, text="Enter 6 measurements of temperature (float) : ", array_type=float)
        print(f"Min : {min(T)}, Max : {max(T)}, Avg : {sum(T)/len(T)}")

    def t27():
        pass

    def t28():
        A = capsule.rand_array(-1000, 1000, 1000)

    if func != None:
        return eval(f"t{func}")

if __name__ == '__main__':

    while True:
        try:
            print()
            i = input('Pick the task : ')

            with open('conditions.bin', 'rb') as f:
                CONDITIONS = pickle.load(f, encoding='utf8')
            print(CONDITIONS[int(i) - 1])

            a = main(func=i)
            a()
        except (NameError, ValueError, IndexError):
            print("Pick the task, again")
        except EOFError:
            print("Goodbye")
            exit()

