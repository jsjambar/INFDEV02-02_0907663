import pygame
from Car import *
from random import *
from Node import *
from Common import *
from Lambda_func import *

#CAR CODE HERE


class Boat:
    def __init__(self, board, texture, canremove):
        self.Board = board
        self.Texture = texture
        self.CanRemove = canremove

def updateBoats(boats, entry_tile, texture):   

    newBoats = Empty

    while(boats.IsEmpty == False):
        if(boats.Value.CanRemove == False):
            newBoats = Node(Boat(boats.Value.Board, boats.Value.Texture, False), newBoats)
        else:
            print("Boat has entered an harbor.")
        boats = boats.Tail

    boats = map(newBoats, lambda boat: Update_boat(boat))

    boatIntGen = randint(0,1337)
    if(boatIntGen % 50 == 0):
      boats = Node(Boat(entry_tile, texture, False), boats)
      print('new boat created.')

    return boats

def Update_boat(self):
    newLoc = False
    while(newLoc == False):
        randomInt = randint(1,4)
        removal = False

        if(randomInt == 1 and self.Board.Right != None and self.Board.Right.River == True or
           randomInt == 1 and self.Board.Right != None and self.Board.Right.Harbor == True):
            newLoc = self.Board.Right
        elif(randomInt == 2 and self.Board.Left != None and self.Board.Left.River == True or
             randomInt == 2 and self.Board.Left != None and self.Board.Left.Harbor == True):
            newLoc = self.Board.Left
        elif(randomInt == 3 and self.Board.Up != None and self.Board.Up.River == True or
             randomInt == 3 and self.Board.Up != None and self.Board.Up.Harbor == True):
            newLoc = self.Board.Up
        elif(randomInt == 4 and self.Board.Down != None and self.Board.Down.River == True or
             randomInt == 4 and self.Board.Down != None and self.Board.Down.Harbor == True):
            newLoc = self.Board.Down
        else:
            newLoc = False

    if(newLoc.Harbor == True):
            removal = True    
    return Boat(newLoc, self.Texture, removal)

def draw_boats(boat, offset, screen):
    _width = int(offset / 3)

    screen.blit(pygame.transform.scale(boat.Texture, (_width, _width)), 
                        (_width + boat.Board.Position.X * offset, 
                            _width + boat.Board.Position.Y * offset))
                        
def draw(boats, offset, screen):
    iterate(boats, lambda boat : draw_boats(boat, offset, screen))
