import pygame
import time, random, sys

pygame.init()
width = 800
height = 600
speed = 4
fps = 100
car_width = 57
car_length = 108

# global screen

screen = pygame.display.set_mode((width, height))
mainClock = pygame.time.Clock()

player_car = pygame.image.load("Cars/Lamborghini_1.png")
grass = pygame.image.load("SideTrack/grass.jpg")
yellow_strip = pygame.image.load("SideTrack/yellow_strip.jpg")
strip = pygame.image.load("SideTrack/strip.jpg")

Intro_image = pygame.image.load("Background/carBackground.jpg")

pygame.mixer.music.load('SoundTrack/NoTurningBack.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.6)

myfont = pygame.font.SysFont("None", 100)
crashed_message = myfont.render("CAR CRASHED !!!",0, (255,255,255))

clock = pygame.time.Clock()
clock.tick(fps)

pygame.display.set_caption("Quynh Anh Race Game !!!")  

def addSideTrack():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    for i in range(7):
        screen.blit(yellow_strip,(375, i*100))
        screen.blit(strip,(120,0))
        screen.blit(strip,(680,0))


def intro_loop():
    intro = True
    pygame.mixer.music.set_volume(0.6)
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

        textSurface,textRect = text_object("EXIT", small_text, (169,169,169))
        textRect.center=(705, 565)
        screen.blit(textSurface, textRect)

        if mouse[1] > 540 and mouse[1] < 590:
            if mouse[0] > 20 and mouse[0] < 170:
                textSurface,textRect = text_object("START", small_text, (255,255,255))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    game_loop()
            else:
                textSurface,textRect = text_object("START", small_text, (169,169,169))
                textRect.center=(95, 565)
                screen.blit(textSurface, textRect)
            
            if mouse[0] > 330 and mouse[0] < 480:
                textSurface,textRect = text_object("SETTING", small_text, (255,255,255))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)
            else:
                textSurface,textRect = text_object("SETTING", small_text, (169,169,169))
                textRect.center=(405, 565)
                screen.blit(textSurface, textRect)

            if mouse[0] > 630 and mouse[0] < 780:
                textSurface,textRect = text_object("EXIT", small_text, (255,255,255))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)
                if click_action == (1,0,0):
                    pygame.quit()
                    sys.exit()
            else:
                textSurface,textRect = text_object("EXIT", small_text, (169,169,169))
                textRect.center=(705, 565)
                screen.blit(textSurface, textRect)

        pygame.display.update()
        


def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("Cars/car.jpg")
    if obs == 1:
        obs_pic = pygame.image.load("Cars/car1.jpg")
    if obs == 2:
        obs_pic = pygame.image.load("Cars/car2.jpg")
    if obs == 3:
        obs_pic = pygame.image.load("Cars/car3.jpg")
    if obs == 4:
        obs_pic = pygame.image.load("Cars/car4.jpg")
    if obs == 5:
        obs_pic = pygame.image.load("Cars/car5.jpg")
    if obs == 6:
        obs_pic = pygame.image.load("Cars/car6.jpg")
    if obs == 7:
        obs_pic = pygame.image.load("Cars/car7.jpg")
    screen.blit(obs_pic, (obs_x, obs_y))


def score_card(car_passed, score):
    font = pygame.font.SysFont(None, 35)
    passed = font.render("Passed: " + str(car_passed), True, (255,255,255))
    score = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(passed, (0,50))
    screen.blit(score, (0,100))
    pygame.display.update()


def moveCar(object, x, y):
    screen.blit(object, (x, y))


def text_object(text, font, textColor):
    textSurface = font.render(text, True, textColor)
    return textSurface, textSurface.get_rect()


def game_loop():

    quit_action = False
    x_change = 0
    x = width/2 - 19
    y = height - 100
    obstacle_speed = 10
    obs = random.randrange(0,7)
    y_change = 0
    obs_x = random.randrange(200,650)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125
    score = 0
    car_passed = 0

    while not quit_action:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_action = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -speed
                if event.key == pygame.K_RIGHT:
                    x_change = speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x += x_change
        
        screen.fill((119, 119, 119))
        addSideTrack()

        moveCar(player_car, x, y)
        score_card(car_passed, score)

        obs_y -= (obstacle_speed/4)
        obstacle(obs_x, obs_y, obs)
        obs_y += obstacle_speed

        

        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(180,650)
            obs = random.randrange(0,7)
            car_passed += 1
            score = car_passed * 10
            obstacle_speed += 0.1

        if y < obs_y + enemy_height:
            if x > obs_x and x < obs_x + enemy_width or x + car_width > obs_x and x+car_width < obs_x + enemy_width:
                screen.blit(crashed_message, (120,300))
                pygame.display.update()
                time.sleep(3)
                game_loop()
                

        if x > 680 - car_width or x < 110:
            screen.blit(crashed_message, (120,300))
            pygame.display.update()
            time.sleep(3)
            game_loop()
            

        pygame.display.update()
        clock.tick(fps)


intro_loop()
pygame.quit()
# sys.exit()
quit()