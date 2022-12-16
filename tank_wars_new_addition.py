import pygame, sys
from pygame import mixer
pygame.init()
# ეკრანის შექმნა
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
# ფონის ცვლადში შენახვა
background = pygame.image.load("images/background.jpg")

#მუსიკალური ეფექტები
mixer.music.load("images/background.wav")
mixer.music.play(-1)
shooting = mixer.Sound("images/shooting.wav")
#player1_ის შემოტანა
player1 = pygame.image.load("images/player1.png")
# player1 დაპატარავება
player1 = pygame.transform.scale(player1, (100, 100))
rect1 = player1.get_rect()
x1 = 100
y1 = 300
direction1 = "up"
alive1 = True
angle1 = 0
speed1 = 0

#player2_ის შემოტანა
player2 = pygame.image.load("images/player2.png")
# player1 დაპატარავება
player2 = pygame.transform.scale(player2, (100, 100))
rect2 = player2.get_rect()
x2 = 700
y2 = 300
direction2 = "up"
alive2 = True
angle2 = 0
speed2 = 0

destroyed_tank1 = pygame.image.load("images/explosion.png")
destroyed_tank1 = pygame.transform.scale(destroyed_tank1, (100, 100))

destroyed_tank2 = pygame.image.load("images/explosion.png")
destroyed_tank2 = pygame.transform.scale(destroyed_tank2, (100, 100))
#ტყვიის შემოტანა player1_ისთვის
bullet1 = pygame.image.load("images/bullet.png")
bullet1 = pygame.transform.scale(bullet1, (10, 10))
rect_b1 = bullet1.get_rect()
b1x = x1
b1y = y1
rect_b1.center = [b1x, b1y]
fired_b1 = False
direction_b1 = None

#ტყვიის შემოტანა player2_ისთვის
bullet2 = pygame.image.load("images/bullet.png")
bullet2 = pygame.transform.scale(bullet2, (10, 10))
rect_b2 = bullet2.get_rect()
b2x = x2
b2y = y2
rect_b2.center = [b2x, b2y]
fired_b2 = False
direction_b2 = None

bullet_speed = 0.7

font1 = pygame.font.Font("freesansbold.ttf", 70)
def game_over():
    game_over_text = font1.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

while True:
    # ფონის დახატვა ეკრანზე
    screen.blit(background, (0, 0))
    # მართკუთხედის განთავსება
    rect1.center = [x1, y1]
    rect2.center = [x2, y2]
    #player1 დახატვა ეკრანზე
    screen.blit(player1, rect1)
    screen.blit(player2, rect2)
    if alive1 != True or alive2 != True:
        break
    # ჩვენი ქმედებების შემოწმება
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if alive1 == True and alive2 == True:
            if event.type == pygame.KEYDOWN:
                #player2
                if event.key == pygame.K_d:
                    player2 = pygame.transform.rotate(player2, -90)
                    angle2 -= 90
                    if abs(angle2) >= 360:
                        angle2 = 0
                if event.key == pygame.K_a:
                    player2 = pygame.transform.rotate(player2, 90)
                    angle2 += 90
                    if abs(angle2) >= 360:
                        angle2 = 0
                if event.key == pygame.K_w:
                    speed2 = 0.5
                if event.key == pygame.K_s:
                    speed2 = -0.5
                if event.key == pygame.K_z and fired_b2 == False:
                    shooting.play()
                    fired_b2 = True
                    direction_b2 = direction2
                    if direction_b2 == "right":
                        b2x = x2 + 50
                        b2y = y2
                    elif direction_b2 == "left":
                        b2x = x2 - 50
                        b2y = y2
                    elif direction_b2 == "up":
                        b2x = x2
                        b2y = y2 - 50
                    else:
                        b2x = x2
                        b2y = y2 + 50
                #player1
                if event.key == pygame.K_RIGHT:
                    player1 = pygame.transform.rotate(player1, -90)
                    angle1 -= 90
                    if abs(angle1) >= 360:
                        angle1 = 0
                if event.key == pygame.K_LEFT:
                    player1 = pygame.transform.rotate(player1, 90)
                    angle1 += 90
                    if abs(angle1) >= 360:
                        angle1 = 0
                if event.key == pygame.K_UP:
                    speed1 = 0.5
                if event.key == pygame.K_DOWN:
                    speed1 = -0.5
                if event.key == pygame.K_SPACE and fired_b1 == False:
                    shooting.play()
                    fired_b1 = True
                    direction_b1 = direction1
                    if direction_b1 == "right":
                        b1x = x1 + 50
                        b1y = y1
                    elif direction_b1 == "left":
                        b1x = x1 - 50
                        b1y = y1
                    elif direction_b1 == "up":
                        b1x = x1
                        b1y = y1 - 50
                    else:
                        b1x = x1
                        b1y = y1 + 50
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    speed1 = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    speed2 = 0
    if alive1 == True and alive2 == True:
        # player1 ტანკის მოძრაობა
        if angle1 == -90 or angle1 == 270:
            direction1 = "right"
            x1 += speed1
        elif angle1 == 90 or angle1 == -270:
            direction1 = "left"
            x1 -= speed1
        elif angle1 == 0:
            direction1 = "up"
            y1 -= speed1
        else:
            direction1 = "down"
            y1 += speed1
        # player2 ტანკის მოძრაობა
        if angle2 == -90 or angle2 == 270:
            direction2 = "right"
            x2 += speed2
        elif angle2 == 90 or angle2 == -270:
            direction2 = "left"
            x2 -= speed2
        elif angle2 == 0:
            direction2 = "up"
            y2 -= speed2
        else:
            direction2 = "down"
            y2 += speed2
    #bullet1 ტყვიის გასროლა
        if fired_b1 == True:
            rect_b1.center = [b1x, b1y]
            screen.blit(bullet1, rect_b1)
            if direction_b1 == "right":
                b1x += bullet_speed
            elif direction_b1 == "left":
                b1x -= bullet_speed
            elif direction_b1 == "up":
                b1y -= bullet_speed
            else:
                b1y += bullet_speed
        # bullet2 ტყვიის გასროლა
        if fired_b2 == True:
            rect_b2.center = [b2x, b2y]
            screen.blit(bullet2, rect_b2)
            if direction_b2 == "right":
                b2x += bullet_speed
            elif direction_b2 == "left":
                b2x -= bullet_speed
            elif direction_b2 == "up":
                b2y -= bullet_speed
            else:
                b2y += bullet_speed
    #გაცდა თუ არა ეკრანს ტყვია
        if b1x < 0 or b1x > width or b1y <0 or b1y > height:
            fired_b1 = False
        # გაცდა თუ არა ეკრანს ტყვია
        if b2x < 0 or b2x > width or b2y < 0 or b2y > height:
            fired_b2 = False

        #collision
        if fired_b1 == True:
            if rect2.collidepoint(b1x, b1y):
                alive2 = False
        if fired_b2 == True:
            if rect1.collidepoint(b2x, b2y):
                alive1 = False
        if rect1.collidepoint(x2, y2):
            alive1 = False
            alive2 = False

        if alive1 == False:
            destroyed_tank1 = pygame.transform.rotate(destroyed_tank1, angle1)
            player1 = destroyed_tank1
        if alive2 == False:
            destroyed_tank2 = pygame.transform.rotate(destroyed_tank2, angle2)
            player2 = destroyed_tank2
    #საზღვრები
    if x1 < 50:
        x1 = 50
    if x1 > width - 50:
        x1 = width - 50
    if y1 < 50:
        y1 = 50
    if y1 > height - 50:
        y1 = height - 50

    if x2 < 50:
        x2 = 50
    if x2 > width - 50:
        x2 = width - 50
    if y2 < 50:
        y2 = 50
    if y2 > height - 50:
        y2 = height - 50
    #ეკრანის აფდეითი
    pygame.display.update()
game_over()