class Checking:

    def __init__(self, amount):
        self.balance = amount
        self.initial_balance = amount
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append("Deposited {}".format(str(amount)))

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append("Withdrew {}".format(str(amount)))

    def print_transaction_history(self):
        for i in self.transaction_history:
            print(i)
