import pygame
import time
"""
-------------- Last Update --------------------------------------------------

all blocks are being added in listDontCheck by coordinates on the map (x, y). The green and red blocks coordinates are
stored in the variables: StartBlock and EndBlock.

One problem is that the end and begining can be placed on the same square rn
"""
#_____________________Fun Variables
diagonalsUnabled = True

drawSlow = True
speedDraw = 0.05

showHowFarFromOtherPaths = True
showHowFarFromOtherPathsColor = (135, 206, 250)
#0.03   - only matters if drawSlow is True
numberHorizontalSquares = 96
#24
numberVerticalSquares = 64
#16
screenHeight = 1000
#998
screenWidth = int(screenHeight*1.5)
#screenWidth = int(screenHeight*1.5)
sizeBorders = 1
#sizeBorders = 3

#___________________________________

colorOfSquares = {}
marginUp = 100
marginLeft = 75
marginRight = 75
marginBottom = 50
sizeBorders = 3
mode = "placingStart"
submode = ""
# possible modes: placingStart, placingEnd, placingWalls
#colors
red = (252, 0, 0)
green = (0, 252, 0)
blue = (0, 70, 255)
white = (210, 210, 210)
black = (50, 50, 50)
purple = (200, 0, 200)
yellow = (230, 230, 0)
purple = white
#by default, algorithm is invisible


#correct variables
running = True

beingPressed = False
#size squares
sizeCubes = (screenHeight - marginUp - marginBottom - (numberVerticalSquares + 1)*sizeBorders)//numberVerticalSquares
#(screenWidth - marginLeft - marginRight - (numberHorizontalSquares + 1)*sizeBorders)/numberVerticalSquares
wallsPlacedButtonPos = (((screenWidth*1.5) // 2 - 75), (marginUp // 2 - 25))
ButtonErasingPos = (int(screenWidth*0.25 - 75), (marginUp // 2 - 25))
StartCube = ""
EndCube = ""
#pathFound = False
listDontCheck = []
listCheckAround = []
listBlocksTeleportation = []
DictParent = {}


erasing = False
#pygame stuff
screen = pygame.display.set_mode((screenWidth, screenHeight))
#icon
pygame.display.set_caption("algorithm")
ButtonErasing = pygame.image.load("drawEraseButton.png")
ButtonWallsPlacedImage = pygame.image.load("ButtonWallsPlaced.png")
ButtonWallsPlacedImageAppearing = True
ButtonTp = pygame.image.load("ButtonTeleportation.png")
ButtonTpPressed = pygame.image.load("ButtonTeleportationPressed.png")


ButtonTpPos = ((marginLeft//2 - 25), (marginUp + 50))
#screen/display
for VS in range(int(numberVerticalSquares)):
    for HS in range(int(numberHorizontalSquares)):
        colorOfSquares[str(HS), str(VS)] = "white"

'''
for VS in range(int(numberVerticalSquares)):
    for HS in range(int(numberHorizontalSquares)):
        print(f"the color of square {HS}, {VS} is {colorOfSquares[str(HS), str(VS)]}")
'''
def checkIfDrawTheSearch():
    if showHowFarFromOtherPaths:
        for cube in listDontCheck:
            if colorOfSquares[str((cube[0])), str((cube[1]))] != black and colorOfSquares[str((cube[0])), str((cube[1]))] != "black":
                colorOfSquares[str((cube[0])), str((cube[1]))] = showHowFarFromOtherPathsColor
                colorOfSquares[str((StartCube[0])), str((StartCube[1]))] = "green"
                colorOfSquares[str((EndCube[0])), str((EndCube[1]))] = "red"
                for tp in listBlocksTeleportation:
                    colorOfSquares[str((tp[0])), str((tp[1]))] = "yellow"


            for cube in listBlocksTeleportation:
                colorOfSquares[str((cube[0])), str((cube[1]))] = yellow

def drawchecker():
    for VS in range(int(numberVerticalSquares)):
        for HS in range(int(numberHorizontalSquares)):
            try:
                pygame.draw.rect(screen, eval(colorOfSquares[str(HS), str(VS)]), ((marginLeft + HS * (sizeCubes + sizeBorders) + sizeBorders),(marginUp + VS * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
            except:
                pygame.draw.rect(screen, colorOfSquares[str(HS), str(VS)], (
                (marginLeft + HS * (sizeCubes + sizeBorders) + sizeBorders),
                (marginUp + VS * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))


#modes


#selecting mode
def placeStartEnd(IntMode, Color, EndMode):
    global mode
    global StartCube
    global EndCube
    global ButtonButtonTpAppearing

    if mode == IntMode:
        cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
        cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
        colorOfSquares[str(cubeStartX), str(cubeStartY)] = Color
        mode = EndMode
        if IntMode == "placingStart": listDontCheck.append((cubeStartX, cubeStartY))

        if IntMode == "placingStart":
            StartCube = (cubeStartX, cubeStartY)
        if IntMode == "placingEnd":
            ButtonButtonTpAppearing = True
            EndCube = (cubeStartX, cubeStartY)

#placeImportantBlocks(placingTp, cubeStartX, cubeStartY, yellow, listBlocksTeleportation)
def placeImportantBlocks(cubeX, cubeY):
    global submode
    if submode == "placingTp":
        colorOfSquares[str(cubeX), str(cubeY)] = yellow
        if (cubeX, cubeY) not in listDontCheck:
            listDontCheck.append((cubeX, cubeY))
        if (cubeX, cubeY) not in listBlocksTeleportation:
            listBlocksTeleportation.append((cubeX, cubeY))

#_______________________________________________________________________________________________________________________find shortest path



def findShortestPath1(initialBlock, endOfPathBlock, listDoNotCheck, listBlocksTeleportation):
    #print(f"listDoNotCheck = {listDoNotCheck}")
    #print("first line of the function to find algorihtm")
    pathComputed = False
    listCheckAround.append((StartCube))
    ListPath = []
    pathFound = False
    haveTeleported = False

    def checkAround(PosX, PosY, parent, endBlock):
        #print("first line of the function to check around")

        nonlocal pathFound
        nonlocal haveTeleported





        if PosX >= 0 and PosX < numberHorizontalSquares:
            if PosY >= 0 and PosY < numberVerticalSquares:

                if (PosX, PosY) not in listDoNotCheck:
                    listCheckAround.append((PosX, PosY))
                    listDoNotCheck.append((PosX, PosY))
                    DictParent[(PosX, PosY)] = parent
                    if PosX == endBlock[0] and PosY == endBlock[1]:
                        #print("pathfound is turning True")
                        pathFound = True

                elif haveTeleported == False:
                    if (PosX, PosY) in listBlocksTeleportation:
                        for blocks in listBlocksTeleportation:
                            #print("for blocks in listBlocksTeleportation:")
                            #print(listBlocksTeleportation)

                            #if blocks != (PosX, PosY):
                                #print(f"block is {}")
                            listCheckAround.append(blocks)
                            listDoNotCheck.append(blocks)
                            DictParent[blocks] = (PosX, PosY)
                            #DictParent[blocks] = parent  ?
                            haveTeleported = True
                        DictParent[(PosX, PosY)] = parent



    for block in listCheckAround:

        if not pathFound:
            #print(f"block = {block}")
            checkAround(block[0]+1, block[1], block, endOfPathBlock)
            checkAround(block[0]-1, block[1], block, endOfPathBlock)
            checkAround(block[0], block[1]+1, block, endOfPathBlock)
            checkAround(block[0], block[1]-1, block, endOfPathBlock)
            if diagonalsUnabled:
                checkAround(block[0] + 1, block[1]+1, block, endOfPathBlock)
                checkAround(block[0] - 1, block[1]-1, block, endOfPathBlock)
                checkAround(block[0]-1, block[1] + 1, block, endOfPathBlock)
                checkAround(block[0]+1, block[1] - 1, block, endOfPathBlock)
            #print(f"listCheckAround = {listCheckAround}")

        else:

            Next = endOfPathBlock
            while not pathComputed:


                try:
                    ListPath.append(DictParent[Next])
                    Next = DictParent[Next]
                    #print(Next)

                except:
                    pathComputed = True


            #print(f'reversed(ListPath) = {list(reversed(ListPath))}')
            #print(f"initialBlock = {initialBlock}")
            ListPath.remove(initialBlock)

            #return reversed(ListPath)
            return list(reversed(ListPath))



#draw shortest path

def drawShortestPath(listToDraw):



    if drawSlow:
        checkIfDrawTheSearch()

        for cube in listToDraw:
            colorOfSquares[str((cube[0])), str((cube[1]))] = "blue"
            time.sleep(speedDraw)
            drawchecker()
            pygame.display.update()
    else:
        checkIfDrawTheSearch()

        for cube in listToDraw:
            colorOfSquares[str((cube[0])), str((cube[1]))] = "blue"



#game loop

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

                if mode == "placingWalls":
                    if mouseXforPos > ButtonTpPos[0] and mouseXforPos < (ButtonTpPos[0] + 50) and mouseYforPos > ButtonTpPos[1] and mouseYforPos < (ButtonTpPos[1] + 50):
                        if submode != "placingTp":
                            submode = "placingTp"
                        else:
                            submode = ""

                if mode == "placingWalls":
                    if mouseXforPos > ButtonErasingPos[0] and mouseXforPos < (ButtonErasingPos[0] + 150) and mouseYforPos > ButtonErasingPos[1] and mouseYforPos < (ButtonErasingPos[1] + 50):


                        if submode == "placingTp":
                            erasing = False
                        else:
                            if erasing == True:
                                erasing = False
                                print("drawing")
                            else:
                                erasing = True
                                print("erasing")

                        submode = ""

                if mouseXforPos > (marginLeft + sizeBorders) and mouseXforPos < (numberHorizontalSquares *(sizeBorders + sizeCubes) + marginLeft):
                    if mouseYforPos > (marginUp + sizeBorders) and mouseYforPos < (numberVerticalSquares * (sizeBorders + sizeCubes) + marginUp):

                        if mode == "placingWalls":
                            if mouseXforPos > wallsPlacedButtonPos[0] and mouseXforPos < (wallsPlacedButtonPos[0] + 150) and mouseYforPos > wallsPlacedButtonPos[1] and mouseYforPos < (wallsPlacedButtonPos[1] + 50):
                                mode = "algorithm"

                                break
                            beingPressed = True
                            while beingPressed == True:
                                cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
                                cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
                                try:
                                    if submode == "":
                                        if erasing == False:
                                            if colorOfSquares[str(cubeStartX), str(cubeStartY)] == "white":
                                                colorOfSquares[str(cubeStartX), str(cubeStartY)] = "black"
                                                listDontCheck.append((cubeStartX, cubeStartY))
                                        else:
                                            if colorOfSquares[str(cubeStartX), str(cubeStartY)] == "black":
                                                colorOfSquares[str(cubeStartX), str(cubeStartY)] = "white"
                                                listDontCheck.remove((cubeStartX, cubeStartY))
                                    else:
                                        placeImportantBlocks(cubeStartX, cubeStartY)




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
                                            if submode == "":
                                                if erasing == False:
                                                    if colorOfSquares[str(cubeStartX), str(cubeStartY)] == "white":
                                                        colorOfSquares[str(cubeStartX), str(cubeStartY)] = "black"
                                                        listDontCheck.append((cubeStartX, cubeStartY))
                                                else:
                                                    if colorOfSquares[str(cubeStartX), str(cubeStartY)] == "black":
                                                        colorOfSquares[str(cubeStartX), str(cubeStartY)] = "white"
                                                        listDontCheck.remove((cubeStartX, cubeStartY))
                                            else:
                                                placeImportantBlocks(cubeStartX, cubeStartY)


                                        except:
                                            pass
                                        if mode == "placingWalls":
                                            screen.blit(ButtonWallsPlacedImage, wallsPlacedButtonPos)
                                            if submode != "placingTp":
                                                screen.blit(ButtonTp, ButtonTpPos)
                                            if submode == "placingTp":
                                                screen.blit(ButtonTpPressed, ButtonTpPos)
                                            if ButtonWallsPlacedImageAppearing:
                                                screen.blit(ButtonErasing, ButtonErasingPos)


                                        drawchecker()
                                        pygame.display.update()

                        placeStartEnd("placingEnd", "red", "placingWalls")
                        placeStartEnd("placingStart", "green", "placingEnd")

    if mode == "placingWalls":
        screen.blit(ButtonWallsPlacedImage, wallsPlacedButtonPos)
        if ButtonWallsPlacedImageAppearing:
            screen.blit(ButtonErasing, ButtonErasingPos)
        if submode != "placingTp":
            screen.blit(ButtonTp, ButtonTpPos)
        if submode == "placingTp":
            screen.blit(ButtonTpPressed, ButtonTpPos)
    #screen.blit(ButtonErasing, ButtonErasingPos)

    if mode == "algorithm":
        running = False

    drawchecker()
    pygame.display.update()



#print(f'listDontCheck = {listDontCheck}')
startToEnd = list(findShortestPath1(StartCube, EndCube, listDontCheck, listBlocksTeleportation))
# Usefull because the lenght is accurate

ListToDraw = []
for cube in startToEnd:
    if cube not in listBlocksTeleportation and cube != StartCube and cube != EndCube:
        ListToDraw.append(cube)

#print(f"cubes in path ={startToEnd}")
#print(f"listDontCheck = {listDontCheck}")


drawShortestPath(ListToDraw)

drawchecker()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawchecker()
    pygame.display.update()