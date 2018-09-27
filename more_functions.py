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
print(perimeter(*stats))
