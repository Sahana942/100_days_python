'''There are fifty-two cards in a deck, each of which belongs to one of four suits and one of
thirteen ranks. The suits are Spades, Hearts, Diamonds, and Clubs (in descending order in
bridge). The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Depending on
the game that you are playing, an Ace may be higher than King or lower than 2.'''
import random
class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def __str__(self):
        return "%s of %s" %(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

    def __gt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 > t2

card1 = Card(2, 8)
card2 = Card(3, 6)
print(card1,"\n",card2)
print(card1 > card2)

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()

deck = Deck()
print(deck)
print("====popping====")
deck.pop_card()
print(deck)

print("====adding card1 and card2====")
deck.add_card(card1)
deck.add_card(card2)
print(deck)

print("====sorting====")
deck.sort()
print(deck)

print("====shuffling====")
deck.shuffle()
print(deck)

print("====again sorting====")
deck.sort()
print(deck)

print("====inheritance starts here====")
class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def move_cards(self, hand, num):
        #print("------------")
        for i in range(num):
            print("------------")
            hand.add_card(card1)
            print(i)
            

hand = Hand('new hand')
print(hand.cards,hand.label)

print("====popping in hand via deck's function which is inherited====")
card = deck.pop_card()
print(deck)

print("====adding a card in deck via deck's function which is inherited====")
deck.add_card(card1)
print(deck)

print("====adding a card in hand via deck's function which is inherited====")
hand.add_card(card1)
print(deck)

print("whats in the hand?")
print(hand)

print("moving")
hand.move_cards(hand,5)
print(hand)
print("final deck")
print(deck)
