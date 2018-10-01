from student_oop import Student
from professor import Professor
from photosession import PhotoSession

print(Student.count) # 0

# developer y
s1 = Student('mehul', 10, 90, 'm') # 4005
'''
    Student() ->
    1. Reserves an area in the ram for the object # 4005
    2. Student.__init__(4005, 'mehul', 10, 90)
'''

print(s1.getdetails())
print(s1.get_name_roll())
print(s1.gender)

'''
    Student.getdetails(s1)
'''

# s1 stores the address of the object (4005). Reference variable
# s1 object has no attributes

# s1.name = 'mehul'
# s1 object now will have 1 attribute

# s1.roll = 10
# s1.marks = 90

print(Student.count)

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

print(Student.count)

p = Professor('prof 1', 'm', ['Python','Java'])
print(p.getdetails())

PhotoSession.takephoto(s2)
PhotoSession.takephoto(p)
PhotoSession.takephoto('good morning')
