import pygame
from Car import *
from random import *
from Node import *
from Common import *
from Lambda_func import *

#CAR CODE HERE


class Car:
    def __init__(self, board, texture, canremove):
        self.Board = board
        self.Texture = texture
        self.CanRemove = canremove

    def Update(self):
        newLoc = False
        while(newLoc == False):
            randomInt = randint(1,4)
            removal = False

            if(randomInt == 1 and self.Board.Right != None and self.Board.Right.Traverseable == 1 and self.Board.Right.Harbor == False or
               randomInt == 1 and self.Board.Right != None and self.Board.Right.Traverseable == 1 and self.Board.Right.River == True and self.Board.Right.Bridge != None and self.Board.Right.Harbor == False):
                newLoc = self.Board.Right
            elif(randomInt == 2 and self.Board.Left != None and self.Board.Left.Traverseable == 1 and self.Board.Left.Harbor == False or
                 randomInt == 2 and self.Board.Left != None and self.Board.Left.Traverseable == 1 and self.Board.Left.River == True and self.Board.Left.Bridge != None and self.Board.Left.Harbor == False):
                newLoc = self.Board.Left
            elif(randomInt == 3 and self.Board.Up != None and self.Board.Up.Traverseable == 1 and self.Board.Up.Harbor == False or
                 randomInt == 3 and self.Board.Up != None and self.Board.Up.Traverseable == 1 and self.Board.Up.River == True and self.Board.Bridge != None and self.Board.Up.Harbor == False):
                newLoc = self.Board.Up
            elif(randomInt == 4 and self.Board.Down != None and self.Board.Down.Traverseable == 1 and self.Board.Down.Harbor == False or
                 randomInt == 4 and self.Board.Down != None and self.Board.Down.Traverseable == 1 and self.Board.Down.River == True and self.Board.Bridge != None and self.Board.Down.Harbor == False):
                newLoc = self.Board.Down
            else:
                newLoc = False

        if(newLoc.Park == True):
                removal = True    
        return Car(newLoc, self.Texture, removal)

    def canRemove(self):
        if(self.CanRemove == False):
            return self
        else:
            return False

def createNewCars(entities, entry_tile, car_texture):
    carIntGen = randint(0,1337)
    if(carIntGen % 50 == 0):
      return Node(Car(entry_tile, car_texture, False), entities)
    else:
      return entities

def draw_cars(cars, offset, screen):

    _width = int(offset / 3)

    # While the cars list is not empty.
    while not cars.IsEmpty:
        screen.blit(pygame.transform.scale(cars.Value.Texture, (_width, _width)), 
                            (_width + cars.Value.Board.Position.X * offset, 
                                _width + cars.Value.Board.Position.Y * offset))
        # To prevent from going through the same node and to continue with the next element.
        cars = cars.Tail
                   