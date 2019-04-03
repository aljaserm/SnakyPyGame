import time
import pygame
import random

pygame.init()

displayWidth = 800
displayHeight = 600
gameScreen = pygame.display.set_mode((displayWidth, displayHeight))

pygame.display.set_caption("Snake")
# This to add icon to the game
# icon=pygame.image.load()
# pygame.display.set_icon(icon)
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
smallFont = pygame.font.SysFont("Comicsansms", 25)
MedFont = pygame.font.SysFont("Comicsansms", 50)
largeFont = pygame.font.SysFont("Comicsansms", 75)


def userScore(score):
    text=smallFont.render("Score: "+str(score),True,blue)
    gameScreen.blit(text,[0,0])

def gameIntro():
    intro = True
    while intro:
        gameScreen.fill(white)
        msgOutput("Welcome", blue, -100, "large")

        msgOutput("The objective of the game is to eat red apples",
                  black,
                  -30)

        msgOutput("The more apples you eat, the longer you get",
                  black,
                  10)

        msgOutput("If you run into yourself, or the edges, you die!",
                  black,
                  50)

        msgOutput("Press C to play or Q to quit.",
                  black,
                  180)

        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro=False
                    gameLife()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def textObject(msg, msgType, size):
    if size == "small":
        textSurface = smallFont.render(msg, True, msgType)
    elif size == "med":
        textSurface = MedFont.render(msg, True, msgType)
    elif size == "large":
        textSurface = largeFont.render(msg, True, msgType)

    # textSurface = font.render(msg, True, msgType)
    return textSurface, textSurface.get_rect()


def msgOutput(msg, msgType, yDisplay=0, size="small"):
    # screenMsg = font.render(msg, True, msgType)
    # gameScreen.blit(screenMsg, [displayWidth / 2, displayHeight / 2])
    textSurf, textRect = textObject(msg, msgType, size)

    textRect.center = (displayWidth / 2), (displayHeight / 2) + yDisplay
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
            msgOutput('Game Over', red, -50, size="large")
            msgOutput('Press space to Play or Q to Quit', black, 50, size="med")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameClose = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameClose = True

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

            if leadX >= displayWidth or leadX < 0 or leadY >= displayHeight or leadY < 0:
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
        userScore(snakeLength-1)
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


gameIntro()
gameLife()
