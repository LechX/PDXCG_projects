from account import Account


test_1 = Account("Lech", "Kaiel", 5000)
test_2 = Account("Index", "One", 1000)
test_3 = Account("Index", "Two", 2000)
test_4 = Account("Index", "Three", 3000)
test_5 = Account("Index", "Four", 4000)

def get_account(id):
    '''
    this will grab an account object based on the idnum
    param id: idnum of the account we are trying to grab
    returns: returns account object if found, else returns None
    '''
    for i in Account.account_list:
        if i.__repr__() == id:
            return i
    return "none"

# user enters account number
# while loop for action (withdraw, transfer, deposit, quit)
# based on action chosen, gather information necessary to complete transaction
# option to quit
# print transaction history

def request_user_number():
    user_id = int(input("Please enter your user ID number > "))
    user_id = get_account(user_id)
    return user_id

def request_transaction_type():
    print("What type of transaction would you like to perform?")
    t_type = input("'w' to withdraw, 't' to transfer, 'd' to deposit, 'q' for quit >> ").lower()
    acceptable_response_list = list("wtdq")
    while t_type not in acceptable_response_list:
        t_type = input("Try again! 'w' to withdraw, 't' to transfer, 'd' to deposit, 'q' for quit >> ").lower()
    return t_type

def action_withdraw(user_id):
    # from checking or saving?
    c_or_s = input("'c' for checking or 's' for saving? ").lower()
    # how much?
    amount = int(input("How much would you like to withdraw? "))
    # execute transaction
    if c_or_s == "c":
        user_id.checking.withdraw(amount)
    elif c_or_s == "s":
        user_id.saving.withdraw(amount)
    else:
        print("I didn't quite catch that.")

def action_deposit(user_id):
    # from checking or saving?
    c_or_s = input("'c' for checking or 's' for saving? ").lower()
    # how much?
    amount = int(input("How much would you like to deposit? "))
    # execute transaction
    if c_or_s == "c":
        user_id.checking.deposit(amount)
    elif c_or_s == "s":
        user_id.saving.deposit(amount)
    else:
        print("I didn't quite catch that.")

def action_transfer(user_id):
    within_or_across = input("'i' to transfer internally or 'a' for across > ") # within account or to another member
    if within_or_across == "i":
        amount = int(input("How much would you like to transfer? > "))
        c_or_s = input("Would you like to transfer TO checking or saving? c/s > ") # direction of transfer within account
        if c_or_s == "c":
            user_id.transfer_within_account("saving", "checking", amount)
        elif c_or_s == "s":
            user_id.transfer_within_account("checking", "saving", amount)
    elif within_or_across == "a":
        target_account_id = int(input("To which account id number? > "))
        target_account = get_account(target_account_id)
        amount = int(input("How much would you like to transfer? > "))
        user_id.transfer_to_other_member(target_account, amount)
    else:
        print("I didn't quite catch that.")

def main():
    user_id = request_user_number()
    transaction_type = request_transaction_type()
    while transaction_type != "q":
        if transaction_type == "w":
            action_withdraw(user_id)
        elif transaction_type == "d":
            action_deposit(user_id)
        elif transaction_type == "t":
            action_transfer(user_id)
        optional_break = input("Would you like to perform any more transactions? y/n > ").lower()
        if optional_break == "n":
            break
        else:
            transaction_type = request_transaction_type()
    print("Thanks for your business! History for your session below:")
    user_id.print_transaction_history()
    user_id.print_balances()

main()

#print(test_1.__dict__)
#print(test_2.__dict__)
#print(test_3.__dict__)

'''
testing checking methods
'''
# test_2.print_balances()
# test_2.checking.deposit(500)
# test_2.print_balances()
# test_2.checking.withdraw(1000)
# test_2.print_balances()
# test_2.print_transaction_history()
# test_2.checking.print_transaction_history()

'''
testing saving methods
'''
# print(test_3.saving.balance)
# test_3.saving.deposit(3000)
# test_3.print_balances()
# test_3.saving.withdraw(1000)
# test_3.print_balances()
# test_3.saving.interest_accrual()
# test_3.print_balances()

'''
testing account methods
'''

# test_1.print_balances()
# test_1.transfer_within_account("checking", "saving", 1000)
# test_2.transfer_within_account("checking", "saving", 2000)
#
# test_1.transfer_to_other_member(get_account(1), 525)
# test_1.print_balances()
# test_1.transfer_to_other_member(test_3, 525)
# test_1.print_balances()
#
# print(test_1.transaction_history)
# test_1.print_transaction_history()
# test_2.print_transaction_history()
# test_3.print_transaction_history()
#
# test_2.print_balances()
# test_1.print_balances()
