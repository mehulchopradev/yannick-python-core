source = '/home/mehul/Documents/training/python/yannick/shape.py'
dest = '/home/mehul/Documents/training/python/yannick/shape-copy.py'

'''fs = open(source, mode='r')
fd = open(dest, mode='w')'''

with open(source, mode='r') as fs:
    # when we come out of this with block, fs will be closed
    with open(dest, mode='w') as fd:
        # when we come out of this with block, fd will be closed
        for line in fs:
            fd.write(line)

'''for line in fs:
    fd.write(line)'''

# avoiding memory leaks
# python program fs, fd -> referencing system resources (files)

# always close file references once work done with them
'''fs.close()
fd.close()
'''
