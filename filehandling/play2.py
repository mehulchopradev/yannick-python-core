path = '/Users/mehul.chopra/Documents/personal/yannick-python-core/shape.py'
file = open(path, mode='r')

c = file.read(10) # moves the file pointer to EOF
print(c)

print('******again read*******')

c = file.read()
print(c)
