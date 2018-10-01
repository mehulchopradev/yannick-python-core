from math import factorial
class MyMath:

    # each of these functions are self contained and operate only on the parameters passed

    # class level functions
    # do no have any self parameter
    def add(*nos):
        sum = 0
        for n in nos:
            sum += n
        return sum

    def fact(n):
        return factorial(n)

if __name__ == '__main__':
    # mymath = MyMath() # does not have any object attributes
    # print(mymath.add(5, 6, 7))
    # print(mymath.fact(7))

    # call them using the class name
    # class name.function call(5, 6)
    print(MyMath.add(5, 10, 5))
    print(MyMath.fact(6))
