import pygame
import time, random, sys, os
from pygame.locals import *

# Game Data
pygame.init()
width = 800
height = 600
speed = 4
fps = 100
player_car_width = 57
player_car_length = 108

font = pygame.font.SysFont(None, 30)

FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 13
BADDIEMAXSPEED = 25
ADDNEWBADDIERATE = 40
PLAYERMOVERATE = 10

screen = pygame.display.set_mode((width, height))
mainClock = pygame.time.Clock()

player_car = pygame.image.load("Cars/Lamborghini_1.png")

# Cars obstacle
Cars_path = b'C:\Users\DELL\Desktop\Support QA\CarRace\Cars'
Obstacle_path = b'C:\Users\DELL\Desktop\Support QA\CarRace\Rock'
paths = []
Cars = []

for i in os.listdir(Cars_path):
    Cars.append(pygame.image.load(os.path.join(Cars_path, i)))

# for i in os.listdir(Obstacle_path):
#     Rock.append(pygame.image.load(os.path.join(Obstacle_path, i)))


playerRect = player_car.get_rect()

grass = pygame.image.load("SideTrack/grass.jpg")
yellow_strip = pygame.image.load("SideTrack/yellow_strip.jpg")
strip = pygame.image.load("SideTrack/strip.jpg")

Intro_image = pygame.image.load("Background/carBackground.jpg")
Pause_image = pygame.image.load("Background/PauseBackground.jpg")
Game_over_image = pygame.image.load("Background/Gameover3.jpg")
Setting_page_image = pygame.image.load("Background/SettingBackground.jpg")

cow_L = pygame.image.load("Background/cow_left.png")
cow_R = pygame.image.load("Background/cow_right.png")
obstacle_1 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (1).png"), (1024*0.05 , 681*0.05))
obstacle_2 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (2).png"), (800*0.065 , 423*0.065))
obstacle_3 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (3).png"), (1279*0.1 , 975*0.1))
obstacle_4 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (4).png"), (1016*0.1 , 761*0.1))
obstacle_5 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (5).png"), (527*0.1 , 1517*0.1))
obstacle_6 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (6).png"), (527*0.15 , 800*0.15))
obstacle_7 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (7).png"), (2768*0.05 , 1500*0.05))
obstacle_8 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (8).png"), (668*0.1 , 1196*0.1))
obstacle_9 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (9).png"), (1920*0.02 , 1800*0.02))
obstacle_10 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (10).png"), (1024*0.05 , 1024*0.05))
obstacle_11 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (11).png"), (1543*0.015 , 3304*0.015))
obstacle_12 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (12).png"), (3000*0.025 , 1943*0.025))
obstacle_13 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com (15).png"), (1000*0.1 , 1000*0.1))
obstacle_14 = pygame.transform.scale(pygame.image.load("Rock/pngwing.com.png"), (564*0.1 , 511*0.1))
obstacle_15 = pygame.transform.scale(pygame.image.load("Rock/pngwing (16).com.png"), (511*0.1 , 682*0.1))
Rock = [obstacle_1, obstacle_2, obstacle_3, obstacle_4, obstacle_5, obstacle_6, obstacle_7,
obstacle_8, obstacle_9, obstacle_10, obstacle_11, obstacle_12, obstacle_13, obstacle_14, obstacle_15]

for i in Rock:
    Cars.append(i)

pygame.mixer.music.load('SoundTrack/Tokyo_Drift.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.6)

myfont = pygame.font.SysFont("None", 100)
crashed_message = myfont.render("CAR CRASHED !!!",0, (255,0,0))
# crashed_message = myfont.render("CAR CRASHED !!!",0, (255,255,255))

clock = pygame.time.Clock()
clock.tick(fps)

pygame.display.set_caption("Quynh Anh Race Game !!!")  



# Intro page
def text_object(text, font, textColor):
    textSurface = font.render(text, True, textColor)
    return textSurface, textSurface.get_rect()


def terminate():
    pygame.quit()
    sys.exit()


def intro_loop():
    intro = True
    pygame.mixer.music.load('SoundTrack/Tokyo_Drift.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(2)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(Intro_image,(0,0))
        font = pygame.font.SysFont(None, 100)
        title = font.render("HUMOR CAR GAME", True, (241,250,54))
        screen.blit(title, (80,20))
        pygame.draw.rect(screen, (113,112,117), (20,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (330,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (630,540,150,50))

        pygame.draw.rect(screen, (28,23,7), (22,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (332,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (632,542,146,46))
        
        mouse = pygame.mouse.get_pos()
        click_action = pygame.mouse.get_pressed()

        small_text = pygame.font.Font(None, 40)

        textSurface,textRect = text_object("START", small_text, (169,169,169))
        textRect.center=(95, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("SETTING", small_text, (169,169,169))
        textRect.center=(405, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("QUIT", small_text, (169,169,169))
        textRect.center=(705, 565)
        screen.blit(textSurface, textRect)

        if mouse[1] > 540 and mouse[1] < 590:
            if mouse[0] > 20 and mouse[0] < 170:
                textSurface,textRect = text_object("START", small_text, (255,255,255))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    # game_loop()
                    # put game loop() here !!!
                    break
            else:
                textSurface,textRect = text_object("START", small_text, (169,169,169))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
            
            if mouse[0] > 330 and mouse[0] < 480:
                textSurface,textRect = text_object("SETTING", small_text, (255,255,255))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    time.sleep(0.5)
                    setting_page()
            else:
                textSurface,textRect = text_object("SETTING", small_text, (169,169,169))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)

            if mouse[0] > 630 and mouse[0] < 780:
                textSurface,textRect = text_object("QUIT", small_text, (255,255,255))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    pygame.quit()
                    sys.exit()
            else:
                textSurface,textRect = text_object("QUIT", small_text, (169,169,169))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)

        pygame.display.update()


def setting_page():
    setting = True
    pygame.mixer.music.set_volume(0.6)
    while setting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(pygame.transform.scale(Setting_page_image, (800,600)),(0,0))
        font = pygame.font.SysFont(None, 100)
        # title = font.render("PAUSE !!!", True, (255,255,255))
        # screen.blit(title, (250,20))
        pygame.draw.rect(screen, (113,112,117), (20,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (330,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (630,540,150,50))

        pygame.draw.rect(screen, (28,23,7), (22,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (332,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (632,542,146,46))
        
        mouse = pygame.mouse.get_pos()
        click_action = pygame.mouse.get_pressed()

        small_text = pygame.font.Font(None, 40)

        textSurface,textRect = text_object("EASY", small_text, (169,169,169))
        textRect.center=(95, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("MEDIUM", small_text, (169,169,169))
        textRect.center=(405, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("HARD", small_text, (169,169,169))
        textRect.center=(705, 565)
        screen.blit(textSurface, textRect)

        if mouse[1] > 540 and mouse[1] < 590:
            if mouse[0] > 20 and mouse[0] < 170:
                textSurface,textRect = text_object("EASY", small_text, (255,255,255))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    time.sleep(0.5)
                    easy_mode()
                    break
            else:
                textSurface,textRect = text_object("EASY", small_text, (169,169,169))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
            
            if mouse[0] > 330 and mouse[0] < 480:
                textSurface,textRect = text_object("MEDIUM", small_text, (255,255,255))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    time.sleep(0.5)
                    medium_mode()
                    break
            else:
                textSurface,textRect = text_object("MEDIUM", small_text, (169,169,169))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)

            if mouse[0] > 630 and mouse[0] < 780:
                textSurface,textRect = text_object("HARD", small_text, (255,255,255))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    time.sleep(0.5)
                    hard_mode()
                    break
            else:
                textSurface,textRect = text_object("HARD", small_text, (169,169,169))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)

        pygame.display.update()

def pause_loop():
    Pause = True
    pygame.mixer.music.set_volume(0.6)
    while Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(pygame.transform.scale(Pause_image, (800,600)),(0,0))
        font = pygame.font.SysFont(None, 100)
        title = font.render("PAUSE !!!", True, (255,255,255))
        screen.blit(title, (250,20))
        pygame.draw.rect(screen, (113,112,117), (20,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (330,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (630,540,150,50))

        pygame.draw.rect(screen, (28,23,7), (22,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (332,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (632,542,146,46))
        
        mouse = pygame.mouse.get_pos()
        click_action = pygame.mouse.get_pressed()

        small_text = pygame.font.Font(None, 40)

        textSurface,textRect = text_object("RESUME", small_text, (169,169,169))
        textRect.center=(95, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("SETTING", small_text, (169,169,169))
        textRect.center=(405, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("QUIT", small_text, (169,169,169))
        textRect.center=(705, 565)
        screen.blit(textSurface, textRect)

        if mouse[1] > 540 and mouse[1] < 590:
            if mouse[0] > 20 and mouse[0] < 170:
                textSurface,textRect = text_object("RESUME", small_text, (255,255,255))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    # game_loop()
                    # put game loop() here !!!
                    break
            else:
                textSurface,textRect = text_object("RESUME", small_text, (169,169,169))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
            
            if mouse[0] > 330 and mouse[0] < 480:
                textSurface,textRect = text_object("SETTING", small_text, (255,255,255))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    time.sleep(0.5)
                    setting_page()
            else:
                textSurface,textRect = text_object("SETTING", small_text, (169,169,169))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)

            if mouse[0] > 630 and mouse[0] < 780:
                textSurface,textRect = text_object("QUIT", small_text, (255,255,255))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    terminate()
                    
            else:
                textSurface,textRect = text_object("QUIT", small_text, (169,169,169))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
        
        pygame.display.update()


def game_over_loop():
    game_over = True
    pygame.mixer.music.load('SoundTrack/laugh.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(2)
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(pygame.transform.scale(Game_over_image, (800,600)),(0,0))
        font = pygame.font.SysFont(None, 100)
        title = font.render("PAUSE !!!", True, (255,255,255))
        # screen.blit(title, (250,20))
        pygame.draw.rect(screen, (113,112,117), (450,540,150,50))
        pygame.draw.rect(screen, (113,112,117), (630,540,150,50))

        pygame.draw.rect(screen, (28,23,7), (452,542,146,46))
        pygame.draw.rect(screen, (28,23,7), (632,542,146,46))
        
        mouse = pygame.mouse.get_pos()
        click_action = pygame.mouse.get_pressed()

        small_text = pygame.font.Font(None, 40)

        textSurface,textRect = text_object("RESTART", small_text, (169,169,169))
        textRect.center=(525, 565)
        screen.blit(textSurface, textRect)

        textSurface,textRect = text_object("QUIT", small_text, (169,169,169))
        textRect.center=(705, 565)
        screen.blit(textSurface, textRect)

        if mouse[1] > 540 and mouse[1] < 590:
            if mouse[0] > 450 and mouse[0] < 600:
                textSurface,textRect = text_object("RESTART", small_text, (255,255,255))
                textRect.center=(525, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    # game_loop()
                    # put game loop() here !!!
                    break
            else:
                textSurface,textRect = text_object("RESTART", small_text, (169,169,169))
                textRect.center=(525, 565)
                screen.blit(textSurface, textRect)

            if mouse[0] > 630 and mouse[0] < 780:
                textSurface,textRect = text_object("QUIT", small_text, (255,255,255))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    terminate()
                    
            else:
                textSurface,textRect = text_object("QUIT", small_text, (169,169,169))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
        
        pygame.display.update()


# Score game
def score_card(car_passed, score):
    font = pygame.font.SysFont(None, 35)
    passed = font.render("Passed: " + str(car_passed), True, (255,255,255))
    score = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(passed, (0,50))
    screen.blit(score, (0,100))
    pygame.display.update()


def addSideTrack():
    screen.fill((119, 119, 119))
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    for i in range(7):
        screen.blit(strip,(120,0))
        screen.blit(strip,(680,0))
    pygame.display.update()


def drawText(text, font, surface, x, y, TEXTCOLOR):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def Crashed():
    screen.blit(crashed_message, (120,300))
    pygame.display.update()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('SoundTrack/Crash.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(2)
    time.sleep(1)
    screen.blit(pygame.transform.scale(cow_L, (200,200)), (0,100))
    screen.blit(pygame.transform.scale(cow_R, (200,200)), (600,400))
    pygame.display.update()
    time.sleep(4)
    pygame.mixer.music.stop()
    game_over_loop()


def easy_mode():

    global BADDIEMINSIZE
    global BADDIEMAXSIZE
    global BADDIEMINSPEED
    global BADDIEMAXSPEED
    global ADDNEWBADDIERATE
    global PLAYERMOVERATE

    BADDIEMINSIZE = 14
    BADDIEMAXSIZE = 41
    BADDIEMINSPEED = 9
    BADDIEMAXSPEED = 15
    ADDNEWBADDIERATE = 90
    PLAYERMOVERATE = 5

def medium_mode():

    global BADDIEMINSIZE
    global BADDIEMAXSIZE
    global BADDIEMINSPEED
    global BADDIEMAXSPEED
    global ADDNEWBADDIERATE
    global PLAYERMOVERATE

    BADDIEMINSIZE = 14
    BADDIEMAXSIZE = 41
    BADDIEMINSPEED = 12
    BADDIEMAXSPEED = 20
    ADDNEWBADDIERATE = 60
    PLAYERMOVERATE = 5

def hard_mode():

    global BADDIEMINSIZE
    global BADDIEMAXSIZE
    global BADDIEMINSPEED
    global BADDIEMAXSPEED
    global ADDNEWBADDIERATE
    global PLAYERMOVERATE

    BADDIEMINSIZE = 14
    BADDIEMAXSIZE = 41
    BADDIEMINSPEED = 19
    BADDIEMAXSPEED = 25
    ADDNEWBADDIERATE = 40
    PLAYERMOVERATE = 5

# Main Game
Running = True

zero = 0

if not os.path.exists("data/save.dat"):
    f=open("data/save.dat",'w')
    f.write(str(zero))
    f.close()   
v=open("data/save.dat",'r')
topScore = int(v.readline())
v.close()



while Running:
    # start of the game
    baddies = []
    playerRect.topleft = (width / 2, height - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    screen.fill((119, 119, 119))
    car_size = 0.85
    lane_marker_move_y = 0
    score = 0
    intro_loop()
    
    
    while True: # the game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
                if event.key == ord('p'):
                    pause_loop()

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()
            

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

        
        # Add new baddies at the top of the screen
        OBSTACLE_SPEED = (BADDIEMINSPEED + BADDIEMAXSPEED)/2
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect': pygame.Rect(random.randint(140, 650), 0 - baddieSize, 56*car_size, 125*car_size),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(random.choice(Cars), (56*car_size, 125*car_size)),
                        }
            baddies.append(newBaddie)

            newObstacle = {'rect': pygame.Rect(random.randint(140, 650), 0 - baddieSize, 56*car_size, 50*car_size),
                        'speed': random.randint(OBSTACLE_SPEED, OBSTACLE_SPEED),
                        'surface':random.choice(Rock),
                        }
            # baddies.append(newObstacle)

            
            # sideLeft= {'rect': pygame.Rect(0,0,100,600),
            #            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
            #            'surface':pygame.transform.scale(grass, (100, 600)),
            #            }
            # baddies.append(sideLeft)
            # sideRight= {'rect': pygame.Rect(500,0,500,600),
            #            'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
            #            'surface':pygame.transform.scale(grass, (100, 600)),
            #            }
            # baddies.append(sideRight)

        # Move the player around.
        if moveLeft and playerRect.left > 100:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        elif moveLeft and playerRect.left <= 100:
            Crashed()
            break
        if moveRight and playerRect.right < width-100:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        elif moveRight and playerRect.right >= width-100:
            Crashed()
            break
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < height:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # yellowStrip['rect'].move_ip(0, yellowStrip['speed'])
        # if yellow_strip['rect'].top > height:
        #     baddies.remove(b)

        for b in baddies[:]:
            if b['rect'].top > height:
                score += 1
                baddies.remove(b)

        # Draw the game world on the window.
        # screen.fill((119, 119, 119))
        addSideTrack()
        ratio = 2
        marker_width = 10
        marker_height = 50
        lane_marker_move_y += 2 * ratio
        if lane_marker_move_y >= marker_height * 2:
            lane_marker_move_y = 0
        for y in range(marker_height * -2, height, marker_height * 2):
            pygame.draw.rect(screen, (255,255,255), (100 + 100, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, (255,255,255), (400, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, (255,255,255), (500 + 100, y + lane_marker_move_y, marker_width, marker_height))
        pygame.display.update()

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, screen, 128, 0, (255,255,255))
        drawText('Top Score: %s' % (topScore), font, screen,128, 20, (255,255,255))
        
        screen.blit(player_car, playerRect)

        
        for b in baddies:
            # print(b['rect'].center)
            # print('*'*50)
            screen.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                g=open("data/save.dat",'w')
                g.write(str(score))
                g.close()
                topScore = score
            
            Crashed()
            break
        
        # print(playerRect[1])

        mainClock.tick(FPS)
