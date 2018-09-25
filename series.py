# every python file (.py) is a "module"
# name of the module -> "series"

# every module in python has one of the magic variables available to the entire file
print(__name__)
# when i directly run the module -> '__main__'
# when the module is imported somewhere -> 'series'

def getfiboseries(n):
    # pass # passes this emtpy block of function without a syntax error beinfg raised
    s = ''

    a, b = 0, 1
    # str + str!!!
    # str + int does not work
    s += str(a) + '\t' + str(b)
    moreleft = n - 2

    for i in range(1, moreleft + 1):
        c = a + b
        s += '\t' + str(c)

        a, b = b, c

    return s

def evenseries(n):
    s = ''

    for i in range(0, n + 1, 2):
        s += str(i) + '\t'
    return s

if __name__ == '__main__':
    # allows to directly run a module as a main program and not run it when the module is imported
    n = int(input('hey enter n : '))
    print(getfiboseries(n))
    print(evenseries(n))
