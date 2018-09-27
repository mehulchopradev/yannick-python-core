from student_oop import Student

studentlist = []
smap = {}

while True:
    print('1. Enter student data(name<space>roll<space>marks) : ')
    print('2. Display all students in order : ')
    print('3. Search by roll : ')
    print('4. Exit')
    choice = int(input('Enter choice: '))

    if choice == 4:
        break

    if choice == 1:
        sd = input('Enter student data in the format explained: ')
        tokens = sd.split(' ')
        s = Student(name=tokens[0], marks=float(tokens[2]), roll=int(tokens[1]))
        studentlist.append(s)
        smap[s.roll] = s

    elif choice == 2:
        for student in studentlist:
            print(student.getdetails())
    elif choice == 3:
        roll = int(input('enter roll : '))

        '''for student in studentlist:
            if student.roll == roll:
                print(student.getdetails())
                break
        else:
            # will execute when the corresponding for was exhausted
            # we never broke out of the for loop
            print('No student found')'''

        if roll in smap:
            s = smap[roll]
            print(s.getdetails())
        else:
            print('No student found')
