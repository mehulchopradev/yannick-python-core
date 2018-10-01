# that can take 0 to n parameters
def mysum(*nos):
    # print(nos)
    # print(type(nos)) # tuple
    sum = 0
    for n in nos:
        sum += n
    return sum

# positional arguments packing in a tuple
'''print(mysum())
print(mysum(5))
print(mysum(6, 5, 10))
print(mysum(5, 5, 10, 6, 5, 10, 20))
'''

def perimeter(length, breadth):
    return 2 * (length + breadth)

stats = [6, 3]
# print(perimeter(stats[0], stats[1]))
# positional parameter unpacking
# print(perimeter(*stats))

def area(**rectstats):
    # print(type(rectstats))
    # print(rectstats)
    return rectstats['length'] * rectstats['breadth']

# print(area(6, 3))
# print(area(5.3, 5.1)) # positional parameters
# print(area(length=5.3, breadth=5.1)) # keyword arguments
# print(area(breadth=4, length=10))

statsmap = {
    'length': 9,
    'breadth': 4
}
# print(perimeter(statsmap['length'], statsmap['breadth']))
print(perimeter(**statsmap))
