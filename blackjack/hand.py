
class Hand:

    '''
    this will grab a hand object based on the id
    param id: id of the hand we are trying to grab
    returns: returns hand object if found, else returns None
    '''
    id = 0
    hand_list = []


    def __init__(self):
        self.hand = []
        self.split_hand = []
        self.bet = 0
        self.split_bet = 0
        self.id = Hand.id
        Hand.id += 1
        Hand.hand_list.append(self)


    def print_hand(self):
        for i in self.hand:
            print(i)


    def print_split_hand(self):
        for i in self.split_hand:
            print(i)


    def show_dealer(self):
        print("Dealer draws:")
        for i in range(0, 1):
            print("XX")
        for i in range(1, 2):
            print(self.hand[i])


    def place_bet(self, amount):
        self.bet = amount


    def calculate_score(self):
        self.hand.sort()
        ranks = list("A234567891JQK") # 10 is 1 here to correspond w/ index[0]
        values = []
        for i in range(1,14):
            if i < 10:
                values.append(i)
            else:
                values.append(10)
        score = 0
        hand_length = len(self.hand)

        # sort so As are at the end to simplify addition (first append, then remove)
        for i in range(0, hand_length):
            if self.hand[i][0] == 'A':
                self.hand.append(self.hand[i])

        for i in range(hand_length - 1, 0, -1):
            if self.hand[i][0] == 'A':
                self.hand.remove(self.hand[i])

        # sum score starting with non-As, then add As individually, basing value on score up to that point
        for i in self.hand:
            if i[0] != 'A':
                score = score + values[ranks.index(i[0])]
            else:
                if score > 10: # this would break in the case of having 5 4 A A A (will sum to 22)
                    score = score + 1
                else:
                    score = score + 11

        return score


    def calculate_split_score(self):
        self.split_hand.sort()
        ranks = list("A234567891JQK") # 10 is 1 here to correspond w/ index[0]
        values = []
        for i in range(1,14):
            if i < 10:
                values.append(i)
            else:
                values.append(10)
        score = 0
        hand_length = len(self.split_hand)

        # sort so As are at the end to simplify addition (first append, then remove)
        for i in range(0, hand_length):
            if self.split_hand[i][0] == 'A':
                self.split_hand.append(self.split_hand[i])

        for i in range(hand_length - 1, 0, -1):
            if self.split_hand[i][0] == 'A':
                self.split_hand.remove(self.split_hand[i])

        # sum score starting with non-As, then add As individually, basing value on score up to that point
        for i in self.split_hand:
            if i[0] != 'A':
                score = score + values[ranks.index(i[0])]
            else:
                if score > 10: # this would break in the case of having 5 4 A A A (will sum to 22)
                    score = score + 1
                else:
                    score = score + 11

        return score


    def __repr__(self):
        return int(self.id)
