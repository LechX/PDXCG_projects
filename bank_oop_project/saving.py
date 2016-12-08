class Saving:

    interest_rate = 1.03

    def __init__(self, amount):
        self.balance = amount
        self.initial_balance = amount
        self.transaction_history = []
        self.interest_rate = Saving.interest_rate

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append("Deposited {}".format(str(amount)))

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append("Withdrew {}".format(str(amount)))

    def print_transaction_history(self):
        for i in self.transaction_history:
            print(i)

    def interest_accrual(self):
        self.balance = self.balance * self.interest_rate
        self.transaction_history.append("Interest accrued, new balance is {}".format(str(self.balance)))
