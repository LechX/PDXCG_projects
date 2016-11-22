'''
# class start exercise -- guess a number

import random

computer_number = random.randint(1,100)

user_number = int(input("Please guess a number between 1 and 100 > "))

print(computer_number)

while computer_number != user_number:
    difference = abs(computer_number - user_number)
    if difference <= 10:
        print("You're close!")
    else:
        print("You're a ways off.")
    user_number = int(input("Please guess again > "))
    if abs(computer_number - user_number) < difference:
        print("You're getting closer!")
    else:
        print("You're getting farther away!")

print("You got it!")
'''



'''
# practice with for loop

total = 0

for i in range(0,101):
    if i % 2 == 1:
        total += i

print(total)
'''



'''
# fizz buzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''



'''
# generate a list of 100 items of random numbers from 0 to 1000 using a for loop
import random

random_number_list = []

for i in range(0,100):
    random_number_list.insert(i,random.randint(0,1000))

# using a for loop, find the max number in the list and print "the max number is: "
max_num = 0

for i in range(0,100):
    # max_num = max(random_number_list)
    if random_number_list[i] > max_num:
        max_num = random_number_list[i]
    else:
        max_num = max_num

print(random_number_list)
print("The max number is: {}".format(max_num))

# using a for loop, find the min number in the list and print "the min number is: "
min_num = 1000

for i in range(0,100):
    # min_num = min(random_number_list)
    if random_number_list[i] < min_num:
        min_num = random_number_list[i]
    else:
        min_num = min_num

print("The min number is: {}".format(min_num))

# for loop, find the sum of the list and print "the sum of the list is: "
sum_list = 0

for i in range(0,100):
    sum_list += random_number_list[i]

print("The sum of the list is: {}".format(sum_list))

# for, take an integer user input and check if the number entered is in the list, print T or F
user_input = int(input("Please enter a number between 0 and 1,000 > "))

index_variable = 0

for i in random_number_list:
    if i == user_input:
        print("True")
        break
    index_variable += 1
    if index_variable == len(random_number_list):
        print("False")
        break

# take a user input as an int and check how many times it appears in the list
other_user_input = int(input("Please enter another number between 0 and 1,000 > "))

other_user_input_count = 0

for i in random_number_list:
    if i == other_user_input:
        other_user_input_count += 1

print("The number {} was in the list {} times.".format(other_user_input,other_user_input_count))
'''



# random number 0 to 1000, 10 user guesses, return congrats if they get it, otherwise say if hotter/colder than before

# import random and have computer choose number
import random
computer_number = random.randint(1,1000)

# create user guess list
user_guess_list = []
user_guess = int(input("Please choose a number between 1 and 1000 > "))
user_guess_list.insert(0,user_guess)
new_diff = "string new"
old_diff = "string old"

# define hot or cold function
def hot_or_cold(new,old):
    if new > old:
        print("You're getting colder!")
    elif new < old:
        print("You're getting warmer!")
    else:
        print("You broke everything.")

# for loop to check guess, add it to the list, check guess number, and use hot/cold function
for i in range (0,14):
    while computer_number != user_guess:
        if len(user_guess_list) == 15:
            break
        else:
            user_guess = int(input("You're not quite there, guess again > "))
            old_diff = abs(computer_number - user_guess_list[i])
            user_guess_list.insert(i,user_guess)
            new_diff = abs(computer_number - user_guess_list[i])
            hot_or_cold(new_diff,old_diff)

if len(user_guess_list) == 15:
    print("Better luck next time!")
    print("The computer's number was {}.".format(computer_number    ))
else:
    print("You got it! Congratulations.")
