name = input('Enter name : ')
roll = int(input('Enter roll : '))
marks = float(input('Enter marks : '))

'''
Name : abc
Roll : 10
Marks : 90
'''
'''
A
'''

def getdetails(name, roll, marks):
    return 'Name : ' + name + '\nRoll : ' + str(roll) + '\nMarks : ' + str(marks)

def getgrade(marks):
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

print(getdetails(name, roll, marks))
print(getgrade(marks))

# OOP
