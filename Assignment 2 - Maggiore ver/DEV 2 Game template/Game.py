import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *
from Boat import *
pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 50
size = 10
entry_road, entry_rivers, bridges = build_scene(size, offset)

#faces to the right
boat_texture = pygame.image.load("Content/tanker.png").convert_alpha()

#faces to the right
car_texture = pygame.image.load("Content/car.png").convert_alpha()

car_list = Empty
boat_list = Empty
print(entry_road)
asdf
counter = 0
while counter < 3:
    car_list = Node(Car(entry_road.Value, car_texture, False), car_list)
    boat_list = Node(Boat(entry_rivers.Value, boat_texture, False), boat_list)
    counter+=1

def updateEntities(entities):   
    entities = filter(entities, lambda e: not e.canRemove())
    entities = map(entities, lambda e: e.Update())
    return entities

def drawEntities(entities):   
    entities = filter(entities, lambda e: not e.canRemove())
    entities = map(entities, lambda e: e.Update())
    return entities

def Main(cars, boats, offset, screen):
  start = time.time()

  while True:    
    pygame.event.get()
    screen.fill(green)

    #here we draw the board, do not move
    _board = entry_road

    while not _board.IsEmpty:
      _board.Value.Draw(screen, False)
      _board = _board.Tail

    #here we draw the bridges, do not move
    _board = bridges

    while not _board.IsEmpty:
      _board.Value.Draw(screen, True)
      _board = _board.Tail

    entities = updateEntities(entities)
    drawEntities(entities, offset, screen)
    
    pygame.display.flip()
    time.sleep(0.2)
    
Main(car_list, boat_list, offset, screen)