#Michael Santoro
#COMP 3008 - Project 4

#Import
import random

#Define a Class
class dice:
    def __init__(self,sides):
        self.sides = sides
        self.value = self.roll()
        self.money = 1500

    def __str__(self):
        s = f'You have: ${self.money} Your Roll was: {self.value}'
        return self.money

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
        if self.value > other.value:
            return True
        else:
            NotImplemented

    #Less Than Equal
    def __le__(self, other):
        if self.value <= other.value:
            return True
        else:
            NotImplemented

    #Greater Than Equal
    def __ge__(self, other):
        if self.value >= other.value:
            return True
        else:
            NotImplemented

    def __add__(self, other):
        if self.value == other.value:
            self.money = self.money
        
    def roll(self):
        self.value = random.randint(1,self.sides)
        return self.value






