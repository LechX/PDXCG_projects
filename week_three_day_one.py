user_number = int(input("Please enter an integer > "))

number_dictionary = {}

for i in range (0,user_number):
    number_dictionary[i + 1] = (i + 1) ** 2

print(number_dictionary)
