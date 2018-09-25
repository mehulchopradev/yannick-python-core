'''
    1. Fibonacci series
    2. Even series
    3. Even or odd
    4. Exit
    Please enter ur choice: 1
    Enter n: 8
    0 1 1 2 3 5 8 13

    1. Fibonacci series
    2. Even series
    3. Even or odd
    4. Exit
    Please enter ur choice: 2
    Enter n: 6
    0 2 4 6

    1. Fibonacci series
    2. Even series
    3. Even or odd
    4. Exit
    Please enter ur choice: 3
    Enter n: 10
    Even

    1. Fibonacci series
    2. Even series
    3. Even or odd
    4. Exit
    Please enter ur choice: 4
    Exit out of ur python program
'''

# user defined modules
# import series
from series import evenseries as eseries, getfiboseries
# import xyz.supercoders.modules.math as mymath
from xyz.supercoders.modules.math import evenorodd

# built in modules
# math
# module namespace conflict
# packages!!
import math

def evenseries(n):
    print('Bla Bla')

while True:
    print('1. Fibonacci series')
    print('2. Even series')
    print('3. Even or odd')
    print('4. Factorial')
    print('5. Exit')

    choice = int(input('Please enter ur choice: '))

    if choice != 5:
        n = int(input('Enter n: '))

    if choice == 1:
        # Fibonacci series
        # print(series.getfiboseries(n)) # modulename.functionCall(...)
        print(getfiboseries(n))
    elif choice == 2:
        # print(series.evenseries(n))
        print(eseries(n))
    elif choice == 3:
        # print whether even or odd
        # print(xyz.supercoders.modules.math.evenorodd(n))
        # print(mymath.evenorodd(n))
        print(evenorodd(n))
    elif choice == 4:
        print(math.factorial(n))
    else:
        break # break out from the enclosing while loop
