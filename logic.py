from enum import Enum
import random

#Allows suits to be given proper names/attributes
class Suit(Enum):
    CLUBS = 1 
    HEARTS = 2
    SPADES = 3
    DIAMONDS = 4

#Defines the idea of a card
class Card:
    rank = 5
    suit = Suit.CLUBS
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        s = ""
        if self.suit == Suit.CLUBS:
            s = "clubs"
        if self.suit == Suit.HEARTS:
            s = "hearts"  
        if self.suit == Suit.SPADES:
            s = "spades"    
        if self.suit == Suit.DIAMONDS:
            s = "diamonds"
        r = str(self.rank)
        if self.rank == 11:
            r = "jack"
        if self.rank == 12:
            r = "queen"
        if self.rank == 13:
            r = "king"
        if self.rank == 14:
            r = "ace"
        return r + " of " + s
    __repr__ = __str__
    
    
    
    def beats(self, c):
        return self.suit == c.suit and self.rank > c.rank
        
#Deck of cards
class Deck:
    all_cards = []
    for s in range(1, 5):
        for r in range(5, 15):
            c = Card(r, Suit(s))
            all_cards.append(c)
    def deal(self):
        h1 = Player()
        h2 = Player()
        h3 = Player()
        h4 = Player()
        while self.all_cards:
            c = random.choice(self.all_cards)
            h1.add_card(c)
            self.all_cards.remove(c)
            c = random.choice(self.all_cards)
            h2.add_card(c)
            self.all_cards.remove(c)
            c = random.choice(self.all_cards)
            h3.add_card(c)
            self.all_cards.remove(c)
            c = random.choice(self.all_cards)
            h4.add_card(c)
            self.all_cards.remove(c)           
        return (h1, h2, h3, h4)

#Defines the idea of a hand of cards (player) (in this case the cards held)
class Player:
    def __init__(self):
        self.cards_held=[]
        self.score = 0 
    def add_card(self, c):
        self.cards_held.append(c)
        
class Round:
    def __init__(self, players, cards):
        self.players = players
        self.cards = cards

    
 
#Barbu game (actual game not name)    
class Barbu:
    def play(self, r):
        winner = 0
        wc = r.cards[0]
        if r.cards[1].beats(wc):
            winner = 2
            wc = c2 
        if c3.beats(wc):
            winner = 3
            wc = c3
        if c4.beats(wc):
            winner = 4
            wc = c4
        return winner, wc
    def checkbarbu(self, c1, c2, c3, c4):
        if c1.rank == 13 and c1.suit == Suit.HEARTS:
            return -40
        if c2.rank == 13 and c2.suit == Suit.HEARTS:
            return -40
        if c3.rank == 13 and c3.suit == Suit.HEARTS:
            return -40
        if c4.rank == 13 and c4.suit == Suit.HEARTS:
            return -40
        return 0
        
    
#Tests game logic code ^ - won't need when done(will be in main.py)
if __name__ == '__main__':
    
    
    c1 = Card(3, Suit.CLUBS)
    c2 = Card(7, Suit.CLUBS)
    c3 = Card(13, Suit.HEARTS)
    c4 = Card(5, Suit.CLUBS)
    
    b = Barbu()
   # w = b.play(c1, c2, c3, c4)
   # print(w)
    
    s = b.checkbarbu(c1, c2, c3, c4)
    print(s)
    
    d = Deck()
    print(d.all_cards)
    
    h1, h2, h3, h4 = d.deal()
    print(h1.cards_held)
    print(h2.cards_held)
    print(h3.cards_held)
    print(h4.cards_held)
