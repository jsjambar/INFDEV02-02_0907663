import time
from threading import Thread
import os, pygame
import time
import random
from Tile import *
from Node import *
from Car  import *
from lambda_functions import *


pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 60
board_size = 10
car_texture = pygame.image.load("Content\car.png").convert()
board = build_square_matrix(board_size, offset)

# List that starts with empty, this is to prevent an infinite loop and to have a base value.
# We place our cars in this variable.
car_list = Empty

counter = 0
# A loop so we can add 3 cars to our list.
while counter < 3:
    car_list = Node(Car(board), car_list)
    counter+=1

def Update(cars):

#TODO: add the logic of your cars here
#HINT For filtering reasons we return a list (of cars?)
  # List where the first value is empty (this is at the bottom when new cars are added to it.
  newLocatedCars = Empty
  # While the list we created at the start is not empty.
  while not cars.IsEmpty:
      # If the current tile has the value 'FALSE' for the Park attribute...
      if(cars.Value.Board.Park == False):
          # We give a variable the FALSE value for the base value.
          newLoc = False
          # While the newLoc variable is FALSE (which we defined above), we do the following:
          while(newLoc == False):
              # We place a random integer between 1 and 4 in the randomInt variable
              randomInt = random.randint(1, 4)
              # We check if the randomInt value is equal to the one we defined, the location of the next title is part of the road AND
              # we check if we can travel there (there's no building)
              # 1 = Right, 2 = Left, 3 = Up, 4 = Down.
              # != None checks whether it's part of the road ( None = not part of road, NOT none = part of road)
              # .Traversable checks whether there is no building on the location. (0 = building in spot, 1 = no building in spot)
              if(randomInt == 1 and cars.Value.Board.Right != None and cars.Value.Board.Right.Traverseable == 1):
                  newLoc = cars.Value.Board.Right
              elif(randomInt == 2 and cars.Value.Board.Left != None and cars.Value.Board.Left.Traverseable == 1):
                  newLoc = cars.Value.Board.Left
              elif(randomInt == 3 and cars.Value.Board.Up != None and cars.Value.Board.Up.Traverseable == 1):
                  newLoc = cars.Value.Board.Up
              elif(randomInt == 4 and cars.Value.Board.Down != None and cars.Value.Board.Down.Traverseable == 1):
                  newLoc = cars.Value.Board.Down
              else:
                  # In case we don't land on any of the above if-statements
                  newLoc = False

          # If we have a new location for our car, 
          # we make a new node with the car class and the board list as value and add it to the newLocatedCars list
          if(newLoc):
            newLocatedCars = Node(Car(newLoc), newLocatedCars)

       
      # If you get a non-decimal number if you divide by 5, we add a new node with the car node as value and list as tail.
      carIntGen = random.randint(0,1337)
      if(carIntGen % 12 == 0):
        newLocatedCars = Node(Car(board), newLocatedCars)
        print('New car created.')
      # To prevent from going through the same node, we make the cariable that we run through the current node's tail.
      cars = cars.Tail

  # return the list of cars.
  return newLocatedCars


def Draw(cars, screen):
#TODO: add the draw of your cars below
#
# Use the following code to draw your car. 
# HINT: POSITION_X and POSITION_Y represent the position of the car to draw on the screen   
    _width = int(offset / 3)

    # While the cars list is not empty.
    while not cars.IsEmpty:
        screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                            (_width + cars.Value.Board.Position[0] * offset, 
                             _width + cars.Value.Board.Position[1] * offset))
        # To prevent from going through the same node and to continue with the next element.
        cars = cars.Tail
                        
    print("<3")



def Main(cars):
  start = time.time()

  while True:    
    screen.fill(green)  
    board.Reset()
    board.Draw(screen)

    cars = Update(cars)
    Draw(cars, screen)

    pygame.display.flip()
    time.sleep(1)
    
# Run the Main function.
Main(car_list)