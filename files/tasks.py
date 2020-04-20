__author__ = 'Pavlo Chaikovskyi 125B'

import sys
from .capsule_class import capsule
import random

def main(func):
    """
    Comment for common things in tasks.
    I've created a capsule class, that you can check in capsule_class.py

    There i made some processing stuff to make calling,
    initializing arrays faster and easier (I'll be not saying this in few weeks))

    So, there three common constructions in tasks :

    1) array = capsule(0, values=5, text='Enter 5 values separated by gap', array_type=int)
    1st argument - 0, means that we using init_array function to initialize array.
    Init_array takes values to array from user input. It asks such args as - values, text, array_type
    Values - amount of variables that we want to take from user.
    Text - want we want to see in input(), condition if you want.
    Array_type - type of each element of array, can be int, float, str.

    2) array = capsule(1, -10, 10, 8)
    1st argument - 1, means that we using rand_array function to initialize array.
    It accepts such arguments - left, right, length (len), and in such order as in example.
    Left - minimum value function randint, elements of array cannot be less that is.
    Right works the same, but it's maximum value of randint.
    Len - length of array, how much elements in could have.

    3) array = capsule(2, array=[17, 14, 13, 12, 12, 13, 13, 11, 10, 10, 15, 17])
    1st argument - 2, means that we just passing already prepared array to deal with.
    Needed, if you want to work with instance methods.

    So, that's how tasks run instance initialization.

    After that, we can use capsule's methods, to deal with arrays.
    More precise you can read in capsule_class.py.
    Here few examples  -
    getArray, philter, count, sum, product, avg.
    getArray just gives us an list of elements.
    Philter - filters elements with needed instructions, like
    elements should be less than 0 (x < 0) or something like that.
    Count works same, but it counts elements, that correspond condition passed in,
    like, count please elements that divides by 3, or less that 0, etc.
    Sum, product - calcs sum and product of elements that corrensponding
    passed conditions. By default these methods processing whole array.
    """


    def t1():
        iarray = capsule(0, values=5, text='Enter 5 values separated by gap', array_type=int).avg()
        print(f"Array's avg - {iarray}")

    def t2():
        array = capsule(0, values=5, text='Enter 5 values separated by gap', array_type=int).getArray()
        [print(f'Root of {i} - {i ** 0.5}') for i in array]
        [print(f'Square of {i} - {i * i}') for i in array]

    def t3():
        array = capsule(0, values=5, text='Enter 5 second names separated by gap', array_type=str).getArray()
        for i in array[::-1]:
            print(i.capitalize())

    def t4():
        array = capsule(0, values=5, text='Enter 5 second names separated by gap', array_type=str).getArray()
        array_first_letters = ''.join([i[0] for i in array])
        print('Enter arbitrary letter')
        for x in sys.stdin:
            x = x[0].capitalize()
            if array_first_letters.find(x) != -1:
                print(array[array_first_letters.find(x)])
            else:
                print("There's no such words that start on this letter")

    def t5():
        A = capsule(1, -100, 100, 7).getArray()
        for i in A:
            print(i, ', doubled : ', i*2)

    def t6():
        A = capsule(1, -10, 10, 8).sum()
        print('Amount of negative nums :' ,A)

    def t7():
        A = capsule(1, -20, 10, 12).getArray()
        for i in A:
            if i < 0:
                print('0' + ', ', end="", sep="")
            else:
                print(f'{i}' + ', ', end="", sep="")
        print('\nThat"s all')

    def t8():
        A = capsule(1, -15, 30, 15).getArray()
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
        A = capsule(1, -11, 0, 10).count('x == -10')
        print(A)

    def t11():
        # придатна температура +- 22 градуси
        A = capsule(1, 15, 30, 10).count("x >= 22")
        print(A)

    def t12():
        A = capsule(1, -20, 10, 10)
        print(A.count(f"x > {A.avg()}"))

    def t13():
        A = capsule(1, 0, 10000, 15)
        print(min(A))

    def t14():
        t = tuple(range(1, 11))
        for i in t:
            h = round(9.81*(i*i)/2, 2)
            print(h, end=", ")
        print()

    def t15():
        A = capsule(1, 100, 200, 10).sum("x%2 == 0")
        print(A)

    def t16():
        A = capsule(1, 10, 50, 15).product("x%7 == 0")
        print(A)

    def t17():
        A = capsule(1, 100, 200, 20).getArray()
        filtered = 0
        for i in range(len(A)):
            if i%2 != 1:
                filtered += A[i]
        print(filtered)

    def t18():
        A = capsule(1, values=10, text='Enter 10 values', init_method=int).product("x < 0")
        print(A)

    def t19():
        A = capsule(1, 100, 200, 20).sum("x%2 == 3")
        print(A)

    def t20():
        n = int(input("Enter value : "))
        A = capsule(1, 50, 100, 20).sum(f"x > {n}")
        print(A)

    def t21():
        n = int(input("Enter value : "))
        A = capsule(1, 50, 100, 20).product(f"x < {n}")
        print(A)

    def t22():
        A = capsule(1, 5, 500, 10).product("x % 3 == 0 and x % 9 == 0")
        print(A)

    def t23():
        A = capsule(1, 150, 300, 20)
        print(A.sum(f"x < {A.avg()}"))

    def t24():
        A = capsule(1, 500, 1000, 30).sum('x%5 == 0 and x%8 == 0')
        print(A)

    def t25():
        A = capsule(1, 10, 100, 10).product('x % 5 == 0')
        print(A)

    def t26():
        T = capsule(0, values=6, text="Enter 6 measurements of temperature (float) : ", array_type=float)
        print(f"Min : {T.min()}, Max : {T.max()}, Avg : {T.avg()}")

    def t27():
        A = capsule(2, array=[17, 14, 13, 12, 12, 13, 13, 11, 10, 10, 15, 17])
        print(f"Середня у-ть опадів : {A.avg()}")
        print(f"Загальна к-ть : {A.sum()}")
        print(f"Посушливі місяці : {A.count('x > 30')}")
        print(f"Найпосушливий місяць : {A.find(A.max()) + 1}")

    def t28():
        A = capsule(1, -1000, 1000, 1000).count("x%2 == 0")
        print(A)

    def t29():
        a = int(input("Enter some number : "))
        A = capsule(1, -1000, 1000, 1000)
        Afind = A.find(a)
        Aarray = A.getArray()
        A2 = capsule(2, array=Aarray[0:Afind]).count("x%2 == 0")
        print(A2)

    def t30():
        A = capsule(1, -1000, 1000, 1000)
        A2 = capsule(2, array=A.getArray()[0:A.min()]).avg()
        print(A2)

    def t31():
        A = capsule(1, -1000, 1000, 200)
        A.philter("x in range(-2,11)")
        A_avg = A.avg()
        print(A_avg)

    def t32():
        t = False
        A = capsule (1, -1000, 1000, 200)
        A.philter("x%2 == 0 and x < 0")
        if len(A.getArray()) > 0:
            t = True
        print(t)

    def t33():
        A = capsule (1, -20, 20, 10)
        print(A.product('x > 0'))

    def t34():
        n = int(input("Array's length? : "))
        A = capsule(0, values=n, text=f'Enter {n} values separated by gap for first array', array_type=int).getArray()
        A2 = capsule(0, values=n, text=f'Enter {n} values separated by gap for second array', array_type=int).getArray()
        A3 = []
        for i,j in zip(A, A2):
            A3.append(i*j)
        print('Result array : ')
        print(A3)

    def t35():
        equal = 'are'
        A = capsule(0, values=10, text='Enter 10 values separated by gap', array_type=int).getArray()
        A2 = capsule(2, array=A).sort()
        print(f'Sorted ARRAY : {A2}')
        for i,j in zip(A, A2):
            if i != j:
                equal = 'are not'
                break
        print('Arrays ' + equal +  ' equal')

    def t36():
        A = capsule (0, values=10, text='Enter 10 values separated by gap', array_type=int).sum('x > 0')
        print(A)

    def t37():
        A = capsule (0, values=10, text='Enter 10 values separated by gap', array_type=int)
        print(A.sort(b00l=False))

    def t38():
        pivdViter = capsule (1, 0, 20, 30)
        print(pivdViter.count('x > 8'))


    def t39():
        opd = capsule (1, 0, 20, 10)
        print(opd.sum('x > 15')) #більше 15мм

    def t40():
        n = 20
        A = capsule (1, -100, 100, n)
        zero_position = A.find (0)
        if zero_position == -1:
            zero_position = random.randint(0, n)
            A.array.insert(zero_position, 0)
            print('Zero inserted in the position ' + str(zero_position))
        A.array = A.array[0:zero_position]
        print(A.sum('x%2==0'))

    def t41():
        t = False
        a = int(input("Enter a : "))
        A = capsule (1, -10 - a, a + 10, 50)
        max = (A.max(), A.count(a))
        if max[1] == 1 and max[0] <= a:
            t = True
        print(t)

    def t42():
        a = int (input ("Enter a : "))
        A = capsule (1, -10 - a, a + 10, 50).count(f'x*x < {a}*x < x')
        print(A)

    def t43():
        a, b = map(int, input().split())
        w = False
        A = capsule (1, -10 - a - b, 10 + a + b, 50).count(f"x%{a} == 0 and x%{b} != 0")
        if A > 0:
            w = True
        print(w)

    def t44():
        A = capsule (2, array=list(range(100)))
        Ac = A.count(f'{A.array}.index(x) == x and x%3==0')
        print(Ac)

    def t45():
        R = int(input("R : "))
        length = []
        for i in range (5):
            length.append((R ** 2 - ((R / 5) * (4 - i)) ** 2)**0.5)
        for i in range(len(length) - 2, -1, -1):
            length.append(length[i])
        print(length)

    def t46():
        n = int(input("Amount of goods : "))
        A = capsule(0, values=n, text=f'Enter {n} values separated by gap', array_type=str)
        if A.count(A.array[0]) > 1:
            A.remove(A.array[0])
        print(A)

    def t47():
        A = capsule (1, -100, 100, 20)
        max = A.max()
        max_index = A.find(max)
        A.array.insert(max_index - 1, max_index)
        print(A.getArray())

    def t48():
        n = int (input ("Amount of second names : "))
        A = capsule (0, values=n, text=f'Enter {n} names separated by gap', array_type=str).getArray()
        n = len (A) - 1
        for i in range (n // 2):
            A[i], A[n - i] = A[n - i], A[i]
        print(A)

    def t49():
        # both tables will be represented as dictionary
        # where keys is services, values - prices
        # services = {"Coffee":100, "Tea":}
        G = int(input("G : "))
        services = {input("Enter service"):random.randint(1,1000) for i in range(50)}
        for i in services.keys():
            if services[i] != G:
                del services[i]
            else:
                break
        else:
            print("Okay, im sorry")
        print(services)

    def t50():
        N = int (input ("N, should be 6 digits : "))
        A = capsule(1, 100000, 999999, 100).getArray()
        print(N) if (N in A) else print("No")

    def t51():
        A = capsule (1, -100, 100, 100).getArray ()
        for i in A:
            if (A.index(i) + 10) == i:
                print(i, end=", ")
        else:
            print("There's no such nums")

    def t52():
        A = capsule (1, 0, 100, 100).getArray()
        newArray = [i for i in A[::2]]
        _max = max(newArray)
        print(f'Max element that has even position : {_max}', end="")
        if newArray.count(_max) > 1:
            print(f", but there's more like it than 1.")
        else:
            print(f".")

    def t53():
        n = int(input("N : "))
        X = [random.choice((0, 1, 5)) for i in range(n)]
        print(sorted(X))

    def t54():
        A = capsule (1, 0, 50, 20).getArray()
        if (len(A) - len(set(A))) != 0:
            print("There is few similar elements")
        else:
            print ("There is not any similar elements")

    def t56():
        r = False
        #a = [random.randint(0, 10) in range(100)]
        a = input("Enter array:\n").split()
        value, counter = a[0], 0
        for i in a:
            if i == value:
                counter += 1
            else:
                value = i
            if counter == 3:
                r = True
                break
        print(r)

    def t57():
        names = map(str.strip, """Johnathan Hardy
        Audrey Hopkins
        Minnie Johnson
        Jody Morris
        Cecelia Henderson
        Shannon Craig
        Dixie Becker
        Sergio Wood
        Elmer Douglas
        Rene Abbott""".split('\n'))
        names = list(names)
        pay = [random.randint(5700, 36666) for i in range(10)]
        avg_pay = []
        print(f'Зарплата найменш відхиляється від середини y {avg_pay_less_dev}')
        max_pay = []
        print(name_pay)

    def t58():
        A = capsule (0, values=10, text='Enter 10 values separated by gap', array_type=int)
        temp = 0
        for i in A.getArray():
            if A.count(i) > temp:
                temp = A.count(i)
        print(temp)

    def t59():
        A = capsule (0, values=10, text='Enter 10 values separated by gap', array_type=int)
        print(len(set(A.getArray())))


    def t60():
        #A = capsule(1, -5, 5, 10).getArray()
        A = list(capsule (0, values=10, text='Enter 10 values separated by gap', array_type=int).getArray())
        A.append('garbage_value')
        count = {'counter': [], 'temp_count': 0}

        for i in range(len(A) - 1):

            if A[i] != A[i + 1]:
                count['counter'].append(count['temp_count'])
                count['temp_count'] = 0

            if A[i] == A[i + 1]:
                count['temp_count'] += 1

        print(max(count['counter']))

    if func != None:
        return eval(f"t{func}")