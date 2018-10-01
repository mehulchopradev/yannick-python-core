from collegeuser import CollegeUser
# OOP
# 1 Student (entity) in Real world -> Some memory location in the program (RAM)
# - Objects : data type - Student
# - class className - data type of the object that i can create from a class (blueprint)
# - class -> 1 to n objects

# 2 Entity attributes -> properties of the object
# every Student object is going to have its own set of properties

# 3 Entity actions -> functions called on that object

# developer X
# CollegeUser -> super class/parent class/base class
# Student -> sub class/child class/concrete class
class Student(CollegeUser):

    # class attribute
    count = 0

    # default
    '''def __init__(self):
        pass'''

    def __init__(self, name, roll, marks, gender=None):
        # constructor
        super().__init__(name, gender)
        # CollegeUser.__init__(self, name, gender)

        # object attributes
        self.roll = roll
        self.marks = marks

        # access class attributes using the class name
        Student.count += 1

    def get_name_roll(self):
        return (self.name, self.roll) # tuple

    # method overriding
    # signature of the overriden function shud be same as the signature of the super class function
    def getdetails(self):
        # ur own implementation to this method
        part1 = super().getdetails()
        part2 = '\nRoll: {0}\nMarks: {1}'\
            .format(self.roll, self.marks)
        return part1 + part2

    def getgrade(self):
        marks = self.marks
        if marks > 100 or marks < 0:
            g = 'I'
        elif marks >= 70:
            g = 'A'
        elif marks >= 60:
            g = 'B'
        elif marks >= 40:
            g = 'C'
        else:
            g = 'F'

        return g
