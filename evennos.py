n = int(input('enter n : '))

# print even nos from 0 to n (including n)

'''
i = 0 # loop variable

while i <= n: # loop terminatiing condition
    if not (i % 2):
        print(i)
    i = i + 1 # playing with ur loop variable
'''

# for loop
# range or sequence of things over which u want ur for loop to move about
# 0..n (including n)
'''for ele in range(0, n + 1):
    if not(ele % 2):
        print(ele)'''

for ele in range(0, n + 1, 2):
    print(ele)
