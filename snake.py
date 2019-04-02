import time
import pygame
import random

pygame.init()

displayWidth = 800
displayHeight = 600
gameScreen = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("Snake")
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
greenDark = (0, 155, 0)
directionMove = 10
FPS = 15
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def textObject(msg, msgType):
    textSurface = font.render(msg, True, msgType)
    return textSurface, textSurface.get_rect()


def msgOutput(msg, msgType):
    # screenMsg = font.render(msg, True, msgType)
    # gameScreen.blit(screenMsg, [displayWidth / 2, displayHeight / 2])
    textSurf, textRect = textObject(msg, msgType)
    textRect.center = (displayWidth / 2), (displayHeight / 2)
    gameScreen.blit(textSurf, textRect)


def snakeSize(size, snakeList):
    for xy in snakeList:
        pygame.draw.rect(gameScreen, black, (xy[0], xy[1], size, size))


def gameLife():
    gameClose = False
    gameOver = False
    leadXChange = 0
    leadYChange = 0
    leadX = displayWidth / 2
    leadY = displayHeight / 2
    snakeList = []
    snakeLength = 1
    randomFoodX = round(random.randrange(0, displayWidth - directionMove) / 10.0) * 10.0
    randomFoodY = round(random.randrange(0, displayHeight - directionMove) / 10.0) * 10.0
    while not gameClose:
        while gameOver:
            gameScreen.fill(white)
            msgOutput('Game Over, press space to play again or Q to quit', red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLife()

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leadXChange = -directionMove
                    leadYChange = 0
                elif event.key == pygame.K_RIGHT:
                    leadXChange = directionMove
                    leadYChange = 0
                elif event.key == pygame.K_UP:
                    leadYChange = -directionMove
                    leadXChange = 0
                elif event.key == pygame.K_DOWN:
                    leadYChange = directionMove
                    leadXChange = 0

                # elif event.type == pygame.KEYUP:
                #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                #         leadXChange=0

            if leadX >= 800 or leadX < 10 or leadY >= 600 or leadY < 0:
                gameOver = True
        leadX += leadXChange
        leadY += leadYChange
        gameScreen.fill(white)
        # foodThickness = 10
        pygame.draw.rect(gameScreen, red, (randomFoodX, randomFoodY, directionMove, directionMove))
        # pygame.draw.rect(gameScreen, black, (leadX, leadY, 10, 10))
        pygame.display.update()
        # snakeList = []
        snakeHead = []
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snakeSize(directionMove, snakeList)
        pygame.display.update()
        if leadX == randomFoodX and leadY == randomFoodY:
            # print("Eaten")
            randomFoodX = round(random.randrange(0, displayWidth - directionMove) / 10.0) * 10.0
            randomFoodY = round(random.randrange(0, displayHeight - directionMove) / 10.0) * 10.0
            snakeLength += 1


        clock.tick(FPS)

    # msgOutput("You lost :(", red)
    # pygame.display.update()
    # time.sleep(2)
    pygame.quit()

    quit()


gameLife()
