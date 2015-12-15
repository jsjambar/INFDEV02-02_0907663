import pygame
from Node import *
from random import *

#PUT YOUR CAR STRUCTURE CODE HERE

class Car:
    def __init__(self, board):
        self.Board = board

def Update_car(self):
    newLoc = False
    while(newLoc == False):
        randomInt = randint(1,4)
        # We check if the randomInt value is equal to the one we defined, the location of the next title is part of the road AND
        # we check if we can travel there (there's no building)
        # 1 = Right, 2 = Left, 3 = Up, 4 = Down.
        # != None checks whether it's part of the road ( None = not part of road, NOT none = part of road)
        # .Traversable checks whether there is no building on the location. (0 = building in spot, 1 = no building in spot)
        if(randomInt == 1 and self.Board.Right != None and self.Board.Right.Traverseable == 1):
            newLoc = self.Board.Right
        elif(randomInt == 2 and self.Board.Left != None and self.Board.Left.Traverseable == 1):
            newLoc = self.Board.Left
        elif(randomInt == 3 and self.Board.Up != None and self.Board.Up.Traverseable == 1):
            newLoc = self.Board.Up
        elif(randomInt == 4 and self.Board.Down != None and self.Board.Down.Traverseable == 1):
            newLoc = self.Board.Down
        else:
            newLoc = False
    
    return Car(newLoc)

def isParked(self):
    if(self.Board.Park == True):
        return True
    else:
        return False
