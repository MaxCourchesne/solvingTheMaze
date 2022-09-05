import pygame
import time
import threading
from itertools import permutations

# ______________________________________________________________________________________________________________________________Fun Variables
diagonalsUnabled = False
priorizeDiagonals = False
drawWeb = True
simultaneousDraw = True
pathNotDrawn = True
drawSlow = True
speedDrawLag = 0
lagLastDraw = 0.05
#lagLastDraw = 0.05




numberHorizontalSquares = 74
# 24
numberVerticalSquares = 48
# 16
screenHeight = 1000
# 998
screenWidth = int(screenHeight * 1.5)
# screenWidth = int(screenHeight*1.5)
limitMoneyBlocks = 8

# ____________________________________________________________________________________________________________________________________________

sizeBorders = 1
# sizeBorders = 3
colorOfSquares = {}
marginUp = 100
marginLeft = 75
marginRight = 75
marginBottom = 50
sizeBorders = 3
mode = "placingStart"
submode = ""
# possible modes: placingStart, placingEnd, placingWalls
# colors
red = (252, 0, 0)
green = (0, 252, 0)
blue = (0, 70, 255)
white = (210, 210, 210)
black = (50, 50, 50)
purple = (200, 0, 200)
yellow = (230, 230, 0)
orange = (255, 165, 0)
brown = (150, 75, 0)
# purple = white
# by default, algorithm is invisible


# correct variables
running = True
challengeDenied = False
beingPressed = False
# size squares
sizeCubes = (screenHeight - marginUp - marginBottom - (
            numberVerticalSquares + 1) * sizeBorders) // numberVerticalSquares
# (screenWidth - marginLeft - marginRight - (numberHorizontalSquares + 1)*sizeBorders)/numberVerticalSquares
wallsPlacedButtonPos = (((screenWidth * 1.5) // 2 - 75), (marginUp // 2 - 25))
ButtonErasingPos = (int(screenWidth * 0.25 - 75), (marginUp // 2 - 25))
StartCube = ""
EndCube = ""
# pathFound = False
listDontCheck = []
listCheckAround = []
listBlocksTeleportation = []
listBlocksTeleportation2 = []
listBlocksTeleportation3 = []
listBlockEnd = []
listMoney = []


listCubesDontDraw = []
DictParent = {}
numLoops = 0

erasing = False
# pygame stuff
screen = pygame.display.set_mode((screenWidth, screenHeight))
# icon
pygame.display.set_caption("200 IQ mouse")

ButtonErasing = pygame.image.load("drawEraseButton.png")
ButtonWallsPlacedImage = pygame.image.load("ButtonWallsPlaced.png")
ButtonWallsPlacedImageAppearing = True

ButtonTp = pygame.image.load("ButtonTeleportation.png")
ButtonTpPressed = pygame.image.load("ButtonTeleportationPressed.png")

ButtonTp2 = pygame.image.load("ButtonTeleportation2.png")
ButtonTpPressed2 = pygame.image.load("ButtonTeleportation2Pressed.png")

ButtonTp3 = pygame.image.load("ButtonTeleportation3.png")
ButtonTpPressed3 = pygame.image.load("ButtonTeleportation3Pressed.png")

#ButtonEnd = pygame.image.load("ButtonEnd.png")
#ButtonEndPressed = pygame.image.load("ButtonEndPressed.png")

ButtonMoney = pygame.image.load("ButtonMoney.png")
ButtonMoneyPressed = pygame.image.load("ButtonMoneyPressed.png")
moneyBlocksButtonClickable = True

noMoneyPlaced = pygame.image.load("noMoneyPlaced.png")
mazeNotPossible = pygame.image.load("mazeNotPossible.png")




ButtonTpPos = ((marginLeft // 2 - 25), (marginUp + 50))
ButtonTp2Pos = ((marginLeft // 2 - 25), (marginUp + 25 + (50 * 2)))
ButtonTp3Pos = ((marginLeft // 2 - 25), (marginUp + (25 * 2) + (50 * 3)))
#ButtonEndPos = ((marginLeft // 2 - 25), (screenHeight - 100))
ButtonMoneyPos = ((marginLeft // 2 - 25), (screenHeight - 100))
#ButtonMoneyPos = ((marginLeft // 2 - 25), (screenHeight - 175))

# screen/display
for VS in range(int(numberVerticalSquares)):
    for HS in range(int(numberHorizontalSquares)):
        colorOfSquares[str(HS), str(VS)] = "white"


def drawchecker():
    for VS in range(int(numberVerticalSquares)):
        for HS in range(int(numberHorizontalSquares)):
            try:
                pygame.draw.rect(screen, eval(colorOfSquares[str(HS), str(VS)]), (
                (marginLeft + HS * (sizeCubes + sizeBorders) + sizeBorders),
                (marginUp + VS * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
            except:
                #print(f"color of square going to be drawn = {colorOfSquares[str(HS), str(VS)]}")
                pygame.draw.rect(screen, colorOfSquares[str(HS), str(VS)], (
                    (marginLeft + HS * (sizeCubes + sizeBorders) + sizeBorders),
                    (marginUp + VS * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))


# modes


# selecting mode
def placeStartEnd(IntMode, Color, EndMode):
    global mode
    global StartCube
    global EndCube
    global ButtonButtonTpAppearing

    if mode == IntMode:
        cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
        cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
        if IntMode != "placingEnd" or (cubeStartX, cubeStartY) != StartCube:
            colorOfSquares[str(cubeStartX), str(cubeStartY)] = Color
            mode = EndMode
        if IntMode == "placingStart": listDontCheck.append((cubeStartX, cubeStartY))

        if IntMode == "placingStart":
            StartCube = (cubeStartX, cubeStartY)

        if IntMode == "placingEnd":
            if (cubeStartX, cubeStartY) != StartCube:
                ButtonButtonTpAppearing = True
                EndCube = (cubeStartX, cubeStartY)


# placeImportantBlocks(placingTp, cubeStartX, cubeStartY, yellow, listBlocksTeleportation)
def placeImportantBlocks(cubeX, cubeY):
    global submode

    # new
    def addToLists(color, listTpOfSameSort):
        colorOfSquares[str(cubeX), str(cubeY)] = color
        if (cubeX, cubeY) not in listDontCheck:
            listDontCheck.append((cubeX, cubeY))
        if (cubeX, cubeY) not in listTpOfSameSort:
            listTpOfSameSort.append((cubeX, cubeY))

    if submode == "placingTp":
        addToLists(yellow, listBlocksTeleportation)
    if submode == "placingTp2":
        addToLists(orange, listBlocksTeleportation2)
    if submode == "placingTp3":
        addToLists(purple, listBlocksTeleportation3)
    if submode == "placingExtraEnd":
        addToLists(red, listBlockEnd)
    if submode == "placingMoney":
        if len(listMoney) < limitMoneyBlocks:
            addToLists(brown, listMoney)
        else:
            submode = ""


def drawOrErase(posX, posY):
    global erasing
    if erasing == False:
        if colorOfSquares[str(posX), str(posY)] == "white":
            colorOfSquares[str(posX), str(posY)] = "black"
            listDontCheck.append((posX, posY))
            pygame.draw.rect(screen, eval(colorOfSquares[str(posX), str(posY)]), (
                (marginLeft + posX * (sizeCubes + sizeBorders) + sizeBorders),
                (marginUp + posY * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
    else:
        if colorOfSquares[str(posX), str(posY)] == "black":
            colorOfSquares[str(posX), str(posY)] = "white"
            listDontCheck.remove((cubeStartX, cubeStartY))
            pygame.draw.rect(screen, eval(colorOfSquares[str(posX), str(posY)]), (
                (marginLeft + posX * (sizeCubes + sizeBorders) + sizeBorders),
                (marginUp + posY * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))


def drawTheButtons():
    global mode
    global submode

    def drawingButtonsForTps(submodeWhenPlacingTp, PosButtonTp, imagePressed, imageNonPressed):
        if submode != submodeWhenPlacingTp:
            screen.blit(imageNonPressed, PosButtonTp)
        if submode == submodeWhenPlacingTp:
            screen.blit(imagePressed, PosButtonTp)

    if mode == "placingWalls":
        screen.blit(ButtonWallsPlacedImage, wallsPlacedButtonPos)
        screen.blit(ButtonErasing, ButtonErasingPos)

        drawingButtonsForTps("placingTp", ButtonTpPos, ButtonTpPressed, ButtonTp)
        drawingButtonsForTps("placingTp2", ButtonTp2Pos, ButtonTpPressed2, ButtonTp2)
        drawingButtonsForTps("placingTp3", ButtonTp3Pos, ButtonTpPressed3, ButtonTp3)
        #drawingButtonsForTps("placingExtraEnd", ButtonEndPos, ButtonEndPressed, ButtonEnd)
        drawingButtonsForTps("placingMoney", ButtonMoneyPos, ButtonMoneyPressed, ButtonMoney)


# _______________________________________________________________________________________________________________________<find shortest path>
def findShortestPath1(intBlock, listOfFinalBlocks, listDontCheck, listBlocksTeleportation, listBlocksTeleportation2, listBlocksTeleportation3, numberHorizontalSquares, numberVerticalSquares, diagonalsUnabled):
    global challengeDenied
    initialBlock = intBlock
    listendOfEndBlocks = list(listOfFinalBlocks)
    listDoNotCheck = list(listDontCheck)
    pathComputed = False
    listCheckAround = [(initialBlock)]
    ListPath = []
    pathFound = False
    haveTeleported = False
    haveTeleported2 = False
    haveTeleported3 = False
    DictBlockParentToBlock = {}
    listOfToReturn = []
    numPathsFound = 0
    endblockJustFound = ""
    listHaveLookedAround = []
    listDoNotCheck.append(initialBlock)
    for mon in listOfFinalBlocks:
        if mon in listDoNotCheck:
            listDoNotCheck.remove(mon)



    def checkAround(PosX, PosY, parent, ListEndBlock):

        nonlocal endblockJustFound
        nonlocal listDoNotCheck


        nonlocal pathFound
        nonlocal numPathsFound
        nonlocal haveTeleported
        nonlocal haveTeleported2
        nonlocal haveTeleported3

        def tryToSpreadToTpPoints(listOfBlocksTeleportation, variableWhenHaveTeleported, numTpList):

            nonlocal endblockJustFound
            nonlocal listDoNotCheck
            nonlocal listCheckAround
            nonlocal haveTeleported
            nonlocal haveTeleported2
            nonlocal haveTeleported3

            if (PosX, PosY) in listOfBlocksTeleportation:
                if not variableWhenHaveTeleported:
                    if (PosX, PosY) in listOfBlocksTeleportation:
                        for blocks in listOfBlocksTeleportation:
                            if blocks != (PosX, PosY):

                                listCheckAround.append(blocks)
                                listDoNotCheck.append(blocks)
                                DictBlockParentToBlock[blocks] = (PosX, PosY)
                        DictBlockParentToBlock[(PosX, PosY)] = parent

                if numTpList == 1:
                    haveTeleported = True
                if numTpList == 2:
                    haveTeleported2 = True
                if numTpList == 3:
                    haveTeleported3 = True

        if 0 <= PosX < numberHorizontalSquares and 0 <= PosY < numberVerticalSquares:
            if (PosX, PosY) not in listDoNotCheck:
                listCheckAround.append((PosX, PosY))
                listDoNotCheck.append((PosX, PosY))
                DictBlockParentToBlock[(PosX, PosY)] = parent

                if (PosX, PosY) in ListEndBlock:

                    endblockJustFound = (PosX, PosY)

                    ListEndBlock.remove(endblockJustFound)
                    numPathsFound += 1
                    pathFound = True

            else:
                tryToSpreadToTpPoints(listBlocksTeleportation, haveTeleported, 1)
                tryToSpreadToTpPoints(listBlocksTeleportation2, haveTeleported2, 2)
                tryToSpreadToTpPoints(listBlocksTeleportation3, haveTeleported3, 3)

    for x in range(0, len(listendOfEndBlocks)):
        endblockJustFound = ""
        pathFound = False
        pathComputed = False
        for block in listCheckAround:
            if block not in listHaveLookedAround:
                if not pathFound:
                    if diagonalsUnabled:
                        if priorizeDiagonals:
                            checkAround(block[0] + 1, block[1] + 1, block, listendOfEndBlocks)
                            checkAround(block[0] - 1, block[1] - 1, block, listendOfEndBlocks)
                            checkAround(block[0] - 1, block[1] + 1, block, listendOfEndBlocks)
                            checkAround(block[0] + 1, block[1] - 1, block, listendOfEndBlocks)

                    checkAround(block[0] + 1, block[1], block, listendOfEndBlocks)
                    checkAround(block[0] - 1, block[1], block, listendOfEndBlocks)
                    checkAround(block[0], block[1] + 1, block, listendOfEndBlocks)
                    checkAround(block[0], block[1] - 1, block, listendOfEndBlocks)
                    if diagonalsUnabled:
                        if not priorizeDiagonals:
                            checkAround(block[0] + 1, block[1] + 1, block, listendOfEndBlocks)
                            checkAround(block[0] - 1, block[1] - 1, block, listendOfEndBlocks)
                            checkAround(block[0] - 1, block[1] + 1, block, listendOfEndBlocks)
                            checkAround(block[0] + 1, block[1] - 1, block, listendOfEndBlocks)

                    listHaveLookedAround.append(block)

                else:

                    Next = endblockJustFound
                    while not pathComputed:
                        try:
                            ListPath.append(DictBlockParentToBlock[Next])
                            Next = DictBlockParentToBlock[Next]
                        except:
                            pathComputed = True

                    try:
                        ListPath.insert(0, endblockJustFound)
                        break
                    except:
                        pass

        listOfToReturn.append(list(reversed(ListPath)))
        ListPath = []
        if listOfToReturn == [[]]:
            print(f"challengeDenied turning true")
            challengeDenied = True
    pygame.event.pump()
    return listOfToReturn

def orderOfPointsToPassBy(endCube, startCube, listMoney, allLinks):
    listWebs = []
    def findPossibilities(endCube, startCube, listMoney):
        listCombinations = []
        combinationOfBlocks = permutations(listMoney, int(len(listMoney)))
        for combination in combinationOfBlocks:
            listCombinations.append(combination)
        return listCombinations
    def findShortestWeb(possibilities):
        webs = []
        for possibility in possibilities:
            pygame.event.pump()
            count = 0
            for connection in allLinks:
                if connection[0] == StartCube and connection[1] == possibility[0]:
                    count += connection[2]


                if connection[0] in possibility and connection[1] in possibility:
                    if (possibility.index(connection[0])+1) == possibility.index(connection[1]):
                        count += connection[2]
                if connection[0] == EndCube and connection[1] == possibility[-1]:
                    count += connection[2]
            webs.append([possibility, count])
        shortest = []
        for web in webs:
            if shortest == []:
                shortest = web
            else:
                if web[-1] < shortest[-1]:
                    shortest = web
        return shortest[0]
    listPossibilities = findPossibilities(EndCube, StartCube, listMoney)
    return findShortestWeb(listPossibilities)


# _______________________________________________________________________________________________________________________<find shortest path/>

def changingModePressedNonPressed(buttonPos, submodeThatWillChange, sizeX, sizeY):
    global submode
    if mouseXforPos > buttonPos[0] and mouseXforPos < (buttonPos[0] + sizeX) and mouseYforPos > buttonPos[
        1] and mouseYforPos < (buttonPos[1] + sizeY):
        if submode != submodeThatWillChange:
            submode = submodeThatWillChange
        else:
            submode = ""



listCubesThatHaveBeenDrawn = []
def drawShortestPath(listToDraw):


    global listCubesThatHaveBeenDrawn
    global listCubesDontDraw
    if drawSlow:
        for cube in listToDraw:
            time.sleep(speedDrawLag)

            if cube not in listCubesDontDraw and cube not in listCubesThatHaveBeenDrawn:
                colorOfSquares[str((cube[0])), str((cube[1]))] = (0, 255, 255)
                listCubesThatHaveBeenDrawn.append(cube)

                pygame.draw.rect(screen, colorOfSquares[str((cube[0])), str((cube[1]))], (
                    (marginLeft + cube[0] * (sizeCubes + sizeBorders) + sizeBorders),
                    (marginUp + cube[1] * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
                pygame.display.update()

            else:
                if cube not in listCubesDontDraw:
                    try:
                        Red = int(colorOfSquares[str((cube[0])), str((cube[1]))][0])
                        Green = int(colorOfSquares[str((cube[0])), str((cube[1]))][1]) - 41
                        Blue = int(colorOfSquares[str((cube[0])), str((cube[1]))][2]) - 41

                        if Red <= 0:
                            Red = 0
                        if Green <= 0:
                            Green = 0
                        if Blue <= 0:
                            Blue = 0
                        colorOfSquares[str((cube[0])), str((cube[1]))] = (Red, Green, Blue)
                        #new
                        pygame.draw.rect(screen, colorOfSquares[str((cube[0])), str((cube[1]))], (
                            (marginLeft + cube[0] * (sizeCubes + sizeBorders) + sizeBorders),
                            (marginUp + cube[1] * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
                        pygame.display.update()
                    except:
                        print("couldn't make a cube color darker")

    else:

        for cube in listToDraw:
            colorOfSquares[str((cube[0])), str((cube[1]))] = "blue"

def drawOnePath(ListOfPaths, indexPathToDraw):
    ListToDraw = []

    for cube in ListOfPaths[indexPathToDraw]:
        if cube not in listBlocksTeleportation and cube not in listBlocksTeleportation2 and cube not in listBlocksTeleportation3 and cube != StartCube and cube != EndCube:
            ListToDraw.append(cube)
    drawShortestPath(ListToDraw)
    ListToDraw = []

def drawAOfListOfPath(OneListOfPath):
    if simultaneousDraw:
        if __name__ == "__main__":
            processes = []
            for x in range(0, len(OneListOfPath)):
                process = threading.Thread(target=drawOnePath, args=[OneListOfPath, x])
                processes.append(process)
                process.start()

    else:
        for x in range(0, len(OneListOfPath)):
            drawOnePath(OneListOfPath, x)

def drawFinalPath(listPath):

    global colorOfSquares
    for path in listPath:
        pygame.event.pump()
        for cube in path:
            if cube not in listMoney and cube not in listBlocksTeleportation and cube not in listBlocksTeleportation2 and cube not in listBlocksTeleportation3 and cube != EndCube and cube != StartCube and cube not in listDontCheck:

                try:
                    if colorOfSquares[cube[0], cube[1]] == blue:
                        colorOfSquares[cube[0], cube[1]] = (0, 0, 150)
                        pygame.draw.rect(screen, (0, 0, 150), (
                            (marginLeft + cube[0] * (sizeCubes + sizeBorders) + sizeBorders),
                            (marginUp + cube[1] * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
                        time.sleep(lagLastDraw)
                        pygame.display.update()
                    else:
                        colorOfSquares[cube[0], cube[1]] = blue
                        pygame.draw.rect(screen, blue, (
                            (marginLeft + cube[0] * (sizeCubes + sizeBorders) + sizeBorders),
                            (marginUp + cube[1] * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
                        time.sleep(lagLastDraw)
                        pygame.display.update()
                except:
                    colorOfSquares[cube[0], cube[1]] = blue
                    pygame.draw.rect(screen, blue, (
                        (marginLeft + cube[0] * (sizeCubes + sizeBorders) + sizeBorders),
                        (marginUp + cube[1] * (sizeCubes + sizeBorders) + sizeBorders), sizeCubes, sizeCubes))
                    time.sleep(lagLastDraw)
                    pygame.display.update()




def appendImportantBlocksTolistCubesDontDraw(StartCube, EndCube, listMoney):
    listCubesDontDraw.append(StartCube)
    listCubesDontDraw.append(EndCube)
    for Block in listMoney:
        listCubesDontDraw.append(Block)

def challengeRefused():
    print("The mouse does not accept the challenge")
    screen.blit(mazeNotPossible, ((screenWidth / 2 - 400), (screenHeight / 2 - 200)))
    pygame.display.update()
    time.sleep(5)

def getLinks(listOflistOfPaths):
    links = []
    for listPaths in listOflistOfPaths:
        for list in listPaths:
            if list:
                links.append((list[0], list[-1], len(list)))
    return links

screen.fill((100, 100, 100))
while running:
    # screen.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # _____________________________________________________________Place End and Start_____________________________________________________________________

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "placingStart" or "placingEnd":
                mouseXforPos = pygame.mouse.get_pos()[0]
                mouseYforPos = pygame.mouse.get_pos()[1]

                if mode == "placingWalls":
                    if mouseXforPos > wallsPlacedButtonPos[0] and mouseXforPos < (
                            wallsPlacedButtonPos[0] + 150) and mouseYforPos > wallsPlacedButtonPos[
                        1] and mouseYforPos < (wallsPlacedButtonPos[1] + 50):
                        mode = "algorithm"

                if mode == "placingWalls":
                    changingModePressedNonPressed(ButtonTpPos, "placingTp", 50, 50)
                    changingModePressedNonPressed(ButtonTp2Pos, "placingTp2", 50, 50)
                    changingModePressedNonPressed(ButtonTp3Pos, "placingTp3", 50, 50)
                    if len(listMoney) < limitMoneyBlocks:
                        changingModePressedNonPressed(ButtonMoneyPos, "placingMoney", 50, 50)

                if mode == "placingWalls":
                    if mouseXforPos > ButtonErasingPos[0] and mouseXforPos < (
                            ButtonErasingPos[0] + 150) and mouseYforPos > ButtonErasingPos[1] and mouseYforPos < (
                            ButtonErasingPos[1] + 50):

                        if submode != "":
                            erasing = False
                        else:
                            if erasing == True:
                                erasing = False
                                print("drawing")
                                # keep
                            else:
                                erasing = True
                                print("erasing")
                                #keep

                        submode = ""

                if mouseXforPos > (marginLeft + sizeBorders) and mouseXforPos < (
                        numberHorizontalSquares * (sizeBorders + sizeCubes) + marginLeft):
                    if mouseYforPos > (marginUp + sizeBorders) and mouseYforPos < (
                            numberVerticalSquares * (sizeBorders + sizeCubes) + marginUp):

                        if mode == "placingWalls":
                            if mouseXforPos > wallsPlacedButtonPos[0] and mouseXforPos < (
                                    wallsPlacedButtonPos[0] + 150) and mouseYforPos > wallsPlacedButtonPos[
                                1] and mouseYforPos < (wallsPlacedButtonPos[1] + 50):
                                mode = "algorithm"

                                break
                            beingPressed = True
                            while beingPressed == True:
                                cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (sizeBorders + sizeCubes)
                                cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (sizeBorders + sizeCubes)
                                try:
                                    if submode == "":
                                        drawOrErase(cubeStartX, cubeStartY)
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
                                        cubeStartX = (mouseXforPos - marginLeft - sizeBorders) // (
                                                    sizeBorders + sizeCubes)
                                        cubeStartY = (mouseYforPos - marginUp - sizeBorders) // (
                                                    sizeBorders + sizeCubes)
                                        try:
                                            if submode == "":
                                                drawOrErase(cubeStartX, cubeStartY)
                                            else:
                                                placeImportantBlocks(cubeStartX, cubeStartY)
                                                beingPressed = False

                                        except:
                                            pass

                                        drawTheButtons()
                                        pygame.display.update()
                        else:

                            placeStartEnd("placingEnd", "red", "placingWalls")
                            placeStartEnd("placingStart", "green", "placingEnd")

    if mode == "algorithm":
        running = False

    drawTheButtons()
    drawchecker()
    pygame.display.update()


listBlockEnd.append(EndCube)

ListOfPathsSE = list(findShortestPath1(StartCube, [EndCube], listDontCheck, listBlocksTeleportation, listBlocksTeleportation2, listBlocksTeleportation3, numberHorizontalSquares, numberVerticalSquares, diagonalsUnabled))
ListOfPaths = list(findShortestPath1(StartCube, listMoney, listDontCheck, listBlocksTeleportation, listBlocksTeleportation2, listBlocksTeleportation3, numberHorizontalSquares, numberVerticalSquares, diagonalsUnabled))
# Usefull because the lenght is accurate
ListOfPaths1 = list(findShortestPath1(EndCube, listMoney, listDontCheck, listBlocksTeleportation, listBlocksTeleportation2, listBlocksTeleportation3, numberHorizontalSquares, numberVerticalSquares, diagonalsUnabled))
listOflistOfPaths = [ListOfPaths, ListOfPaths1]
for moneyBlock in listMoney:
    listOflistOfPaths.append(list(findShortestPath1(moneyBlock, listMoney, listDontCheck, listBlocksTeleportation, listBlocksTeleportation2, listBlocksTeleportation3, numberHorizontalSquares, numberVerticalSquares, diagonalsUnabled)))

allLinks = (getLinks(listOflistOfPaths))


for links in allLinks:
    if links[0] == EndCube:
        pass

appendImportantBlocksTolistCubesDontDraw(StartCube, EndCube, listMoney)

if not challengeDenied and drawWeb:
    for list in listOflistOfPaths:
        drawAOfListOfPath(list)

# _________________________________________________________________________________________________Trying an algorithm
# _________________________________________________________________________________________________Trying an algorithm
# _________________________________________________________________________________________________Trying an algorithm
# _________________________________________________________________________________________________Trying an algorithm



PointsToPassBy = orderOfPointsToPassBy(EndCube, StartCube, listMoney, allLinks)

PointsToPassBy_copy = tuple(PointsToPassBy)
finalListToDraw = []

listPointsPassingByInOrder = [StartCube]
for point in PointsToPassBy_copy:
    listPointsPassingByInOrder.append(point)
listPointsPassingByInOrder.append(EndCube)

finalPath = []

for listOfPaths in listOflistOfPaths:
    finalAdded = False
    for list in listOfPaths:
        try:
            if list[0] == EndCube:
                list = reversed(list)
        except:
            #list is empty
            pass


for x in range(0, len(listPointsPassingByInOrder)):
    lastMoney = ""
    for listOfList in listOflistOfPaths:
        for list in listOfList:
            try:
                if list[0] == listPointsPassingByInOrder[x] and list[-1] == listPointsPassingByInOrder[x+1]:
                    finalPath.append(list)
                    lastMoney = list[-1]
            except:
                pass

for listOfList in listOflistOfPaths:
    for list in listOfList:
        try:
            if list[0] == EndCube and list[-1] == finalPath[-1][-1]:
                revertedList = []
                for coordinates in list:
                    revertedList.insert(0, coordinates)
                finalPath.append(revertedList)
        except IndexError:
            # empty list
            pass

# _________________________________________________________________________________________________Trying an algorithm
# _________________________________________________________________________________________________Trying an algorithm
# _________________________________________________________________________________________________Trying an algorithm
# _________________________________________________________________________________________________Trying an algorithm

drawchecker()
pygame.display.update()

for VS in range(int(numberVerticalSquares)):
    for HS in range(int(numberHorizontalSquares)):
        _cube_ = (HS, VS)
        #print(_cube_)
        #time.sleep(0.01)
        if _cube_ not in listMoney and _cube_ not in listBlocksTeleportation and _cube_ not in listBlocksTeleportation2 and _cube_ not in listBlocksTeleportation3 and _cube_ != EndCube and _cube_ != StartCube and _cube_ not in listDontCheck:
            colorOfSquares[str(HS), str(VS)] = "white"

drawchecker()
pygame.display.update()

try:
    if finalPath[-1][-1] != EndCube:
        challengeDenied = True
    if finalPath[0][0] != StartCube:
        challengeDenied = True
except IndexError:
    pass

if finalPath == [] or challengeDenied:
    if listOflistOfPaths == [[], []] and len(listMoney) == 0:
        finalPath = ListOfPathsSE
        if finalPath != [[]]:
            drawFinalPath(finalPath)
            pathNotDrawn = False
        else:
            challengeRefused()
    elif len(listMoney) == 1:
        drawFinalPath(finalPath)
        pathNotDrawn = False
    else:
        challengeRefused()
else:
    drawFinalPath(finalPath)
    pathNotDrawn = False


running = True




while running:
    if pathNotDrawn:
        screen.fill((100, 100, 100))
        drawchecker()
        pygame.display.update()
    else:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






