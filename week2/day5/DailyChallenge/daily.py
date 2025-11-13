#### OOP Quiz
# What is a class?
## class is the blueprint of objects behaviour and attributes as they exist in memory, it is a way to define new user-defined type. 
# What is an instance?
## instance is making object from a certain class. one object is one instance. 
# What is encapsulation?
## encapsulation is the feature of combining data with methods under same roof which the class in OOP case. 
# What is abstraction?
## abstraction is the method of hiding implementation detail from the user and exposing only the what not the how. 
# What is inheritance?
## inheritance is mostly an IS-A relationship between two or more classes that include the fact that one class includes and extends another (inherits)
# What is multiple inheritance?
## multiple inheritance is when we have a child class inheriting from more than one parent class.
# What is polymorphism?
## polymorphism is about many forms, in OOP it is how methods with the same name can do different actions through overriding or overloading process. 
# What is method resolution order or MRO?
## in Python OOP concept of MRO means how python interpreter searches for methods and attributes in classes hirarchy specially in multiple inheritance cases to know which to use. 

#### Create a DECK of CARDS class
# The Deck of cards class should NOT inherit from a Card class.
# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
#  should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#  should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random 

CARDS = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

class Card:
    
    def __init__(self, value = None, suit = None):
        if value is None:
            value = random.choice(CARDS)
        if suit is None:
            suit = random.choice(SUITS)
        if value not in CARDS:
            raise TypeError(f"A Card can be only one of {CARDS}")
        if suit not in SUITS:
            raise TypeError(f"A Card Suit can be only one of {SUITS}")
        self.suit = suit
        self.value = value
    def __str__(self):
        if (self.value == 'A'):
            word = "Ace"
        elif (self.value == '2'):
            word = "Two"
        elif (self.value == '3'):
            word = "Three"
        elif (self.value == '4'):
            word = "Four"
        elif (self.value == '5'):
            word = "Five"
        elif (self.value == '6'):
            word = "Six"
        elif (self.value == '7'):
            word = "Seven"
        elif (self.value == '8'):
            word = "Eight"
        elif (self.value == '9'):
            word = "Nine"
        elif (self.value == '10'):
            word = "Ten"
        elif (self.value == 'J'):
            word = "Jack"
        elif (self.value == 'Q'):
            word = "Queen"
        elif (self.value == 'K'):
            word = "King"
        return f"{word} of {self.suit}"
    
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.value == other.value and self.suit == other.suit
    def __hash__(self):
        return hash((self.value, self.suit))
    
class Deck:
    # card_map = {'A':False, '2':False,'3':False,
    #             '4':False,'5':False,'6':False,
    #             '7':False,'8':False,'9':False,
    #             '10':False,'J':False,'Q':False,'K':False
    #             }
    def __init__(self, cards = list()):
        self.cards = cards
    
    def shuffle(self):
        while (len(self.cards) != 52):
            new_card = Card()
            if new_card not in self.cards:
                self.cards.append(new_card)
        random.shuffle(self.cards)
    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("No more cards to deal.")
        dealt_card = self.cards.pop()
        return dealt_card

# Example usage:
try:
    deck = Deck()
    deck.shuffle()
    print("Dealing 5 cards:")
    for _ in range(5):
        print(deck.deal())
except Exception as e:
    print(e)

