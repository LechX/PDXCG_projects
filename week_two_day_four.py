'''
# create list of random numbers and count the even numbers
import random

random_number_list = []

for i in range(0,100):
    random_number_list.insert(i,random.randint(100,1000))

print(random_number_list)

even_numbers = 0
odd_numbers = 0

for i in range(0,100):
    if random_number_list[i] % 2 == 0:
        even_numbers += 1
    elif random_number_list[i] % 2 != 0:
        odd_numbers += 1
    else:
        print("Taco")

print(even_numbers)
print(odd_numbers)
'''



# continue and break

# break stops the smallest enclosing for or while loop

# continue breaks out of the current loop iteration and proceeds with next loop iteration
'''
word = "classroom"

for i in range(0,len(word)):
    print(word[i])
'''
# create word_list
'''
word_list = list("abcdefg")

for i in range(0,len(word_list)):
    print(word_list[i])

for i in word_list:
    print(i)
'''
# get user input, loop through string, print value, if value = vowel, break loop
'''
entry = list(input("Please enter a jumble of letters > "))
vowels = list("aeiouy")

for i in entry:
    if i in vowels:
        break
    print(i)
'''

# user input a cipher key value (integer) and four letter word
cipher_value = int(input("Please enter an integer value > "))
user_word = str(input("Please enter a word without spaces > ")).lower()
'''
while len(user_word) != 4:
    user_word = str(input("Please try entering an actual four letter word > "))
'''
# create dictionary and alphabet
dictionary = {}
alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in range(0,len(alphabet)):
    dictionary[alphabet[i]] = i

# encode user's word using pdx code guild cipher
''' basic cipher here, for learning's sake
first_letter_index = dictionary[user_word[0]] + cipher_value
second_letter_index = dictionary[user_word[1]] + cipher_value
third_letter_index = dictionary[user_word[2]] + cipher_value
fourth_letter_index = dictionary[user_word[3]] + cipher_value

print(alphabet[first_letter_index]+alphabet[second_letter_index]+alphabet[third_letter_index]+alphabet[fourth_letter_index])
'''

# cipher that accepts limitless values

letter_index = 0
new_string = []

for i in range(0,len(user_word)):
    if dictionary[user_word[i]] + cipher_value > 25:
        letter_index = (dictionary[user_word[i]] + cipher_value) % 26
    else:
        letter_index = dictionary[user_word[i]] + cipher_value
    new_string.insert(i, alphabet[letter_index])

# given an integer you can shift all letters over by that amount
print("".join(new_string))
