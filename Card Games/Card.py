from __future__ import print_function, division

import random

import copy


class Card:
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2, face='up'):
        self.suit = suit
        self.rank = rank
        self.face = face

    def __str__(self):
        """Returns a human-readable string representation."""
        if self.face == 'up':
            return '%s of %s' % (Card.rank_names[self.rank],
                                 Card.suit_names[self.suit])
        else:
            return 'Facedown card'

    def __eq__(self, other):
        """Checks whether self and other have the same rank and suit.

        returns: boolean
        """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.

        returns: boolean
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def face_up(self):
        self.face = 'up'

    def face_down(self):
        self.face = 'down'


class Deck:
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    
    def __init__(self):
        """Initializes the Deck with 52 cards.
        """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck.

        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.
        
        card: Card
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self,n_hands,n_cards):
        hands = []
        for i in range(n_hands):
            hand = Hand()
            deck.move_cards(hand,n_cards)
            hands.append(copy.deepcopy(hand))
        return hands

    def count_cards(self):
        count = 0
        for card in self.cards:
            count += 1
        return count
            


class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    
##    hands = deck.deal_hands(5,5)
##    for hand in hands:
##        print(hand)
##        print('')

##card = Card(2,3,'down')
##print(card)
##card.face_up()
##print(card)


##    hand = Hand()
##    print(find_defining_class(hand, 'shuffle'))
##
##    deck.move_cards(hand, 5)
##    hand.sort()
##    print(hand)
