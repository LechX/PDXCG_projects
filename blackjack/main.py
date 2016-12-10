from deck import Deck
from hand import Hand

def get_deck(id):
    '''
    this will grab a hand object based on the id
    param id: id of the hand we are trying to grab
    returns: returns hand object if found, else returns None
    '''
    for i in Deck.deck_list:
        if i.__repr__() == id:
            return i
    return "none"


def get_hand(id):
    '''
    this will grab a hand object based on the id
    param id: id of the hand we are trying to grab
    returns: returns hand object if found, else returns None
    '''
    for i in Hand.hand_list:
        if i.__repr__() == id:
            return i
    return "none"


def establish_player_count():
    players = int(input("How many players? (1-5) > "))
    while players < 1 or players > 5:
        players = int(input("How many players? (1-5) > "))
    return players


def main():
    # initiate game by asking how many players and shuffling the deck
    players = establish_player_count()
    deck = Deck()

    # bets to be added later


    # draw hands for each player and the dealer
    for i in range(0, players + 1):
        i = Hand()
    for i in range(0, 2):
        for j in range(0, players + 1):
            get_hand(j).hand.append(deck.draw_card())

    # show hands for each player and the second card for the dealer
    for i in range(0,players):
        print("Player {} draws:".format(str(i + 1)))
        get_hand(i).print_hand()
    for i in range(players, players + 1):
        get_hand(i).show_dealer()
    get_deck(0).print_card_count()

    # players choose to hit or stay
    for i in range(0, players):
        hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()

        while hit_or_stay != 's' and hit_or_stay != 'h':
            hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()

        while hit_or_stay != 's':
            get_hand(i).hand.append(deck.draw_card())
            print("You have:")
            get_hand(i).print_hand()
            get_deck(0).print_card_count()

            if get_hand(i).calculate_score() > 21:
                print("Oh no! You bust.")
                break

            hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()
            while hit_or_stay != 's' and hit_or_stay != 'h':
                hit_or_stay = input("Player {}, hit or stay? (h/s) > ".format(str(i + 1))).lower()

    # dealer draws on 16 or less
    while get_hand(players).calculate_score() < 17:
        get_hand(players).hand.append(deck.draw_card())
        print("Dealer has:")
        get_hand(players).print_hand()

    # scores are compared and bets are factored in as necessary
    dealer_score = get_hand(players).calculate_score()

    if dealer_score > 21:
        print("Dealer busts!")
    else:
        print("Dealer finishes with {}.".format(str(dealer_score)))
    get_hand(players).print_hand()

    for i in range(0, players):
        player_score = get_hand(i).calculate_score()
        if player_score > dealer_score and player_score <= 21:
            print("Congratulations Player {}, you scored {} and you win!".format(str(i + 1),str(player_score)))
        elif player_score <= 21 and dealer_score > 21:
            print("Congratulations Player {}, you scored {} and you win!".format(str(i + 1),str(player_score)))
        else:
            print("Sorry Player {}, you scored {} and you lose.".format(str(i + 1),str(player_score)))


main()
