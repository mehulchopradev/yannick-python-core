def perimeterrectangle(length, breadth=2): # default value to breadth
    '''p = 2 * (length + breadth)
    return p'''

    a = 5 # global in the function
    l = 10 # global in the function

    # length, breadth are global variables in the function

    # refer the global file variables. Cannot modify a global file variable inside a function
    # unintentionally
    print(l) # 10
    print(b) # global at the file level
    return 2 * (length + breadth)

def arearectangle(length, breadth):
    '''a = length * breadth
    return a'''

    # length, breadth are global variables in the function
    return length * breadth

# l, b, pa are global variables in the file
l = float(input('Enter length : '))

# int(), bool(), str()

b = float(input('Enter breadth : '))

# one function in different forms (method overloading)
pa = perimeterrectangle(l, b)
print(pa)

print(l) # 82
print(b) # 34

'''
pa = perimeterrectangle(6)
print(pa)

pa = perimeterrectangle(5, 3)
print(pa)

pa = perimeterrectangle(6.3, 5.2)
print(pa)'''

'''a = arearectangle(l, b)
print(a)'''
