# OOP
# 1 Student (entity) in Real world -> Some memory location in the program (RAM)
# - Objects : data type - Student
# - class className - data type of the object that i can create from a class (blueprint)
# - class -> 1 to n objects

# 2 Entity attributes -> properties of the object
# every Student object is going to have its own set of properties

# 3 Entity actions -> functions called on that object

# developer X
class Student:
    # default
    '''def __init__(self):
        pass'''

    def __init__(self, name, roll, marks):
        # constructor
        self.name = name
        self.roll = roll
        self.marks = marks

    def get_name_roll(self):
        return (self.name, self.roll) # tuple

    def getdetails(self):
        return 'Name : ' + self.name + '\nRoll : ' + str(self.roll) + '\nMarks : ' + str(self.marks)

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


if __name__ == '__main__':
    # developer y
    s1 = Student('mehul', 10, 90) # 4005
    '''
        Student() ->
        1. Reserves an area in the ram for the object # 4005
        2. Student.__init__(4005, 'mehul', 10, 90)
    '''

    print(s1.getdetails())
    print(s1.get_name_roll())

    '''
        Student.getdetails(s1)
    '''

    # s1 stores the address of the object (4005). Reference variable
    # s1 object has no attributes

    # s1.name = 'mehul'
    # s1 object now will have 1 attribute

    # s1.roll = 10
    # s1.marks = 90


    s2 = Student('jane', 32, 56.50) # 70005
    # s2 stores the address (70005)

    '''
        Student() ->
        1. Reserves an area in the ram for the object # 70005
        2. Student.__init__(70005, 'jane', 32, 56.50)
    '''

    '''s2.studentname = 'jane'
    s2.r = 32
    s2.marks = 56.50'''

    # print(type(s1))
    # print(type(s2))

    print(s2.getdetails())
    '''
        Student.getdetails(s2)
    '''


    '''
    print(s1.name)
    print(s1.roll)

    print(s2.name)
    print(s2.roll)
    '''

    print(s1.getgrade())
    # Student.getgrade(s1)


    print(s2.getgrade())
    # Student.getgrade(s2)
