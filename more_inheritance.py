# vendor 1
class Abc:

    def fun(self):
        print('Fun from abc')

    def hello(self):
        print('Hello doing something else')

# vendor 2
class Pqr:

    def foo(self):
        print('Foo from Pqr')

    def hello(self):
        print('Hello World')

class Mno(Pqr, Abc): # multiple inheritance
    # one child class has more than one class as its parent
    pass

m = Mno()
m.foo()
m.fun()
m.hello() # Hello World
# expecting to call the hello function from the class Pqr
