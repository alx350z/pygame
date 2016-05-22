#!/usr/bin/python3

import pygame
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False

carImg = pygame.image.load('racecar.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))
    
x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += -10
            if event.key == pygame.K_RIGHT:
                x_change += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change += 10
            if event.key == pygame.K_RIGHT:
                x_change += -10
                
    x += x_change
    
    gameDisplay.fill(WHITE)
    car(x, y)
    
    pygame.display.flip() # or pygame.display.update()
    
    clock.tick(60)
    
pygame.quit()
quit()