#Michael Santoro
#COMP 3008 - Project 5


def main():
    cards = []
    suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    initialValues = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    for val in initialValues:
        value = []
        value.append(val)
        value.append(val)
        value.append(val)
        value.append(val)
        cards.extend(list(zip(value,suits)))
    print(cards)


main()
