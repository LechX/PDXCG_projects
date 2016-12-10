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

    # draw hands for each player and the dealer (CARDS NOT SHOWN)
    for i in range(0, players + 1):
        i = Hand()
    for i in range(0, 2):
        for j in range(0, players + 1):
            get_hand(j).hand.append(deck.draw_card())

    # betting
    for i in range(0, players):
        bet = int(input("Player {}, how much would you like to bet? ($5-50 by $5) > ".format(str(i + 1))))
        while bet % 5 != 0 or bet < 5 or bet > 50:
            bet = int(input("Player {}, how much would you like to bet? ($5-50 by $5) > ".format(str(i + 1))))
        get_hand(i).place_bet(bet)

    # show hands for each player and the second card for the dealer
    for i in range(0,players):
        print("Player {} draws:".format(str(i + 1)))
        get_hand(i).print_hand()
    for i in range(players, players + 1):
        get_hand(i).show_dealer()
    get_deck(0).print_card_count()


    # players choose to hit, stay, double down, or split
    for i in range(0, players):
        hit_or_stay = input("Player {}, Hit, Stay, sPlit, or Double down? (h/s/p/d) > ".format(str(i + 1))).lower()
        split_hit_or_stay = ""

        while hit_or_stay != 's' and hit_or_stay != 'h' and hit_or_stay != 'p' and hit_or_stay != 'd':
            hit_or_stay = input("Player {}, Hit, Stay, sPlit, or Double down? (h/s/p/d) > ".format(str(i + 1))).lower()

        while hit_or_stay != 's':

            if hit_or_stay == 'd':
                bet = get_hand(i).bet
                get_hand(i).place_bet(bet * 2)
                get_hand(i).hand.append(deck.draw_card())
                print("You have:")
                get_hand(i).print_hand()
                if get_hand(i).calculate_score() > 21:
                    print("Oh no! You bust.")
                break

            if hit_or_stay == 'p':
                get_hand(i).split_hand.append(get_hand(i).hand[1])
                get_hand(i).hand.remove(get_hand(i).split_hand[0])
                get_hand(i).split_bet = get_hand(i).bet

                while split_hit_or_stay != 's':

                    get_hand(i).split_hand.append(deck.draw_card())
                    print("In your second hand you have:")
                    get_hand(i).print_split_hand()
                    get_deck(0).print_card_count()

                    if get_hand(i).calculate_split_score() > 21:
                        print("Oh no! You bust.")
                        break

                    split_hit_or_stay = input("Player {}, Hit or Stay? (h/s) > ".format(str(i + 1))).lower() # not allowing double down on second split hand for now, for simplicity's sake
                    while split_hit_or_stay != 's' and split_hit_or_stay != 'h':
                        split_hit_or_stay = input("Player {}, Hit or Stay? (h/s) > ".format(str(i + 1))).lower()

            get_hand(i).hand.append(deck.draw_card())
            print("You have:")
            get_hand(i).print_hand()
            get_deck(0).print_card_count()

            if get_hand(i).calculate_score() > 21:
                print("Oh no! You bust.")
                break

            hit_or_stay = input("Player {}, Hit, Stay, or Double down? (h/s/d) > ".format(str(i + 1))).lower()
            while hit_or_stay != 's' and hit_or_stay != 'h' and hit_or_stay != 'd':
                hit_or_stay = input("Player {}, Hit, Stay, or Double down? (h/s) > ".format(str(i + 1))).lower()

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
        player_bet = get_hand(i).bet
        if player_score > dealer_score and player_score <= 21:
            print("Congratulations Player {}, you scored {} and you win ${}!".format(str(i + 1), str(player_score), str(2 * player_bet)))
        elif player_score <= 21 and dealer_score > 21:
            print("Congratulations Player {}, you scored {} and you win ${}!".format(str(i + 1),str(player_score), str(2 * player_bet)))
        else:
            print("Sorry Player {}, you scored {} and you lose ${}.".format(str(i + 1),str(player_score), str(player_bet)))
        if get_hand(i).split_bet != 0:
            player_split_score = get_hand(i).calculate_split_score()
            split_bet = get_hand(i).split_bet
            if player_split_score > dealer_score and player_split_score <= 21:
                print("Congratulations Player {}, you scored {} on your split hand and you win ${}!".format(str(i + 1), str(player_split_score), str(2 * split_bet)))
            elif player_score <= 21 and dealer_score > 21:
                print("Congratulations Player {}, you scored {} on your split hand and you win ${}!".format(str(i + 1), str(player_split_score), str(2 * split_bet)))
            else:
                print("Sorry Player {}, you scored {} on your split hand and you lose ${}.".format(str(i + 1),str(player_split_score), str(split_bet)))


main()
