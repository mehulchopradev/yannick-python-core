from square import Square
from rectangle import Rectangle

# an abstract class with an abstract method cannot be instantiated
# cannot create an object
s = Square(4)
r = Rectangle(6, 3)

print(s.area())
print(r.area())

# Square IS-A Shape
# Rectangle IS-a Shape
