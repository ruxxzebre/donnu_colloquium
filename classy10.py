__author__ = 'Pavlo Chaikovskyi 125B'

import sys
import pickle
from donnu_colloquium.capsule.capsule_class import capsule

def main(func):

    def t1():
        iarray = capsule(0, values=5, text='Enter 5 values separated by gap', array_type=int)
        array = iarray.getArray()
        print(f"Array's avg - {sum(array)/len(array)}")

    def t2():
        array = capsule(0, values=5, text='Enter 5 values separated by gap', array_type=int).getArray()
        [print(f'Root of {i} - {i ** 0.5}') for i in array]
        [print(f'Square of {i} - {i * i}') for i in array]

    def t3():
        array = capsule(0, values=5, text='Enter 5 second names separated by gap', array_type=str).getArray()
        for i in array[::-1]:
            print(i.capitalize())
        #print(*array[::-1], sep="\n")

    def t4():
        array = capsule(0, values=5, text='Enter 5 second names separated by gap', array_type=str).getArray()
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
        A = capsule(1, -100, 100, 7).getArray()
        for i in A:
            print(i, ', doubled : ' ,i*2)

    def t6():
        A = capsule(1, -10, 10, 8).getArray()
        print('Amount of negative nums :' ,sum(1 for i in A if i < 0))

    def t7():
        A = capsule(1, -20, 10, 12).getArray()
        for i in A:
            if i < 0:
                print('0' + ', ', end="", sep="")
            else:
                print(f'{i}' + ', ', end="", sep="")
        print('That"s all')

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

