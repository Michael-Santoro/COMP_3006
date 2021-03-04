#Michael Santoro
#COMP 3008 - Project 4

#Import
import random

#Define a Class
#Dice Class
class dice:
    def __init__(self,sides):
        self.sides = sides
        self.value = 1

    def __str__(self):
        s = self
        return s

    #Equals
    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            NotImplemented
    #Not Equal
    def __ne__(self, other):
        if self.value != other.value:
            return True
        else:
            NotImplemented
    #Less Than
    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            NotImplemented

    #Greater Than
    def __gt__(self, other):
        if type(self) == type(other):
            if self.value > other.value:
                return True
            else:
                NotImplemented

    #Less Than Equal
    def __le__(self, other):
        if type(self) == type(other):
            if self.value <= other.value:
                return True
            else:
                NotImplemented

    #Greater Than Equal
    def __ge__(self, other):
        if type(self) == type(other):
            if self.value >= other.value:
                return True
            else:
                NotImplemented

    def __add__(self, other):
        if type(self) == type(other):
            self.value = self.value + other.value
        else:
            NotImplemented

    def roll(self):
        self.value = random.randint(1,self.sides)
        print(f'    Die Value: {self.value}')
        return self.value

#A "Cup of Dice" class
class cupOfDice:
    def __init__(self, diceQty, sides):
        self.cup = []
        self.lastRoll = []
        self.sum = 0
        for i in range(diceQty):
            self.cup.append(dice(sides))

    def __str__(self):
        s = f'{self.sum}'
        return s

    #Equals
    def __eq__(self, other):
        if self.sum == other.sum:
            return True
        else:
            NotImplemented
    #Not Equal
    def __ne__(self, other):
        if self.sum != other.sum:
            return True
        else:
            NotImplemented
    #Less Than
    def __lt__(self, other):
        if self.sum < other.sum:
            return True
        else:
            NotImplemented
    #Greater Than
    def __gt__(self, other):
        if self.sum > other.sum:
            return True
        else:
            NotImplemented

    #Less Than Equal
    def __le__(self, other):
        if self.sum <= other.sum:
            return True
        else:
            NotImplemented

    #Greater Than Equal
    def __ge__(self, other):
        if self.sum >= other.sum:
            return True
        else:
            NotImplemented

    def cupRoll(self):
        self.lastRoll = []
        for die in self.cup:
            r = die.roll()
            self.sum += r
            self.lastRoll.append(r)
        return self.sum

class player:
    def __init__(self,qtyOfDice,sidesOnDie):
        self.money = 1500
        self.cup = cupOfDice(qtyOfDice,sidesOnDie)
    def __str__(self):
        return str(self.money)

def main():
    qtyDice = input(f'Welcome To Dice War Game\nEnter the number of '
                    f'dice you would like to play with\n')
    numSides = input(f'Enter the number of sides you would like the die to have?\n')
    user = player(int(qtyDice),int(numSides))
    computer = player(int(qtyDice),int(numSides))
    while user.money >0:
        wager = input(f'You have: ${user} to wager. How much would you like to wager?\n')
        print('Your Rolls:')
        user.cup.cupRoll()
        print('Computer Rolls:')
        computer.cup.cupRoll()
        if user.cup.sum > computer.cup.sum:
            user.money += int(wager)
        else:
            user.money -= int(wager)
        print(f'Your sum was: {user.cup.sum}; and the Computers sum was: {computer.cup.sum}')





main()

