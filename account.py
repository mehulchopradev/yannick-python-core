class Account:

    minbalance = 500

    def __init__(self, name, acctype, balance):
        self.name = name
        self.acctype = acctype
        self.balance = balance

    def withdraw(self, amt):
        if self.balance - amt < Account.minbalance:
            # exceptional condition that has happened in the software
            # handling of the program shudchange
            pass
        else:
            self.balance = self.balance - amt
            return self.balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        return self.balance
