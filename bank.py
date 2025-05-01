class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You cannot withdraw less than {self.min_withdraw} taka')
        elif amount > self.max_withdraw:
            print(f'You cannot withdraw more than {self.max_withdraw} taka')
        else:
            self.balance -= amount




brac = Bank(15000)
brac.withdraw(500)
print(brac.balance)
brac.deposit(10000)
print(brac.balance)
brac.withdraw(2)
