nos = [5, 6, 10, 2, 3, 1, 7]

'''minus1 = [n - 1 for n in nos]
print(minus1)'''

# callback function passed as an argument to map function
def decrementBy1(ele):
    return ele - 1

m = map(decrementBy1, nos)
for item in m:
    print(item)

print('*****************squares of all numbers from nos*******************')

# callback function (code that will be passed to the map function)
def square(ele):
    return ele ** 2

ans = map(square, nos)
for a in ans:
    print(a)

print('******************even nos ***********************')
'''evens = [n for n in nos if not (n % 2)]
print(evens)'''

def evenNo(ele):
    return not(ele % 2)

fl = filter(evenNo, nos)
for f in fl:
    print(f)
