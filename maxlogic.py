"""gonna try my own keep it simple stupid attempt of barbu game"""
import random
#import pygame
#from pygame.locals import *

"""First, to create a deck of cards (which in Barbu goes from 5 - Ace)"""
def CreateDeck():
    #These are all the list holders for the deck of cards
    cardvalues = []
    royals = ["Jack", "Queen", "King", "Ace"]
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    deck = []
    
    #This creates a card from 5-10 and 'royal' cards and puts them in the empty cardvalues list
    for i in range(5,11):
        cardvalues.append(str(i))
    for j in range(4):
        cardvalues.append(royals[j])
    #print(cardvalues)
        
    #This will 'attach' the suits to the card values and add them to the 'deck' list
    for k in range(4):
        for l in range(10):
            cards = (cardvalues[l] +  " of " + suits[k])
            deck.append(cards)
    #print(deck)
    
    #This will shuffle the deck of cards
    random.shuffle(deck)
    #print(deck)
    return deck

CreateDeck()

"""Now to deal out cards to create the players' hands"""
def DealCards(deck):
    #This creates the player's hand as an empty list
    player1_hand = []
    player2_hand = []
    player3_hand = []
    player4_hand = []
    
    #Each player needs 10 cards, and there are 40 cards in the deck. This will add 10 cards from the shuffled deck into each player's hand
    for m in range(10):
        player1_hand.append(deck[m])
    for n in range(10,20):
        player2_hand.append(deck[n])
    for o in range(20,30):
        player3_hand.append(deck[o])
    for p in range(30,40):
        player4_hand.append(deck[p])
        
    print(deck)
    print(player1_hand)
    print(player2_hand)
    print(player3_hand)
    print(player4_hand)
    
DealCards([deck])

"""In order for a game to be played, a round needs to be defined"""
def Round():
    print("whoops ill do this later")

"""Now to create the logic for the actual game and playing a round"""
"""def PlayBarbu():
    starter = random.randint(1,4)
    print("Player {} starts!".format(starter))
    if starter == 1:
        #print(player1_hand)
        play_card = input("What card would you like to play? ").lower()
        print(play_card)"""
        
"""Need to create somoe program to use for test data for standard"""

            
        
