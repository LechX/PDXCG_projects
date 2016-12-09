from deck import Deck
from hand import Hand


def get_account(id):
    '''
    this will grab an account object based on the idnum
    param id: idnum of the account we are trying to grab
    returns: returns account object if found, else returns None
    '''
    for i in Hand.hand_list:
        if i.__repr__() == id:
            return i
    return "none"

def main():
    # initiate game by asking how many players and shuffling the deck
    players = int(input("How many players? (1-5) > "))
    if players < 1 or players > 5:
        players = int(input("How many players? (1-5) > "))
    deck = Deck()

    # bets to be added later


    # draw hands for each player and the dealer
    for i in range(0, players + 1):
        i = Hand()
    for i in range(0, 2):
        for j in range(0, players + 1):
            get_account(j).hand.append(deck.draw_card())

    # test to see if drawing works correctly -- it does!
    # for i in range(0, players + 1):
    #     print(get_account(i).hand)
    # print(deck.cards)

    # show hands for each player and the second card for the dealer
    for i in range(0,players):
        print("Player {} draws:".format(str(i + 1)))
        get_account(i).print_hand()
    for i in range(players, players + 1):
        get_account(i).show_dealer()

    # players choose to hit or stay
    for i in range(0, players):
        hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()
        while hit_or_stay != 's' and hit_or_stay != 'h':
            hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()
        while hit_or_stay != 's':
            get_account(i).hand.append(deck.draw_card())
            print("You have:")
            get_account(i).print_hand()
            if get_account(i).calculate_score() > 21:
                print("Oh no! You bust.")
                break
            hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()
            while hit_or_stay != 's' and hit_or_stay != 'h':
                hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()

    # dealer draws on 16 or less
    while get_account(players).calculate_score() < 17:
        get_account(players).hand.append(deck.draw_card())
        print("Dealer has:")
        get_account(players).print_hand()

    # scores are compared and bets are factored in as necessary
    dealer_score = get_account(players).calculate_score()
    if dealer_score > 21:
        print("Dealer busts!")
    else:
        print("Dealer finishes with {}.".format(str(dealer_score)))
    get_account(players).print_hand()
    for i in range(0, players):
        player_score = get_account(i).calculate_score()
        if player_score > dealer_score and player_score <= 21:
            print("Congratulations Player {}, you scored {} and you win!".format(str(i + 1),str(player_score)))
        elif player_score <= 21 and dealer_score > 21:
            print("Congratulations Player {}, you scored {} and you win!".format(str(i + 1),str(player_score)))
        else:
            print("Sorry Player {}, you scored {} and you lose.".format(str(i + 1),str(player_score)))


main()
