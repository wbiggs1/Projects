from __future__ import print_function, division

from Card import Card, Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def flush_suit(self):
        """Returns the suit of a flush"""
        self.suit_hist()
        for k in self.suits.keys():
            if self.suits[k] >= 5:
                return k

    def flush_hand(self):
        k = self.flush_suit()
        h = PokerHand()
        for card in self.cards:
            if card.suit == k:
                h.cards.append(card)
        return h

    def has_pair(self):
        """Returns true if the hand has a pair"""
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_two_pair(self):
        """Returns true is the hand has a two pair"""
        self.rank_hist()
        count = 0 
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >= 2:
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def number_following(self,rank):
        """Returns the number of cards following, and including a card of a certain rank
           If there is no card with the inputed rank in the hand, it returns 0"""
        n = 0
        self.rank_hist()
        try:
            self.ranks[14] = self.ranks[1]
        except KeyError:
            pass           
        """This is to ensure aces are high and low"""
        while True:
            if rank in self.ranks.keys():
                n +=1
                rank += 1
            else:
                break
        return n
               

    def most_in_a_row(self):
        """Returns highest number of cards in a row in a hand and card at start of this streak"""
        in_a_row = 0
        for i in range(1,14):
            if self.number_following(i) >= in_a_row:
                in_a_row = self.number_following(i)
                best = i
        return (in_a_row,best)

    def has_straight(self):
        """Returns whether a hand contains a straight"""
        return self.most_in_a_row()[0] >= 5

    def has_full_house(self):
        """Returns whether a hand contains a full house"""
        return self.has_two_pair() and self.has_three_of_a_kind()

    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False       

    def has_straight_flush(self):
        if self.has_flush():
            h = self.flush_hand()
            return h.has_straight()
        else:
            return False
        

##    def has_royal_flush(self):
##        if not self.has_straight_flush():
##            return False
##        else:
##            fsuit = self.flush_suit()
##            for i in range(10,14):
##                card = Card(fsuit,i)
##                if any(c == card for c in self.cards):
##                    pass
##                else:
##                    return False
##            if any(c == Card(fsuit,1) for c in self.cards):
##                return True
##            else:
##                return False

    def has_royal_flush(self):
        if self.has_flush():
            count = 0
            h = self.flush_hand()
            for card in h.cards:
                if card.rank in [1,10,11,12,13]:
                    count += 1
            return count == 5
        return False
            

    def classify(self):
        if self.has_royal_flush():
            return "Royal Flush"
        elif self.has_straight_flush():
            return "Straight Flush"
        elif self.has_four_of_a_kind():
            return "Four of a Kind"
        elif self.has_full_house():
            return "Full House"
        elif self.has_flush():
            return "Flush"
        elif self.has_straight():
            return "Straight"
        elif self.has_three_of_a_kind():
            return "Three of a Kind"
        elif self.has_two_pair():
            return "Two Pair"
        elif self.has_pair():
            return "Pair"
        else:
            return "High Card"


def test(n, n_hands=1, n_cards=7):
    """test shuffles a deck of cards, divides it into hands, classifies the
    hands, and counts the number of times various classifications appear.
    n is total number of trials
    n_hands is number of hands dealt per trial
    n_cards is number of cards per hand
    """
    hist = {"High Card":0,"Pair":0,"Two Pair":0,"Three of a Kind":0,
            "Straight":0,"Flush":0,"Full House":0,"Four of a Kind":0,
            "Straight Flush":0,"Royal Flush":0}
    
    for i in range(n):
        deck = Deck()
        deck.shuffle()
        for j in range(n_hands):
            hand = PokerHand()
            deck.move_cards(hand,7)
            hist[hand.classify()] += 1
    ratios = {}
    check = 0
    for h in hist.keys():
        ratios[h] = hist[h]/(n*n_hands)
        check += hist[h]
    if check != n * n_hands:
        return("Error with number of hands recorded: %g" % check)
    return ratios
            
            

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()
# deal the cards and classify the hands
    for i in range(1):
        hand = PokerHand()
        deck.move_cards(hand, 7)
##        hand.sort()
##        print(hand)
##        print('')
##        print(hand.classify())
##        print('')
    hand_class = ["High Card","Pair","Two Pair","Three of a Kind",
            "Straight","Flush","Full House","Four of a Kind",
            "Straight Flush","Royal Flush"]
    ratios = (test(1000000))
    for i in hand_class:
        print(i + ": %f" % (ratios[i]*100) + "%")
        
        




