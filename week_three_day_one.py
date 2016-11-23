'''
user_number = int(input("Please enter an integer > "))

number_dictionary = {}

for i in range (0,user_number):
    number_dictionary[i + 1] = (i + 1) ** 2

print(number_dictionary)
'''

'''
# list functions

# example code for demonstrating list functions append, clear, and count
import random

list_o_mania = []

content = "this is the new end of the list"

# append
for i in range(random.randint(0,10)):
    list_o_mania.append(content)

# clear
print("Your list contains {} currently.".format(list_o_mania))
user_clear = input("Should we clear the list? (Y/N) > ")

if user_clear == "Y":
    list_o_mania.clear()

print("Your list contains {} now.".format(list_o_mania))

# count
print("Your list has {} items.".format(list_o_mania.count(content)))
'''

'''
# practice importing something as something else

import random as r

cheese = []

for i in range(0,10):
    cheese.append(r.randint(1,100))

print(cheese)
print(r.choice(cheese))
'''

# practice with list loop

names = ["albert", "bridget", "charles", "donovan", "edward", "frida", "gertrude", "ismerelda", "jack", "lykke", "zanzibar"]

cherry_picked = []

first_letter = input("Please enter a letter > ").lower()

for i in range(0,len(names)):
    if names[i][0] == first_letter:
        cherry_picked.append(names[i])

if len(cherry_picked) == 0:
    print("Sorry, no items were found that started with {}.".format(first_letter))
else:
    print(cherry_picked)
