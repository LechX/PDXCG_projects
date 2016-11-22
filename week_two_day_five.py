'''
# print vowels from a user string using a for loop
user_vowels = input("Please enter your favorite band > ").lower()
vowels = list("aeiouy")

for i in range(0,len(user_vowels)):
    if user_vowels[i] not in vowels:
        print(user_vowels[i])
    else:
        continue


# print consonants from a user string using a for loop
user_consonants = input("Please enter your favorite city > ").lower()
consonants = list("bcdfghjklmnpqrstvwxz")

for i in range(0,len(user_consonants)):
    if user_consonants[i] not in consonants:
        print(user_consonants[i])
    else:
        continue
'''

'''
# create list of randomly generated numbers between 100 and 10000
import random
random_number_list = []
insert_number = 0
blocked_list = []

# user integer input
user_number = int(input("Please pick a number between 1 and 9 > "))

# for loop to add 200 values
for i in range(0,200):
    insert_number = random.randint(100,10000)
    if insert_number % user_number == 0:
        random_number_list.insert(i,insert_number)
    else:
        blocked_list.insert(i,insert_number)

print("The sum of numbers divisible by {} is {}. There are {} in the list.".format(user_number,sum(random_number_list),len(random_number_list)))

print("The sum of numbers not divisible by {} is {}. There are {} in the list.".format(user_number,sum(blocked_list),len(blocked_list)))
'''

'''
# replace vowels with the index number that it is
vowel_replace = list(input("Please enter your favorite vegetable > "))
vowels = list("aeiouy")

for i in range(0,len(vowel_replace)):
    if vowel_replace[i] in vowels:
        vowel_replace[i] = str(i)
    else:
        continue

print("".join(vowel_replace))
'''

# print a tic-tac-toe board using 2D lists
import random
board = []

for i in range(0,3):
    squares = ["*"] * 3
    board.append(squares)

def print_board(board):
    """
    function to print current status of board
    takes a list as an argument, in this case the board list
    output is printing the board list contents with spaces in between
    """
    for row in board:
        print(" ".join(row))

def app():
    """
    function to play tic tac toe with user vs computer selecting at random
    function takes no input but it will prompt the user to enter row and column
    output is printing either the winner or a tie game to the console
    """

    # create and set variables for row, column, turn, and winning
    row = 3
    column = 3
    current_turn = "x"
    game_over = "no"

    for i in range(0,9):
        print("It is the {}'s turn.".format(current_turn))
        if current_turn == "o": # computer selection
            row = random.randint(0,2)
            column = random.randint(0,2)
        elif current_turn == "x": # user selection
            row = int(input("Please enter a row number (0-2) > "))
            column = int(input("Please enter a column number (0-2) > "))

        while board[row][column] != "*": # check to make sure spot is open, ask again if necessary
            if current_turn == "o":
                row = random.randint(0,2)
                column = random.randint(0,2)
            elif current_turn == "o":
                print("That spot is already taken.")
                row = int(input("Please enter a row number (0-2) > "))
                column = int(input("Please enter a column number (0-2) > "))

        if current_turn == "o":
            print("The computer chose row {} and column {}.".format(row,column))

        board[row][column] = current_turn # change * to x or o

        for i in range(0,3): # check to see if any winning condition is met
            if board[i][0] == board[i][1] == board[i][2] != "*":
                game_over = "yes"
            elif board[0][i] == board[1][i] == board[2][i] != "*":
                game_over = "yes"
            elif board[0][0] == board[1][1] == board[2][2] != "*":
                game_over = "yes"
            elif board[0][2] == board[1][1] == board[2][0] != "*":
                game_over = "yes"
        if game_over == "yes": # win condition is met, break
            break

        if current_turn == "x": # switch turns
            current_turn = "o"
        else:
            current_turn = "x"

        print_board(board) # print current status of board

    if game_over == "yes":
        print("CONGRATULATIONS to team {}, you win!".format(current_turn))
    else:
        print("Sometimes nobody wins! Game over.")

    print_board(board)

app()
