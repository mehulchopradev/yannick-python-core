print('Program started')

n = input('Enter n : ')

# ValueError -> Exception

# handling or preparing for the exceptional scenario
# which may or may not happen
# try -> except (1..*) -> else
try:
    ni = int(n)
except ValueError:
    print('Please enter integer values')
except Exception:
    print('Some error happened')
else:
    # else block statements will execute when there is no exception thrown
    # in the corresponding try block
    print('Odd') if ni % 2 else print('Even')

print('Program ended')
