# practice warmup -- replace everything except last four letters with #s
'''
user_input = input("Please enter your favorite quotation > ")
size = len(user_input)
user_input_list = list(user_input)

user_input_list = user_input_list.reverse()

new_list = []

for i in range (0,size):
    if i < 4:
        current_letter = user_input_list[i]
        new_list.append(current_letter)
    else:
        new_list.append("#")

new_list = new_list.reverse()

print("".join(new_list))
'''

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
