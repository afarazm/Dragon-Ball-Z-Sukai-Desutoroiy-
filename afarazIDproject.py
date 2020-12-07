# Arham Faraz
# afaraz@andrew.cmu.edu

import pygame
import random
import sys

pygame.init()

# All music and sounds from the original Dragon Ball Z show.
# Main Menu Function
def mainMenu():
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()
    textXloc = 160
    whiteColor = (255, 255, 255)
    picXloc = 80

    # Image Loading
    backGround = pygame.image.load("Pics/BGDB.PNG").convert()
    logoDBZ = pygame.image.load("Pics/logo.png")
    gokuO = pygame.image.load("Pics/gokuO.png")
    ss2Image = pygame.image.load("Pics/SS2PROF.gif")
    vegetaImage = pygame.image.load("Pics/VPROF.gif")
    brolyImage = pygame.image.load("Pics/BPROF.gif")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    logoWidth = 350
    logoHeight = 200
    characterWidth = 60
    characterHeight = 60

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Logo Function
    def logo():
        gameScreen.blit(pygame.transform.scale(logoDBZ, (logoWidth, logoHeight)), (100, 50))

    def gokuLoad():
        gameScreen.blit(pygame.transform.scale(gokuO, (characterWidth, characterHeight)), (picXloc, 310))

    def ss2Load():
        gameScreen.blit(pygame.transform.scale(ss2Image, (characterWidth, characterHeight)), (picXloc, 380))

    def vegetaLoad():
        gameScreen.blit(pygame.transform.scale(vegetaImage, (characterWidth, characterHeight)), (picXloc, 450))

    def brolyLoad():
        gameScreen.blit(pygame.transform.scale(brolyImage, (characterWidth, characterHeight)), (picXloc, 520))

    # Text Function
    def gokuSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 1 to pick Classic Goku", True, whiteColor)
        gameScreen.blit(text, (textXloc, 320))

    # Text Function
    def ss2Select():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 2 to pick Goku SSJ", True, whiteColor)
        gameScreen.blit(text, (textXloc, 390))

    # Text Function
    def vegetaSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 3 to pick Vegeta SSJ", True, whiteColor)
        gameScreen.blit(text, (textXloc, 460))

    # Text Function
    def brolySelect():
        font = pygame.font.SysFont("Agency FB", 35)
        scoreText = font.render("Press 4 to pick Broly", True, whiteColor)
        gameScreen.blit(scoreText, (textXloc, 530))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/Menu.ogg")
    bgMusic.play()


    # This helps close the window once the player is done playing
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bgMusic.stop()
                    mapMenu()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    bgMusic.stop()
                    mapMenu1()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    bgMusic.stop()
                    mapMenu2()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    bgMusic.stop()
                    mapMenu3()
                    sys.exit()

        # This is where I call my functions
        BG()
        logo()
        gokuSelect()
        ss2Select()
        vegetaSelect()
        brolySelect()
        ss2Load()
        vegetaLoad()
        brolyLoad()
        gokuLoad()

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def mapMenu():
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()
    textXloc = 100
    whiteColor = (255, 255, 255)
    picXloc = 30

    # Image Loading
    backGround = pygame.image.load("Pics/map.PNG").convert()
    gokuBG = pygame.image.load("Pics/BGDBZ.PNG")
    ss2BG = pygame.image.load("Pics/SS2back.png")
    vegetaBG = pygame.image.load("Pics/vegetaback.png")
    brolyBG = pygame.image.load("Pics/brolyback.png")

    # Image Scaling
    bgWidth = 550
    bgHeight = 500
    characterWidth = 60
    characterHeight = 60

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Logo Function
    def gokubgLoad():
        gameScreen.blit(pygame.transform.scale(gokuBG, (characterWidth, characterHeight)), (picXloc, 310))

    def ss2bgLoad():
        gameScreen.blit(pygame.transform.scale(ss2BG, (characterWidth, characterHeight)), (picXloc, 380))

    def vegetabgLoad():
        gameScreen.blit(pygame.transform.scale(vegetaBG, (characterWidth, characterHeight)), (picXloc, 450))

    def brolybgLoad():
        gameScreen.blit(pygame.transform.scale(brolyBG, (characterWidth, characterHeight)), (picXloc, 520))

    # Text Function
    def mapSelect():
        font = pygame.font.SysFont("Agency FB", 50, "Bold")
        text = font.render("Map Selection", True, whiteColor)
        gameScreen.blit(text, (130, 100))

    def gokubgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 1 to pick Gizard Wasteland", True, whiteColor)
        gameScreen.blit(text, (textXloc, 320))

    # Text Function
    def ss2bgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 2 to pick Supreme Kai's Planet", True, whiteColor)
        gameScreen.blit(text, (textXloc, 390))

    # Text Function
    def vegetabgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 3 to pick Namek", True, whiteColor)
        gameScreen.blit(text, (textXloc, 460))

    # Text Function
    def brolybgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        scoreText = font.render("Press 4 to pick Destroyed Central City", True, whiteColor)
        gameScreen.blit(scoreText, (textXloc, 530))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/place.ogg")
    bgMusic.play()

    # This helps close the window once the player is done playing
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bgMusic.stop()
                    game()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    bgMusic.stop()
                    gameMap1()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    bgMusic.stop()
                    gameMap2()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    bgMusic.stop()
                    gameMap3()
                    sys.exit()

        # This is where I call my functions
        BG()
        gokubgSelect()
        ss2bgSelect()
        vegetabgSelect()
        brolybgSelect()
        ss2bgLoad()
        vegetabgLoad()
        brolybgLoad()
        gokubgLoad()
        mapSelect()

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def mapMenu1():
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()
    textXloc = 100
    whiteColor = (255, 255, 255)
    picXloc = 30

    # Image Loading
    backGround = pygame.image.load("Pics/map.PNG").convert()
    gokuBG = pygame.image.load("Pics/BGDBZ.PNG")
    ss2BG = pygame.image.load("Pics/SS2back.png")
    vegetaBG = pygame.image.load("Pics/vegetaback.png")
    brolyBG = pygame.image.load("Pics/brolyback.png")

    # Image Scaling
    bgWidth = 550
    bgHeight = 500
    characterWidth = 60
    characterHeight = 60

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Logo Function
    def gokubgLoad():
        gameScreen.blit(pygame.transform.scale(gokuBG, (characterWidth, characterHeight)), (picXloc, 310))

    def ss2bgLoad():
        gameScreen.blit(pygame.transform.scale(ss2BG, (characterWidth, characterHeight)), (picXloc, 380))

    def vegetabgLoad():
        gameScreen.blit(pygame.transform.scale(vegetaBG, (characterWidth, characterHeight)), (picXloc, 450))

    def brolybgLoad():
        gameScreen.blit(pygame.transform.scale(brolyBG, (characterWidth, characterHeight)), (picXloc, 520))

    # Text Function
    def mapSelect():
        font = pygame.font.SysFont("Agency FB", 50, "Bold")
        text = font.render("Map Selection", True, whiteColor)
        gameScreen.blit(text, (130, 100))

    def gokubgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 1 to pick Gizard Wasteland", True, whiteColor)
        gameScreen.blit(text, (textXloc, 320))

    # Text Function
    def ss2bgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 2 to pick Supreme Kai's Planet", True, whiteColor)
        gameScreen.blit(text, (textXloc, 390))

    # Text Function
    def vegetabgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 3 to pick Namek", True, whiteColor)
        gameScreen.blit(text, (textXloc, 460))

    # Text Function
    def brolybgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        scoreText = font.render("Press 4 to pick Destroyed Central City", True, whiteColor)
        gameScreen.blit(scoreText, (textXloc, 530))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/place.ogg")
    bgMusic.play()

    # This helps close the window once the player is done playing
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bgMusic.stop()
                    gameSS2map2()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    bgMusic.stop()
                    gameSS2()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    bgMusic.stop()
                    gameSS2map1()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    bgMusic.stop()
                    gameSS2map3()
                    sys.exit()

        # This is where I call my functions
        BG()
        gokubgSelect()
        ss2bgSelect()
        vegetabgSelect()
        brolybgSelect()
        ss2bgLoad()
        vegetabgLoad()
        brolybgLoad()
        gokubgLoad()
        mapSelect()

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def mapMenu2():
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()
    textXloc = 100
    whiteColor = (255, 255, 255)
    picXloc = 30

    # Image Loading
    backGround = pygame.image.load("Pics/map.PNG").convert()
    gokuBG = pygame.image.load("Pics/BGDBZ.PNG")
    ss2BG = pygame.image.load("Pics/SS2back.png")
    vegetaBG = pygame.image.load("Pics/vegetaback.png")
    brolyBG = pygame.image.load("Pics/brolyback.png")

    # Image Scaling
    bgWidth = 550
    bgHeight = 500
    characterWidth = 60
    characterHeight = 60

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Logo Function
    def gokubgLoad():
        gameScreen.blit(pygame.transform.scale(gokuBG, (characterWidth, characterHeight)), (picXloc, 310))

    def ss2bgLoad():
        gameScreen.blit(pygame.transform.scale(ss2BG, (characterWidth, characterHeight)), (picXloc, 380))

    def vegetabgLoad():
        gameScreen.blit(pygame.transform.scale(vegetaBG, (characterWidth, characterHeight)), (picXloc, 450))

    def brolybgLoad():
        gameScreen.blit(pygame.transform.scale(brolyBG, (characterWidth, characterHeight)), (picXloc, 520))

    # Text Function
    def mapSelect():
        font = pygame.font.SysFont("Agency FB", 50, "Bold")
        text = font.render("Map Selection", True, whiteColor)
        gameScreen.blit(text, (130, 100))

    def gokubgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 1 to pick Gizard Wasteland", True, whiteColor)
        gameScreen.blit(text, (textXloc, 320))

    # Text Function
    def ss2bgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 2 to pick Supreme Kai's Planet", True, whiteColor)
        gameScreen.blit(text, (textXloc, 390))

    # Text Function
    def vegetabgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 3 to pick Namek", True, whiteColor)
        gameScreen.blit(text, (textXloc, 460))

    # Text Function
    def brolybgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        scoreText = font.render("Press 4 to pick Destroyed Central City", True, whiteColor)
        gameScreen.blit(scoreText, (textXloc, 530))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/place.ogg")
    bgMusic.play()

    # This helps close the window once the player is done playing
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bgMusic.stop()
                    gameVegetamap1()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    bgMusic.stop()
                    gameVegetamap2()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    bgMusic.stop()
                    gameVegeta()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    bgMusic.stop()
                    gameVegetamap3()
                    sys.exit()

        # This is where I call my functions
        BG()
        gokubgSelect()
        ss2bgSelect()
        vegetabgSelect()
        brolybgSelect()
        ss2bgLoad()
        vegetabgLoad()
        brolybgLoad()
        gokubgLoad()
        mapSelect()

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def mapMenu3():
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()
    textXloc = 100
    whiteColor = (255, 255, 255)
    picXloc = 30

    # Image Loading
    backGround = pygame.image.load("Pics/map.PNG").convert()
    gokuBG = pygame.image.load("Pics/BGDBZ.PNG")
    ss2BG = pygame.image.load("Pics/SS2back.png")
    vegetaBG = pygame.image.load("Pics/vegetaback.png")
    brolyBG = pygame.image.load("Pics/brolyback.png")

    # Image Scaling
    bgWidth = 550
    bgHeight = 500
    characterWidth = 60
    characterHeight = 60

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Logo Function
    def gokubgLoad():
        gameScreen.blit(pygame.transform.scale(gokuBG, (characterWidth, characterHeight)), (picXloc, 310))

    def ss2bgLoad():
        gameScreen.blit(pygame.transform.scale(ss2BG, (characterWidth, characterHeight)), (picXloc, 380))

    def vegetabgLoad():
        gameScreen.blit(pygame.transform.scale(vegetaBG, (characterWidth, characterHeight)), (picXloc, 450))

    def brolybgLoad():
        gameScreen.blit(pygame.transform.scale(brolyBG, (characterWidth, characterHeight)), (picXloc, 520))

    # Text Function
    def mapSelect():
        font = pygame.font.SysFont("Agency FB", 50, "Bold")
        text = font.render("Map Selection", True, whiteColor)
        gameScreen.blit(text, (130, 100))

    def gokubgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 1 to pick Gizard Wasteland", True, whiteColor)
        gameScreen.blit(text, (textXloc, 320))

    # Text Function
    def ss2bgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 2 to pick Supreme Kai's Planet", True, whiteColor)
        gameScreen.blit(text, (textXloc, 390))

    # Text Function
    def vegetabgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        text = font.render("Press 3 to pick Namek", True, whiteColor)
        gameScreen.blit(text, (textXloc, 460))

    # Text Function
    def brolybgSelect():
        font = pygame.font.SysFont("Agency FB", 35)
        scoreText = font.render("Press 4 to pick Destroyed Central City", True, whiteColor)
        gameScreen.blit(scoreText, (textXloc, 530))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/place.ogg")
    bgMusic.play()

    # This helps close the window once the player is done playing
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bgMusic.stop()
                    gameBrolymap1()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    bgMusic.stop()
                    gameBrolymap2()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    bgMusic.stop()
                    gameBrolymap3()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    bgMusic.stop()
                    gameBroly()
                    sys.exit()

        # This is where I call my functions
        BG()
        gokubgSelect()
        ss2bgSelect()
        vegetabgSelect()
        brolybgSelect()
        ss2bgLoad()
        vegetabgLoad()
        brolybgLoad()
        gokubgLoad()
        mapSelect()

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()


# Main game Function
def game():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("DragonBall Z: Goku's Journey")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/BGDBZ.png").convert()
    gokuImage = pygame.image.load("Pics/Goku.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    yellowColor = (255, 223, 0)
    fontSize = 35

    # Goku Jump Variables
    gokuYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    #def dragonChar(z, b):
        #gameScreen.blit(pygame.transform.scale(dragonBall, (dragonballWidth, dragonBallHeight)), (z, b))

    # Goku Movement
    def gokuChar(y):
        gameScreen.blit(gokuImage, (120, y))

    # Score Counter
    score = 0

    def pyScore(score):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Goku Power Level: " + str(score), True, yellowColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BGMusic.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    gokuUp = pygame.mixer.Sound("sounds/gokuUP.ogg")
    gokuDown = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(score)
        #dragonChar(z, b)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        gokuYpos = gokuYpos + jumpY
        gokuChar(gokuYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, gokuYpos):
            if x <= 180 <= x + 120:
                if gokuYpos <= y + 245 or gokuYpos >= y + 370:
                    gokuUp.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            score = score + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if gokuYpos < 10:
            gokuYpos = 10
            gokuUp.play()
        if gokuYpos > 505:
            gokuYpos = 505
            gokuDown.play()

        collision(x, y, gokuYpos)

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()


# Main game Function
def gameSS2():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/SS2back.png").convert()
    ss2Image = pygame.image.load("Pics/SS2.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    greenColor = (50, 205, 50)
    fontSize = 35

    # SS2 Jump Variables
    ss2Ypos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # SS2 Movement
    def ss2Char(y):
        gameScreen.blit(pygame.transform.scale(ss2Image, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("SSJ Power Level: " + str(counter), True, greenColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/SS2Mus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    ss2Up = pygame.mixer.Sound("sounds/gokuUP.ogg")
    ss2Down = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        ss2Ypos = ss2Ypos + jumpY
        ss2Char(ss2Ypos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, ss2Ypos):
            if x <= 190 <= x + 120:
                if ss2Ypos <= y + 245 or ss2Ypos >= y + 370:
                    ss2Up.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if ss2Ypos < 10:
            ss2Ypos = 10
            ss2Up.play()
        if ss2Ypos > 505:
            ss2Ypos = 505
            ss2Down.play()

        collision(x, y, ss2Ypos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()


# Main game Function
def gameVegeta():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/vegetaback.png").convert()
    vegetaImage = pygame.image.load("Pics/Vegeta.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 70
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    blueColor = (0, 0, 205)
    fontSize = 35

    # Veg Jump Variables
    vegetaYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Veg Movement
    def vegetaChar(y):
        gameScreen.blit(pygame.transform.scale(vegetaImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Vegeta Power Level: " + str(counter), True, blueColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/VegetaMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    vegetaUp = pygame.mixer.Sound("sounds/vegataUP.ogg")
    vegetaDown = pygame.mixer.Sound("sounds/vegetaDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        vegetaYpos = vegetaYpos + jumpY
        vegetaChar(vegetaYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, vegetaYpos):
            if x <= 170 <= x + 120:
                if vegetaYpos <= y + 245 or vegetaYpos >= y + 370:
                    vegetaDown.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if vegetaYpos < 10:
            vegetaYpos = 10
            vegetaUp.play()
        if vegetaYpos > 505:
            vegetaYpos = 505
            vegetaDown.play()

        collision(x, y, vegetaYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()


# Main game Function
def gameBroly():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/brolyback.png").convert()
    brolyImage = pygame.image.load("Pics/Broly.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 100

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    whiteColor = (255, 255, 255)
    fontSize = 35

    # Broly Jump Variables
    brolyYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Broly Movement
    def brolyChar(y):
        gameScreen.blit(pygame.transform.scale(brolyImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Broly Power Level: " + str(counter), True, whiteColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BrolyMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    brolyUp = pygame.mixer.Sound("sounds/brolyUP.ogg")
    brolyDown = pygame.mixer.Sound("sounds/brolyDown.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        brolyYpos = brolyYpos + jumpY
        brolyChar(brolyYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, brolyYpos):
            if x <= 190 <= x + 120:
                if brolyYpos <= y + 245 or brolyYpos >= y + 370:
                    brolyUp.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if brolyYpos < 10:
            brolyYpos = 10
            brolyUp.play()
        if brolyYpos > 505:
            brolyYpos = 505
            brolyDown.play()

        collision(x, y, brolyYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

# End Menu Function
def endMenu():
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/endmenu1.jpg").convert()
    logoDBZ = pygame.image.load("Pics/logo.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    logoWidth = 150
    logoHeight = 100
    logoX = 0
    logoY = 450

    # Variable Vals
    fontSize = 40
    whiteColor = (255, 255, 255)

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Logo Function
    def logo():
        gameScreen.blit(pygame.transform.scale(logoDBZ, (logoWidth, logoHeight)), (logoX, logoY))

    # Text Function
    def restart():
        font = pygame.font.SysFont("Agency FB", fontSize)
        text = font.render("Press 1 to go back to the Main Menu", True, whiteColor)
        gameScreen.blit(text, (0, 30))

    # Text Function
    def endMain():
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Press 2 to close game", True, whiteColor)
        gameScreen.blit(scoreText, (0, 100))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/endMus.ogg")
    bgMusic.play()

    # This helps close the window once the player is done playing
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    bgMusic.stop()
                    sys.exit()

        # This is where I call my functions
        BG()
        logo()
        restart()
        endMain()

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameMap1():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("DragonBall Z: Goku's Journey")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/SS2back.png").convert()
    gokuImage = pygame.image.load("Pics/Goku.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")
    #dragonBall = pygame.image.load("Pics/blastoid.gif")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    dragonballWidth = 30
    #dragonBallHeight = 30

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    z = disWidth + dragonballWidth
    b = 0
    greenColor = (50, 205, 50)
    fontSize = 35

    # Goku Jump Variables
    gokuYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    #def dragonChar(z, b):
        #gameScreen.blit(pygame.transform.scale(dragonBall, (dragonballWidth, dragonBallHeight)), (z, b))

    # Goku Movement
    def gokuChar(y):
        gameScreen.blit(gokuImage, (120, y))

    # Score Counter
    score = 0

    def pyScore(score):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Goku Power Level: " + str(score), True, greenColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/SS2Mus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    gokuUp = pygame.mixer.Sound("sounds/gokuUP.ogg")
    gokuDown = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(score)
        #dragonChar(z, b)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        gokuYpos = gokuYpos + jumpY
        gokuChar(gokuYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7
        z = z - 11

        def collision(x, y, gokuYpos):
            if x <= 180 <= x + 120:
                if gokuYpos <= y + 245 or gokuYpos >= y + 370:
                    gokuUp.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        #def collisionb(z, b, gokuYpos):
            #if z <= 180 <= z + 10:
                #if gokuYpos <= b - 50 or gokuYpos >= b + 50:
                    #gokuUp.play()
                    #bgMusic.stop()
                    #endMenu()
                    #sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            score = score + 1

        #if z < -dragonballWidth:
            #z = dragonballWidth + disWidth
            #b = random.randint(50, 550)

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if gokuYpos < 10:
            gokuYpos = 10
            gokuUp.play()
        if gokuYpos > 505:
            gokuYpos = 505
            gokuDown.play()

        collision(x, y, gokuYpos)
        #collisionb(z, b, gokuYpos)

        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameMap2():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/vegetaback.png").convert()
    gokuImage = pygame.image.load("Pics/Goku.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    blueColor = (0, 0, 205)
    fontSize = 35

    # SS2 Jump Variables
    gokuYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # SS2 Movement
    def gokuChar(y):
        gameScreen.blit(gokuImage, (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("SSJ Power Level: " + str(counter), True, blueColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/VegetaMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    ss2Up = pygame.mixer.Sound("sounds/gokuUP.ogg")
    ss2Down = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        gokuYpos = gokuYpos + jumpY
        gokuChar(gokuYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, gokuYpos):
            if x <= 190 <= x + 120:
                if gokuYpos <= y + 245 or gokuYpos >= y + 370:
                    ss2Up.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if gokuYpos < 10:
            gokuYpos = 10
            ss2Up.play()
        if gokuYpos > 505:
            gokuYpos = 505
            ss2Down.play()

        collision(x, y, gokuYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameMap3():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/brolyback.png").convert()
    gokuImage = pygame.image.load("Pics/Goku.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    whiteColor = (255, 255, 255)
    fontSize = 35

    # SS2 Jump Variables
    gokuYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Goku Movement
    def gokuChar(y):
        gameScreen.blit(gokuImage, (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("SSJ Power Level: " + str(counter), True, whiteColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BrolyMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    ss2Up = pygame.mixer.Sound("sounds/gokuUP.ogg")
    ss2Down = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        gokuYpos = gokuYpos + jumpY
        gokuChar(gokuYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, gokuYpos):
            if x <= 190 <= x + 120:
                if gokuYpos <= y + 245 or gokuYpos >= y + 370:
                    ss2Up.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if gokuYpos < 10:
            gokuYpos = 10
            ss2Up.play()
        if gokuYpos > 505:
            gokuYpos = 505
            ss2Down.play()

        collision(x, y, gokuYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameSS2map1():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/vegetaback.png").convert()
    ss2Image = pygame.image.load("Pics/SS2.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    blueColor = (0, 0, 205)
    fontSize = 35

    # SS2 Jump Variables
    ss2Ypos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # SS2 Movement
    def ss2Char(y):
        gameScreen.blit(pygame.transform.scale(ss2Image, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("SSJ Power Level: " + str(counter), True, blueColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/VegetaMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    ss2Up = pygame.mixer.Sound("sounds/gokuUP.ogg")
    ss2Down = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        ss2Ypos = ss2Ypos + jumpY
        ss2Char(ss2Ypos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, ss2Ypos):
            if x <= 190 <= x + 120:
                if ss2Ypos <= y + 245 or ss2Ypos >= y + 370:
                    ss2Up.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if ss2Ypos < 10:
            ss2Ypos = 10
            ss2Up.play()
        if ss2Ypos > 505:
            ss2Ypos = 505
            ss2Down.play()

        collision(x, y, ss2Ypos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameSS2map2():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/BGDBZ.PNG").convert()
    ss2Image = pygame.image.load("Pics/SS2.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    yellowColor = (255, 223, 0)
    fontSize = 35

    # SS2 Jump Variables
    ss2Ypos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # SS2 Movement
    def ss2Char(y):
        gameScreen.blit(pygame.transform.scale(ss2Image, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("SSJ Power Level: " + str(counter), True, yellowColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BGMusic.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    ss2Up = pygame.mixer.Sound("sounds/gokuUP.ogg")
    ss2Down = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        ss2Ypos = ss2Ypos + jumpY
        ss2Char(ss2Ypos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, ss2Ypos):
            if x <= 190 <= x + 120:
                if ss2Ypos <= y + 245 or ss2Ypos >= y + 370:
                    ss2Up.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if ss2Ypos < 10:
            ss2Ypos = 10
            ss2Up.play()
        if ss2Ypos > 505:
            ss2Ypos = 505
            ss2Down.play()

        collision(x, y, ss2Ypos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameSS2map3():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/brolyback.png").convert()
    ss2Image = pygame.image.load("Pics/SS2.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    whiteColor = (255, 255, 255)
    fontSize = 35

    # SS2 Jump Variables
    ss2Ypos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # SS2 Movement
    def ss2Char(y):
        gameScreen.blit(pygame.transform.scale(ss2Image, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("SSJ Power Level: " + str(counter), True, whiteColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BrolyMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    ss2Up = pygame.mixer.Sound("sounds/gokuUP.ogg")
    ss2Down = pygame.mixer.Sound("sounds/gokuDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        ss2Ypos = ss2Ypos + jumpY
        ss2Char(ss2Ypos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, ss2Ypos):
            if x <= 190 <= x + 120:
                if ss2Ypos <= y + 245 or ss2Ypos >= y + 370:
                    ss2Up.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if ss2Ypos < 10:
            ss2Ypos = 10
            ss2Up.play()
        if ss2Ypos > 505:
            ss2Ypos = 505
            ss2Down.play()

        collision(x, y, ss2Ypos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameVegetamap1():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/BGDBZ.PNG").convert()
    vegetaImage = pygame.image.load("Pics/Vegeta.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 70
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    yellowColor = (255, 223, 0)
    fontSize = 35

    # Veg Jump Variables
    vegetaYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Veg Movement
    def vegetaChar(y):
        gameScreen.blit(pygame.transform.scale(vegetaImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Vegeta Power Level: " + str(counter), True, yellowColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BGMusic.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    vegetaUp = pygame.mixer.Sound("sounds/vegataUP.ogg")
    vegetaDown = pygame.mixer.Sound("sounds/vegetaDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        vegetaYpos = vegetaYpos + jumpY
        vegetaChar(vegetaYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, vegetaYpos):
            if x <= 170 <= x + 120:
                if vegetaYpos <= y + 245 or vegetaYpos >= y + 370:
                    vegetaDown.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if vegetaYpos < 10:
            vegetaYpos = 10
            vegetaUp.play()
        if vegetaYpos > 505:
            vegetaYpos = 505
            vegetaDown.play()

        collision(x, y, vegetaYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameVegetamap2():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/SS2back.png").convert()
    vegetaImage = pygame.image.load("Pics/Vegeta.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 70
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    greenColor = (50, 205, 50)
    fontSize = 35

    # Veg Jump Variables
    vegetaYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Veg Movement
    def vegetaChar(y):
        gameScreen.blit(pygame.transform.scale(vegetaImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Vegeta Power Level: " + str(counter), True, greenColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/SS2Mus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    vegetaUp = pygame.mixer.Sound("sounds/vegataUP.ogg")
    vegetaDown = pygame.mixer.Sound("sounds/vegetaDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        vegetaYpos = vegetaYpos + jumpY
        vegetaChar(vegetaYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, vegetaYpos):
            if x <= 170 <= x + 120:
                if vegetaYpos <= y + 245 or vegetaYpos >= y + 370:
                    vegetaDown.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if vegetaYpos < 10:
            vegetaYpos = 10
            vegetaUp.play()
        if vegetaYpos > 505:
            vegetaYpos = 505
            vegetaDown.play()

        collision(x, y, vegetaYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameVegetamap3():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/brolyback.png").convert()
    vegetaImage = pygame.image.load("Pics/Vegeta.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 70
    charHeight = 90

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    whiteColor = (255, 255, 255)
    fontSize = 35

    # Veg Jump Variables
    vegetaYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Veg Movement
    def vegetaChar(y):
        gameScreen.blit(pygame.transform.scale(vegetaImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Vegeta Power Level: " + str(counter), True, whiteColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BrolyMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    vegetaUp = pygame.mixer.Sound("sounds/vegataUP.ogg")
    vegetaDown = pygame.mixer.Sound("sounds/vegetaDOWN.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        vegetaYpos = vegetaYpos + jumpY
        vegetaChar(vegetaYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, vegetaYpos):
            if x <= 170 <= x + 120:
                if vegetaYpos <= y + 245 or vegetaYpos >= y + 370:
                    vegetaDown.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if vegetaYpos < 10:
            vegetaYpos = 10
            vegetaUp.play()
        if vegetaYpos > 505:
            vegetaYpos = 505
            vegetaDown.play()

        collision(x, y, vegetaYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameBrolymap1():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/BGDBZ.png").convert()
    brolyImage = pygame.image.load("Pics/Broly.png")
    pillarImage = pygame.image.load("Pics/pillars.png")
    pillarImage2 = pygame.image.load("Pics/pillarsUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 100

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    yellowColor = (255,223,0)
    fontSize = 35

    # Broly Jump Variables
    brolyYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Broly Movement
    def brolyChar(y):
        gameScreen.blit(pygame.transform.scale(brolyImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Broly Power Level: " + str(counter), True, yellowColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/BGMusic.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    brolyUp = pygame.mixer.Sound("sounds/brolyUP.ogg")
    brolyDown = pygame.mixer.Sound("sounds/brolyDown.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        brolyYpos = brolyYpos + jumpY
        brolyChar(brolyYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, brolyYpos):
            if x <= 190 <= x + 120:
                if brolyYpos <= y + 245 or brolyYpos >= y + 370:
                    brolyUp.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if brolyYpos < 10:
            brolyYpos = 10
            brolyUp.play()
        if brolyYpos > 505:
            brolyYpos = 505
            brolyDown.play()

        collision(x, y, brolyYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameBrolymap2():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/SS2back.png").convert()
    brolyImage = pygame.image.load("Pics/Broly.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 100

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    greenColor = (50, 205, 50)
    fontSize = 35

    # Broly Jump Variables
    brolyYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Broly Movement
    def brolyChar(y):
        gameScreen.blit(pygame.transform.scale(brolyImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Broly Power Level: " + str(counter), True, greenColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/SS2Mus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    brolyUp = pygame.mixer.Sound("sounds/brolyUP.ogg")
    brolyDown = pygame.mixer.Sound("sounds/brolyDown.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        brolyYpos = brolyYpos + jumpY
        brolyChar(brolyYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, brolyYpos):
            if x <= 190 <= x + 120:
                if brolyYpos <= y + 245 or brolyYpos >= y + 370:
                    brolyUp.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if brolyYpos < 10:
            brolyYpos = 10
            brolyUp.play()
        if brolyYpos > 505:
            brolyYpos = 505
            brolyDown.play()

        collision(x, y, brolyYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

def gameBrolymap3():
    # Initialized values for size of display
    # and setup of display
    disWidth = 550
    disHeight = 600
    gameScreen = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption("Dragon Ball Z: Sukai Desutoroiyā")

    # Variables to run game
    playRun = True
    FPS = pygame.time.Clock()

    # Image Loading
    backGround = pygame.image.load("Pics/vegetaback.png").convert()
    brolyImage = pygame.image.load("Pics/Broly.png")
    pillarImage = pygame.image.load("Pics/pillarsg.png")
    pillarImage2 = pygame.image.load("Pics/pillarsgUp.png")

    # Image Scaling
    bgWidth = 750
    bgHeight = 600
    charWidth = 90
    charHeight = 100

    # Pillar Scaling and Variables
    pillarWidth = 80
    pillarHeight = 700
    x = disWidth + pillarWidth
    y = 0
    blueColor = (0, 0, 205)
    fontSize = 35

    # Broly Jump Variables
    brolyYpos = 270
    jumpY = 0

    # Background function
    def BG():
        gameScreen.blit(pygame.transform.scale(backGround, (bgWidth, bgHeight)), (0, 0))

    # Pillar function
    def pillarChar(x, y):
        gameScreen.blit(pygame.transform.scale(pillarImage2, (pillarWidth, pillarHeight)), (x, y - 439))
        gameScreen.blit(pygame.transform.scale(pillarImage, (pillarWidth, pillarHeight)), (x, y + 439))

    # Broly Movement
    def brolyChar(y):
        gameScreen.blit(pygame.transform.scale(brolyImage, (charWidth, charHeight)), (120, y))

    # Score Counter
    counter = 0

    def pyScore(counter):
        font = pygame.font.SysFont("Agency FB", fontSize)
        scoreText = font.render("Broly Power Level: " + str(counter), True, blueColor)
        gameScreen.blit(scoreText, (0, 0))

    # Audio
    bgMusic = pygame.mixer.Sound("sounds/VegetaMus.ogg")
    bgMusic.play()
    flying = pygame.mixer.Sound("sounds/flying1.ogg")
    brolyUp = pygame.mixer.Sound("sounds/brolyUP.ogg")
    brolyDown = pygame.mixer.Sound("sounds/brolyDown.ogg")

    # This helps close the window once the player is done playing
    # This while loop is also where the whole game takes place
    while playRun is True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                playRun = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    bgMusic.stop()
                    mainMenu()
                    sys.exit()
            # This makes the character jump once the space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpY = -7
                    flying.play()
            # This makes the character go down when the space bar is not pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    jumpY = 5

        # This is where I call my functions
        BG()
        pillarChar(x, y)
        pyScore(counter)

        # This makes the player jump by changing the position of the character with
        # the jump variable that increases with KEYDOWN and KEYUP
        brolyYpos = brolyYpos + jumpY
        brolyChar(brolyYpos)

        # By subtracting from x I am making the image move by 7 pixels a second
        x = x - 7

        def collision(x, y, brolyYpos):
            if x <= 190 <= x + 120:
                if brolyYpos <= y + 245 or brolyYpos >= y + 370:
                    brolyUp.play()
                    bgMusic.stop()
                    endMenu()
                    sys.exit()
                    

        if x < -pillarWidth:
            x = pillarWidth + disWidth
            y = random.randint(-200, 130)
            counter = counter + 1

        # Code help from https://github.com/Anish-Malla/Flappy-birds-game-using-pygame
        if brolyYpos < 10:
            brolyYpos = 10
            brolyUp.play()
        if brolyYpos > 505:
            brolyYpos = 505
            brolyDown.play()

        collision(x, y, brolyYpos)
        # This sets the frames per second to 60
        FPS.tick(60)

        pygame.display.update()

mainMenu()
endMenu()
pygame.quit()
