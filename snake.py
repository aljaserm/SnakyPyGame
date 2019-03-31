import pygame
import pygame

pygame.init()

gameScreen = pygame.display.set_mode((800, 600))

gameClose = False
pygame.display.set_caption("Snake")
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
leadX = 300
leadY = 300
leadXChange = 0
leadYChange = 0
while not gameClose:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameClose = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leadXChange -= 10
            if event.key == pygame.K_RIGHT:
                leadXChange += 10
            if event.key == pygame.K_UP:
                leadYChange -= 10
            if event.key == pygame.K_DOWN:
                leadYChange += 10
        leadX += leadXChange
        leadY += leadYChange

    gameScreen.fill(white)
    pygame.draw.rect(gameScreen, black, (leadX, leadY, 10, 10))

    pygame.display.update()

pygame.quit()

quit()
