#Michael Santoro
#COMP 3008 - Project 3
##Old Maid (as described from bicyclecards.com)##
#The Pack
#The standard 52-card pack is used, however, one of the four queens is removed, leaving a total of 51 cards.
#Object of the Game
#The goal is to form and discard pairs of cards, and not to be left with the odd card (a queen) at the end.
#The Deal
#Any player shuffles the pack and deals them around, one at a time to each player, until all the cards have been
#handed out. Players do not need to have an equal number of cards.
#The Play
#Each player removes all pairs from his hand face down. If a player has three-of-a-kind, they remove only two of
#those three cards. The dealer then offers their hand, spread out face down, to the player on the left, who draws one
#card from it. This player discards any pair that may have been formed by the drawn card. The player then offers
#their own hand to the player on their left. Play proceeds in this way until all cards have been paired except one
#- the odd queen, which cannot be paired - and the player who has that card is the Old Maid!

#Import
import random

#Define a Class
class card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

#Add a Method
class player:
    def __init__(self):
        self.hand = []
        self.pile = []
        self.handValues = []
    def addCardtoHand(self, card):
        if card.value not in self.handValues:
            self.handValues.append(card.value)
            self.hand.append(card)
        else:
            for a in self.hand:
                if card.value == a.value:
                    self.discardpair(self, a, card)

    def removeCardfromHand(self, card):
        self.hand.remove(card)
    def discardpair(self, card1, card2):
        self.pile.append((card1,card2))
    def checkForPair(self, checkCard):
        for b in self.hand:
            if checkCard.value == b.value:
                self.discardpair(self,checkCard,b)
                self.removeCardfromHand(self, b)
    def handCount(self):
        return len(self.hand)
    def printHand(self):
        for c in self.hand:
            print(c.value,c.suit)

class deck:
    #Deck Object with all 52 cards
    #Full list of 52 cards

    def __init__(self):
        self.deck = []
    def addCardtoDeck(self,card):
        self.deck.append(card)
    def removeCardfromDeck(self,card):
        for d in self.deck:
            if d.suit == card.suit and d.value == card.value:
                self.deck.remove(d)
    def createDeck(self):
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        for value in values:
            for suit in suits:
                e = card(value,suit)
                self.deck.append(e)
    def drawCardFromDeck(self):
        randomInt = random.randint(0,len(self.deck)-1)
        #Might need a Deep Copy Here
        #Deep Copy
        returnCard = card(self.deck[randomInt].value, self.deck[randomInt].suit)
        self.removeCardfromDeck(self.deck[randomInt])
        return returnCard
    def deckCount(self):
        return len(self.deck)




def main():
    oldMaid = card('Q','S')
    #Create Deck
    gameDeck = deck()
    gameDeck.createDeck()
    #Remove Old Maid from Deck
    gameDeck.removeCardfromDeck(oldMaid)
    print(gameDeck.deckCount())
    #Create Players
    user = player()
    comp = player()
    #Deal Cards
    flag = True
    while(gameDeck.deckCount() > 1):
        if flag:
            print(gameDeck.deckCount())
            user.addCardtoHand(gameDeck.drawCardFromDeck())
            flag = False
        else:
            print(gameDeck.deckCount())
            comp.addCardtoHand(gameDeck.drawCardFromDeck())
            flag = True
    user.printHand()
    print(len(user.hand),user.handValues)
    comp.printHand()
    print(len(comp.hand),comp.handValues)



main()
