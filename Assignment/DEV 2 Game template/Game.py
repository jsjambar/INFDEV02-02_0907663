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
while counter < 1:
    car_list = Node(Car(random.uniform(0.1, 5), random.uniform(0.1,5)), car_list)
    counter+=1

def Update(cars):

#TODO: add the logic of your cars here
#HINT For filtering reasons we return a list (of cars?)
  newLocatedCars = Empty
  while not cars.IsEmpty:
      newLocatedCars = Node(Car(cars.Value.X + 0.1, cars.Value.Y), newLocatedCars)
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
                            (_width + cars.Value.X * offset, 
                            _width + cars.Value.Y * offset))
        cars = cars.Tail
        print(board)
                        
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
    
Main(car_list)