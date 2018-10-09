import json

with open('student_data.json', mode='r') as fp:
    studentdata = json.load(fp)

def printallstudents():
    items = studentdata.items()
    for item in items:
        print('Roll: {0}\nName: {1}'.format(item[0], item[1]['name']))

def searchbyroll(roll):
    if roll in studentdata:
        v = studentdata[roll]
        print('Roll: {0}\nName: {1}'.format(roll, v['name']))
    else:
        print('Not found')

def updateentry(roll, name, gender):
    studentdata[roll] = {
        'name': name,
        'gender': gender
    }

def commitdata():
    with open('student_data.json', mode='w') as fp:
        json.dump(studentdata, fp, indent=2)

while True:
    print('1. Viewing all students')
    print('2. Search by roll')
    print('3. Update data')
    print('4. Exit')
    choice = int(input('enter choice: '))
    if choice == 1:
        printallstudents()
    elif choice == 2:
        roll = input('enter roll: ')
        searchbyroll(roll)
    elif choice == 3:
        roll = input('enter roll: ')
        name = input('enter name: ')
        gender = input('enter gender: ')

        updateentry(roll, name, gender)
    else:
        commitdata()
        break
