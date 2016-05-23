#!/usr/bin/python3

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
car_width = 73

def car(x, y):
    gameDisplay.blit(carImg, (x, y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',  100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()
    
    
def crash():
    message_display('You crashed')
    

def game_loop():
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    gameExit = False

    x_change = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
        
        # Logic - Adding boundaries
        if x > display_width - car_width or x < 0:
            crash()
        

        pygame.display.flip() # or pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
quit()