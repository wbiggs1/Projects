from __future__ import print_function, division

from Card import Card, Hand, Deck

import copy

import dbm
    

class BlackjackHand(Hand):
    """Represents a blackjack hand. """

    def score(self):
        """ Gives a list of possible scores of a Blackjack hand """
        scores = [0]
        for card in self.cards:
            if card.rank == 1:
                scores.append(scores[-1] + 10)
            if card.rank <= 9:
                for i in range(len(scores)):
                    scores[i] += card.rank
            else:
                for i in range(len(scores)):
                    scores[i] += 10
        newscores = []
        for i in range(len(scores)):
            if scores[i] <= 21:
                newscores.append(scores[i])
        return newscores

    def best_score(self):
        """Returns best score of a Blackjack hand"""
        return self.score()[-1] if len(self.score()) else 'BUST'

    def hard_score(self):
        """Gives score of Blackjack hand with ace being 11"""
        n = 0
        for card in self.cards:
            if card.rank <= 9:
                n += card.rank
            else:
                n += 10
        return n

    def is_hard(self):
        """Returns True if a hand is hard, i.e. no aces with value 1 """
        return self.best_score() == self.hard_score()

    def is_blackjack(self):
        return True if self.best_score() == 21 and self.count_cards() == 2 else False

    def is_bust(self):
        return False if len(self.score()) else True

    def print_score(self):
        if self.is_blackjack():
            return 'BLACKJACK!'
        elif self.is_bust():
            return 'BUST'
        else:
            return self.score()[-1]
    
    def __lt__(self,other):
        if self.is_blackjack() or other.is_bust():
            return False
        else:
            if other.is_blackjack() or self.is_bust():
                return True
            else:
                return self.best_score() < other.best_score()

            

    def twist(self,deck):
        """Moves a card from the deck to the hand"""
        deck.move_cards(self,1)

    def is_pair(self):
        if self.count_cards() == 2:
            ranks = []
            for card in self.cards:
                ranks.append(card.rank)
            if ranks[0] == ranks[1]:
                return True
            elif ranks[0] in [10,11,12,13] and ranks[1] in [10,11,12,13]:
                return True
        return False


def deal(n,deck):
    """Deals n hands. Returns a list of these hands. Takes hand and deck as inputs"""
    hands = []
    deck.shuffle()
    for i in range(n):
        hand = BlackjackHand()
        deck.move_cards(hand,2)
        hands.append(hand)
    return hands

def print_most(dealers,players):
    """Prints dealer's and player's hands, as well as player's score"""
    print("Dealer's hand:")
    print(dealers)
    print('')
    print("Player's hand:")
    print(players)
    print("Player's score:")
    print(players.print_score())
    print('')

def print_all(dealers,players):
    """Prints dealer's and player's hands and scores"""
    print("Dealer's hand:")
    print(dealers)
    print("Dealer's score:")
    print(dealers.print_score())
    print("Player's hand:")
    print(players)
    print("Player's score:")
    print(players.print_score())
    print('')

    
def dealers_choice(dealers):
    """The dealer hits on anything lower than a hard 17 or soft 18"""
    if dealers.best_score() == 'BUST':
        return False
    else:
        if dealers.is_hard():
            if dealers.best_score() < 17:
                return True
        if dealers.best_score() < 18:
            return True
        return False

"""Store the amount in the player's stack in a text file"""

def read_stack():
    """Outputs the value of the player's stack (which is stored under the first
    line of the text file stack.txt """
    f = open('stack.txt','r')
    stack = f.read()
    stack = int(stack)
    f.close()
    return stack

def write_stack(stack):
    f = open('stack.txt','w')
    stack = str(stack)
    f.write(stack)
    f.close()


def players_hand(deck,hand, dealers):
    while hand.best_score() != 'BUST':
        if hand.is_blackjack():
            break
        print("Would you like to hit or stand?")
        print(">>> ", end='')
        entry = input()
        if entry.lower() == 'hit':
            hand.twist(deck)
            print_most(dealers,hand)
        else:
            dealers.cards[0].face_up()
            print_all(dealers,hand)
            print('')
            break
    return hand

def evaluate_hands(hand,dealers_hand,stack,bet):
    print_all(dealers_hand,hand)
    if hand.is_blackjack():
        if dealers_hand.is_blackjack():
            print("STAND-OFF")
            new_stack = stack
        else:
            print("BLACKJACK! YOU WIN!")
            new_stack = int(stack + bet*1.5)
    elif dealers_hand < hand:
        new_stack = int(stack + bet)
        print('YOU WIN!')
    else:
        new_stack = int(stack - bet)
        print('YOU LOSE!')
    write_stack(new_stack)

def dealers_hand(deck,dealers):
    while True:
        if dealers_choice(dealers):
            deck.move_cards(dealers,1)
        else:
            break

def play_hand(deck):
    stack = read_stack()
    while True:
        print("Player's stack is currently: %d" % stack)
        print("How much would you like to bet?")
        print(">>> ", end='')
        try:
            bet = int(input())
            if bet < 0 or bet > stack:
                print("Please enter an integer less than your total stack")
            else:
                break
        except ValueError:
            print("Please enter an integer less than your total stack")    
    hands = deal(2,deck)
    dealers = hands[0]
    players = hands[1]
    dealers.cards[0].face_down()
    print_most(dealers,players)
    while True:
        if players.is_pair():
            print("Would you like to split your pair? Please answer yes or no.")
            print(">>> ", end='')
            split = input()
            if split.lower() == 'yes':
                players1 = BlackjackHand()
                players.move_cards(players1,1)
                players2 = BlackjackHand()
                players.move_cards(players2,1)
                print('Splitting Hands:\n')
                print('HAND 1\n')
                players1 = players_hand(deck,players1,dealers)
                print('HAND 2\n')
                players2 = players_hand(deck,players2,dealers)
                print("Final Hands")
                bet = int(bet/2)
                dealers_hand(deck,dealers)
                evaluate_hands(players1,dealers,stack,bet)
                evaluate_hands(players2,dealers,stack,bet)
                stack = read_stack()
                print('')
                break
        players = players_hand(deck,players,dealers)
        dealers.cards[0].face_up()
        dealers_hand(deck,dealers)
        print("Final Hands:")
        evaluate_hands(players,dealers,stack,bet)
        break
    stack = read_stack()
    print('')


    

def shell():
    deck = Deck()
    deck.shuffle()
    while True:
        if deck.count_cards() > 15:
            play_hand(deck)
        else:
            deck = Deck()
            deck.shuffle()
            print("Reshuffling deck")
        print("Press enter to play another hand or type 'Quit' to exit")
        print(">>> ", end='')
        ans = input()
        if ans.lower() == 'quit':
            break
        

if __name__ == '__main__':
    shell()
