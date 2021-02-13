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
    def addCardtoHand(self, card):
        self.hand.append(card)
    def removeCardfromHand(self, card):
        self.hand.remove(card)
    def discardpair(self,card1, card2):
        self.pile.append((card1,card2))
    def checkForPair(self):
        firstCard = self.hand[0]
        for c in self.hand[1:]:
            if firstCard.value == c.value:
                self.discardpair(self,firstCard,c)
                self.removeCardfromHand(self, firstCard)
                self.removeCardfromHand(self, c)
                

class deck:
    #Deck Object with all 52 cards
    #Full list of 52 cards
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['H', 'C', 'S', 'D']
    def __init__(self):
        self.deck = []
    def addCardtoDeck(self,card):
        self.deck.append(card)
    def removeCardfromDeck(self,card):
        for c in self.deck:
            if c.suit == card.suit
        self.deck.remove(card)
    def createDeck(self):
        for value in values:
            for suit in suits:
                c = card(value,suit)
                self.deck.append(c)




def main():
    for value in values:
        for suit in suits:
            c = card(value,suit)
            deck.append(c)
            print(c.value,c.suit)
    print(deck)
    oldMaid = card('Q','S')
    print(oldMaid.value,oldMaid.suit)

    print(len(deck))


main()
