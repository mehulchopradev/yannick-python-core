source = '/Users/mehul.chopra/Documents/personal/yannick-python-core/shape.py'
dest = '/Users/mehul.chopra/Documents/personal/yannick-python-core/shape-copy.py'

fs = open(source, mode='r')
fd = open(dest, mode='w')

for line in fs:
    fd.write(line)

# avoiding memory leaks
# python program fs, fd -> referencing system resources (files)

# always close file references once work done with them
fs.close()
fd.close()
