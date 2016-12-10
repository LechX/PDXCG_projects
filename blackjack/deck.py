import random

class Deck:

    id = 0
    deck_list = []

    def __init__(self):
        ranks = list("A23456789TJQK")
        ranks[ranks.index("T")] = "10"
        suits = list("HSCD")
        self.cards = []

        for i in suits:
            for j in ranks:
                self.cards.append(j + i)
        self.id = Deck.id
        Deck.id += 1
        Deck.deck_list.append(self)


    def draw_card(self):
        drawn_card = self.cards[random.randint(0,len(self.cards) - 1)]
        self.cards.remove(drawn_card)
        return drawn_card

    def print_card_count(self):
        count = len(self.cards)
        if count == 1:
            print("1 card remaining in the deck.")
        else:
            print("{} cards remaining in the deck.".format(str(count)))

    def __repr__(self):
        return int(self.id)
