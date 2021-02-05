
#Define a Class
class card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

#Add a Method
class hand:
    def __init__(self):
        self.hand = []
    def addCardtoHand(self, card):
        self.hand.append(card)
    def removeCardfromHand(self, card):
        self.hand.remove(card)

class discard:
    def __init__(self):
        self.pile = []
    def discardpair(self,card1, card2):
        self.pile.append((card1,card2))

class deck:
    def __init__(self):
        self.deck = []
    def addCardtoDeck(self,card):
        self.deck.append(card)
    def removeCardfromDeck(self,card):
        self.deck.remove(card)




def main():
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['H', 'C', 'S', 'D']
    for value in values:
        for suit in suits:
            c = card(value,suit)
            d = deck()
            deck.addCardtoDeck(d,c)
            print(c.value,c.suit)
    oldMaid = card('Q','S')
    deck.removeCardfromDeck(d, oldMaid)


main()
