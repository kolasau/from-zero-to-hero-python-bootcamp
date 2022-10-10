class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, dep):
        self.balance += dep
        return "Deposit Accepted"

    def withdraw(self, wi):
        if self.balance >= wi:
            self.balance -= wi
            return "Withdrawal Accepted"
        else:
            return "Not enough funds"


acc1 = Account('Jose', 100)
print(acc1)
print(acc1.deposit(50))
print(acc1.deposit(50))
print(acc1.deposit(50))
print(acc1.deposit(50))
print(acc1.withdraw(250))
print(acc1.withdraw(250))
print(acc1.balance)

acc2 = Account('Love', 1000000)
print(acc2)
print(acc2.withdraw(100000))
print(acc2)
print(acc2.owner)
print(acc2.deposit(201719))
print(acc2)
print(acc2.withdraw(2000000))

