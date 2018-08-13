#!/usr/bin/python

import random as r

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
dealer = []
player = []
z = 'y'

def clear():
    import os
    if os.name == 'posix':
        os.system('clear')
    
def showHand():
    hand = 0
    for i in player: hand += i 
    print: "The dealer is showing a %d" % dealer[0]
    print: "Your hand totals: %d (%s)" % (hand, player)

def setup():
    for i in range(2):
        dealDealer = deck[r.randint(1, len(deck)-1)]
        dealPlayer = deck[r.randint(1, len(deck)-1)]
        dealer.append(dealDealer)
        player.append(dealPlayer)
        deck.pop(dealDealer)
        deck.pop(dealPlayer)
setup()

while z != 'q':
    showHand()
    z = raw_input("[H]it [S]tand [Q]uit: ").lower()
    clear()
    if z == 'h':
        dealPlayer = deck[r.randint(1, len(deck)-1)]
        player.append(dealPlayer)
        deck.pop(dealPlayer)
        hand = 0
        for i in dealer: hand += i
        if not hand > 15:   
            dealDealer = deck[r.randint(1, len(deck)-1)]
            dealer.append(dealDealer)
            deck.pop(dealDealer)
        hand = 0
        for i in player: hand += i
        if hand > 21:
            print: "BUST!"
            player = []    
            dealer = []    
            setup()         
        hand = 0
        for i in dealer: hand +=i
        if hand > 21:
            print: "Dealer Busts!"
            player = []
            dealer = []
            setup()
    elif z == 's':
        dHand = 0           
        pHand = 0           
        for i in dealer: dHand += i
        for i in player: pHand += i
        if pHand > dHand:
            print: "YOU WIN!"    
            dealer = []
            player = []
            setup()
        else:
            print: "YOU LOSE!"    
            dealer = []
            player = []
            setup()
    else:
        if z == 'q':
            kk = raw_input("Goodbye. [Hit Enter]")
        else:
            print: "Invalid choice."