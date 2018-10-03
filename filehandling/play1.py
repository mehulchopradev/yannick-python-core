path = '/Users/mehul.chopra/Documents/personal/yannick-python-core/markscalc.py';
file = open(path, mode='r')

print('*******first print************')
for line in file: # get line by line
    print(line)
    # every iteration of the for loop moves the internal file pointer to the next line

print('******second print***********')
for line in file:
    print(line)
    # since the file pointer is on the EOF, this for loop will not get any data from the file

print('*******third print********')
# reset the file pointer to the start
file.seek(0)

for line in file:
    print(line)
# the filer pointer has again reached EOF

file.seek(0)

print('****** Fourth print*******')
lines = file.readlines() # reads all the lines in one go from the file on the disk
# and also moves the file poninter to the end
# use this method with caution. For large files getting all the 1 million lines,
# at one go in the lines list data structure can get expensive

for line in lines:
    print(line)
# readlines() resets the file pointer to the end

print('******Fifth print*********')
for line in file:
    print(line)
