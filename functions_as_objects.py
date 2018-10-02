def abc():

    name = 'mehul' # name (abc)
    age = 32 # age (abc)
    def pqr(): # pqr (abc)
        print('Pqr')
        age = 20 # pqr scope
        print(name) # (CLosures) inner function can very well acces the enclosing (outer) function variables
        print(age) # 20
    pqr()

    print(age) # 32

# print(abc())
# pqr() Error!

def mno(a):
    # a (mno)

    #rty (mno)
    def rty(b):
        return (a + b) * (a ** b)

    # a function can return anothe function object as it does for regular objects(int, str, float,..)
    return rty

r = mno(5)
print(r)
# r also becomes a callable variable like rty
# scope of rty was only mno
# scope of r is entire module
ans = r(2)
print(ans)


def xyz(a, fn):
    print(a) # 4
    # fn  is a callable variable
    # scope of fn is xyz
    fn() # pty()

def pty():
    print('Hello to All')

xyz(4, pty) # a function object can be passed as a parameter to another function
# passing code as an argument to a function
# callback functions
