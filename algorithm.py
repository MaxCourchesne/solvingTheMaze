import pygame
import time

#setting variables
screenHeight = 998
colorOfSquares = {}
marginUp = 100
marginLeft = 75
marginRight = 75
marginBottom = 50
sizeBorders = 3
mode = "placingStart"
# possible modes: placingStart, placingEnd, placingWalls
#colors
red = (252, 0, 0)
green = (0, 252, 0)
blue = (0, 0, 252)
white = (210, 210, 210)
black = (50, 50, 50)

#correct variables
running = True
screenWidth = int(screenHeight*1.5)
numberHorizontalSquares = 24
#24
numberVerticalSquares = 16
#16
print(screenWidth)
print(numberHorizontalSquares)
beingPressed = False
#size squares
sizeCubes = (screenHeight - marginUp - marginBottom - (numberVerticalSquares + 1)*sizeBorders)//numberVerticalSquares
#(screenWidth - marginLeft - marginRight - (numberHorizontalSquares + 1)*sizeBorders)/numberVerticalSquares
wallsPlacedButtonPos = (((screenWidth*1.5) // 2 - 75), (marginUp // 2 - 25))


#pygame stuff
screen = pygame.display.set_mode((screenWidth, screenHeight))
#icon
pygame.display.set_caption("algorithm")

ButtonWallsPlacedImage = pygame.image.load("ButtonWallsPlaced.png")


#screen/display
for VS in range(int(numberVerticalSquares)):
    for HS in range(int(numberHorizontalSquares)):
        colorOfSquares[str(HS), str(VS)] = "white"

'''
for VS in range(int(numberVerticalSquares)):
    for HS in range(int(numberHorizontalSquares)):
        print(f"the color of square {HS}, {VS} is {colorOfSquares[str(HS), str(VS)]}")
'''
def drawchecker():
    for VS in range(int(numberVerticalSquares)):
        for HS in range(int(numberHorizontalSquares)):
            pygame.draw.rect(screen, eval(colorOfSquares[str(HS), str(VS)]), (
            (marginLeft + HS * (sizeCubes + sizeBorders) + sizeBorders),
            (marginUp + VS * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))

#modes


#selecting mode
def placeStartEnd(IntMode, Color, EndMode):
    global mode
    if mode == IntMode:
        cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
        print(f"cubeStartX = {cubeStartX}")
        cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
        colorOfSquares[str(cubeStartX), str(cubeStartY)] = Color
        mode = EndMode



#changing value of a certain square


#find shortest path
def findShortestPath1(greenBlock, redBlock):
    pass



#draw shortest path



#game loop
print(colorOfSquares)
while running:
    screen.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


            #_____________________________________________________________Place End and Start_____________________________________________________________________

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "placingStart" or "placingEnd":
                mouseXforPos = pygame.mouse.get_pos()[0]
                mouseYforPos = pygame.mouse.get_pos()[1]

                if mode == "placingWalls":
                    if mouseXforPos > wallsPlacedButtonPos[0] and mouseXforPos < (wallsPlacedButtonPos[0] + 150) and mouseYforPos > wallsPlacedButtonPos[1] and mouseYforPos < (wallsPlacedButtonPos[1] + 50):
                        mode = "algorithm"
                        print("supposed to have switched on algorithm mode")


                if mouseXforPos > (marginLeft + sizeBorders) and mouseXforPos < (numberHorizontalSquares *(sizeBorders + sizeCubes) + marginLeft):
                    if mouseYforPos > (marginUp + sizeBorders) and mouseYforPos < (numberVerticalSquares * (sizeBorders + sizeCubes) + marginUp):

                        if mode == "placingWalls":
                            if mouseXforPos > wallsPlacedButtonPos[0] and mouseXforPos < (wallsPlacedButtonPos[0] + 150) and mouseYforPos > wallsPlacedButtonPos[1] and mouseYforPos < (wallsPlacedButtonPos[1] + 50):
                                mode = "algorithm"
                                print("supposed to have switched on algorithm mode")
                                break
                            beingPressed = True
                            while beingPressed == True:
                                cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
                                cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
                                try:
                                    if colorOfSquares[str(cubeStartX), str(cubeStartY)] == "white":
                                        colorOfSquares[str(cubeStartX), str(cubeStartY)] = "black"
                                except:
                                    pass
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        beingPressed = False
                                    if beingPressed:
                                        mouseXforPos = pygame.mouse.get_pos()[0]
                                        mouseYforPos = pygame.mouse.get_pos()[1]
                                        cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
                                        cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
                                        try:
                                            if colorOfSquares[str(cubeStartX), str(cubeStartY)] == "white":
                                                colorOfSquares[str(cubeStartX), str(cubeStartY)] = "black"
                                        except:
                                            pass
                                        if mode == "placingWalls":
                                            screen.blit(ButtonWallsPlacedImage, wallsPlacedButtonPos)

                                        drawchecker()
                                        pygame.display.update()

                        placeStartEnd("placingEnd", "red", "placingWalls")
                        placeStartEnd("placingStart", "green", "placingEnd")

    if mode == "placingWalls":
        screen.blit(ButtonWallsPlacedImage, wallsPlacedButtonPos)

    drawchecker()
    pygame.display.update()






