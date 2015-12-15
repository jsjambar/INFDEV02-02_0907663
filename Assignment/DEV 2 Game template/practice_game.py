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
car_list = Node(Car(board), Empty)

def Update(cars):
   
  cars = filter(cars, lambda car: not isParked(car))
  cars = map(cars, lambda car: Update_car(car))

 
  # If you get a non-decimal number if you divide by 12, we add a new node with the car node as value and list as tail.
  carIntGen = randint(0,1337)
  if(carIntGen % 12 == 0):
      cars = Node(Car(board), cars)
      print('New car created.')

  # Return cars.
  return cars


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
    time.sleep(0.1)
    
# Run the Main function.
Main(car_list)