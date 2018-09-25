marks = float(input('enter marks : '))
'''
    >= 70 -> A
    >= 60 -> B
    >= 40 -> C
    < 40 -> F
    > 100 or < 0 -> I
'''

# if - elif - elif - * - else
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

# scope of variable g is the entire file
# scope of variables in python is never block scoped. Either entire file or the function

print(g)
