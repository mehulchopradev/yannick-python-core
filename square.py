from shape import Shape
# Square -> Shape -> ABC (multilevel)
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
