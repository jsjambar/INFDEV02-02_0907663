import time
from threading import Thread
import os, pygame
import time
import random
from Tile import *
from Node import *
from Car  import *


pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 60
board_size = 10
car_texture = pygame.image.load("Content\car.png").convert()
board = build_square_matrix(board_size, offset)

car_list = Empty
counter = 0
while counter < 3:
    car_list = Node(Car(board), car_list)
    counter+=1

def Update(cars):

#TODO: add the logic of your cars here
#HINT For filtering reasons we return a list (of cars?)
  newLocatedCars = Empty
  while not cars.IsEmpty:
      if(cars.Value.Board.Park == False):
          newLoc = False
          while(newLoc == False):
              randomInt = random.randint(1, 4)
              if(randomInt == 1 and cars.Value.Board.Right != None and cars.Value.Board.Right.Traverseable == 1):
                  newLoc = cars.Value.Board.Right
              elif(randomInt == 2 and cars.Value.Board.Left != None and cars.Value.Board.Left.Traverseable == 1):
                  newLoc = cars.Value.Board.Left
              elif(randomInt == 3 and cars.Value.Board.Up != None and cars.Value.Board.Up.Traverseable == 1):
                  newLoc = cars.Value.Board.Up
              elif(randomInt == 4 and cars.Value.Board.Down != None and cars.Value.Board.Down.Traverseable == 1):
                  newLoc = cars.Value.Board.Down
              else:
                  newLoc = False

          if(newLoc):
            newLocatedCars = Node(Car(newLoc), newLocatedCars)

      cars = cars.Tail
        
  return newLocatedCars


def Draw(cars, screen):
#TODO: add the draw of your cars below
#
# Use the following code to draw your car. 
# HINT: POSITION_X and POSITION_Y represent the position of the car to draw on the screen   
    _width = int(offset / 3)

    while not cars.IsEmpty:
        screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                            (_width + cars.Value.Board.Position[0] * offset, 
                             _width + cars.Value.Board.Position[1] * offset))
        cars = cars.Tail
                        
    print("<3")



def Main(cars):
  start = time.time()
  timer = 0

  while True:    
    screen.fill(green)  
    board.Reset()
    board.Draw(screen)

    cars = Update(cars)
    Draw(cars, screen)

    pygame.display.flip()
    time.sleep(1)

    timer += 1

    print(timer)

    if(timer % 5 == 0):
        cars = Node(Car(board), cars)

    
    
Main(car_list)