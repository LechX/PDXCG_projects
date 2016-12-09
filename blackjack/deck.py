import random

class Deck:

    def __init__(self):
        ranks = list("A23456789TJQK")
        ranks[ranks.index("T")] = "10"
        suits = list("HSCD")
        self.cards = []

        for i in suits:
            for j in ranks:
                self.cards.append(j + i)

    def draw_card(self):
        drawn_card = self.cards[random.randint(0,len(self.cards) - 1)]
        self.cards.remove(drawn_card)
        return drawn_card
