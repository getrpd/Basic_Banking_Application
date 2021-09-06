from random import randint


class Client:
    # {account_number: xxxxx, name: "xxxxxx", holdings: xxxx}
    account = {}

    def __init__(self, name, deposit):
        self.account['account_number'] = randint(10000, 99999)
        self.account['name'] = name
        self.account['holdings'] = deposit

    def balance(self):
        print('Current Account Balance: $', self.account['holdings'])

    def deposit(self, amount):
        self.account['holdings'] += amount
        print("Amount Deposited: $", amount)
        self.balance()

    def withdraw(self, amount):
        if self.account['holdings'] < amount:
            print('Insufficient Balance for Withdrawal.')
            self.balance()
        else:
            self.account['holdings'] -= amount
            print("Amount Withdrawn: $", amount)
            self.balance()