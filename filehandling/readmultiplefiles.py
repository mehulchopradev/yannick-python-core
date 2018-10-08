from fileinput import input
import fileinput

basepath = '/home/mehul/Documents/training/python/yannick'

files = (basepath + '/collegeuser.py', basepath + '/professor.py', basepath + '/student_oop.py')

with input(files=files) as fa:
    for line in fa:
        if fileinput.isfirstline():
            print('******Current file being read is : {0}*****************'.format(fileinput.filename()))
        print(line)
