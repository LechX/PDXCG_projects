'''
# random computer-generated number here
import random

user_score = random.randint(0,100)
user_score_string = str(user_score)
print("Your grade is " + user_score_string + "%")

# user input version here
# user_score = input("Please enter a number between 1 and 100 > ")

# turn numbers into percentage floats (assumes input is an integer)

if user_score > 1 and user_score <= 100:
    user_score = user_score/100
elif user_score >= 0 and user_score <= 1:
    user_score = float(user_score)
else:
    print("That didn't work!")
    user_score = input("Please try again, enter a number between 1 and 100 > ")

# declare user_grade for future use
user_grade = ""

# calculate user_grade based on user_score

if user_score >= 0.90:
    user_grade = "A"
elif user_score >= 0.80:
    user_grade = "B"
elif user_score >= 0.70:
    user_grade = "C"
elif user_score >= 0.60:
    user_grade = "D"
else:
    user_grade = "F"

# print!

print(user_grade)
'''

user_answers = {
    1: 10
    2: 6
    3: False
}

correct_answers = {
    1: 15
    2: 6
    3: False
}

for i in user_answers.item():

"What is 14 % 4? >>> "
"True or False: 65 % 15 = 0 >>> "
""

# create user input dictionary, correct answer dictionary, and user_score variable
# ask modulo questions which store answers in user's dictionary
# run user's answer against correct answers and keep track of user_score using += and -=
# print # answered correctly and # answered incorrectly as well as percentage correct

# print a letter grade associated with percent correct
