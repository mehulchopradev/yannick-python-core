from account import Account

a1 = Account(name='mehul chopra', acctype='Savings', balance=9000)
a2 = Account(name='jane', acctype='Current', balance=8000)

print(a1.withdraw(9000))
print(a2.deposit(900))
