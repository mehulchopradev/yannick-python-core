# fibonacci series
# 0 1 1 2 3 5 8

n = int(input('enter n : '))
# n = 8 (8 fibonacci numbers)
# 0 1 1 2 3 5 8 13

a, b = 0, 1

print(a)
print(b)

moreleft = n - 2

# range overwhich the for loop will move (1..moreleft + 1)

for t in range(1, moreleft + 1):
    c = a + b
    print(c)

    a, b = b, c
