from checking import Checking
from saving import Saving

class Account:

    id = 0
    account_list = []

    def __init__(self, first, last, initial_amount):
        self.first = first
        self.last = last
        self.checking = Checking(initial_amount)
        self.saving = Saving(0)
        self.idnum = Account.id
        Account.id += 1
        Account.account_list.append(self)

    def transfer_within_account(self, from_account, to_account, amount):
        if from_account == "checking" and to_account == "saving":
            self.checking.balance -= amount
            self.checking.transaction_history.append("Transferred {} to saving".format(str(amount)))
            self.saving.balance += amount
            self.saving.transaction_history.append("Received {} from checking".format(str(amount)))
        if from_account == "saving" and to_account == "checking":
            self.saving.balance -= amount
            self.saving.transaction_history.append("Transferred {} to checking".format(str(amount)))
            self.checking.balance += amount
            self.checking.transaction_history.append("Received {} from saving".format(str(amount)))

    def transfer_to_other_member(self, other, amount):
        self.checking.balance -= amount
        self.checking.transaction_history.append("Transferred {} from checking to {}'s checking".format(str(amount),Account.__str__(other)))
        other.checking.balance += amount
        other.checking.transaction_history.append("Received {} from {}'s checking".format(str(amount),Account.__str__(self)))

    def print_balances(self):
        print("balance in {}'s checking: {}".format(Account.__str__(self), self.checking.balance))
        print("balance in {}'s saving: {}".format(Account.__str__(self), self.saving.balance))

    def print_transaction_history(self):
        print("transaction history for {}'s checking:".format(Account.__str__(self)))
        for i in self.checking.transaction_history:
            print(i)
        print("transaction history for {}'s saving:".format(Account.__str__(self)))
        for i in self.saving.transaction_history:
            print(i)

    def __str__(self):
        return "%s %s" % (self.first, self.last)

    def __repr__(self):
        return int(self.idnum)
