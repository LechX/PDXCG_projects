'''
# practice warmup -- replace everything except last four letters with #s

# get user input
user_input = input("Please enter your favorite quotation > ")

hashes_and_last_four = []

# add # for each letter minus four
if len(user_input) <= 4:
    for i in range(0,len(user_input)):
        hashes_and_last_four.append("#")
else:
    for i in range(0,len(user_input) - 4):
        hashes_and_last_four.append("#")

    # append last four letters
    hashes_and_last_four.append(user_input[len(user_input) - 4:])

print("".join(hashes_and_last_four))
'''


# random number guessing game with while loop
import random

user_number = int(input("Please guess a number between 1 and 10 > "))

computer_number = random.randint(1,10)

while user_number != computer_number:
    user_number = int(input("Guess again! > "))

print("Congrats, you got it! The correct number was {}.".format(computer_number))
