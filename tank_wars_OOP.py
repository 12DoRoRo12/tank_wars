import pygame, sys
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
fps = 600
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

pygame.mouse.set_visible(False)

mixer.music.load("images/background.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.5)

shooting = mixer.Sound("images/shooting.wav")


pygame.display.set_caption("Tank Wars!")
icon = pygame.image.load("images/player1.png")
pygame.display.set_icon(icon)

background = pygame.image.load("images/background.jpg")

player1_image = pygame.image.load("images/player1.png")
player1_image = pygame.transform.scale(player1_image, (100, 100))

player2_image = pygame.image.load("images/player2.png")
player2_image = pygame.transform.scale(player2_image, (100, 100))

destroyed_tank = pygame.image.load("images/explosion.png")
destroyed_tank = pygame.transform.scale(destroyed_tank, (100, 100))

class Tank(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=[self.x, self.y])
        self.alive = True
        self.speed = 0
        self.angle = 0
        self. direction = "up"

    def update(self):
        self.rect.center = [self.x, self.y]

        #მიმართულების განსაზღვრა
        if self.angle == 0:
            self.direction = "up"
        elif abs(self.angle) == 180:
            self.direction = "down"
        elif self.angle == -90 or self.angle == 270:
            self.direction = "right"
        else:
            self.direction = "left"
        #მოძრაობა
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed
        #საზღვრები
        if self.x < 50:
            self.x = 50
        if self.x > width - 50:
            self.x = width - 50
        if self.y < 50:
            self.y = 50
        if self.y > height - 50:
            self.y = height - 50






player1 = Tank(player1_image, 150, height / 2)
player2 = Tank(player2_image, width - 150, height / 2)

player1_group = pygame.sprite.Group()
player1_group.add(player1)

player2_group = pygame.sprite.Group()
player2_group.add(player2)

bullet_image = pygame.image.load("images/bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (10, 10))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=[self.x, self.y])
        self.fired = False
        self.speed = 0
        self. direction = "up"
    def update(self):
        self.rect.center = [self.x, self.y]
        #როდის შეიცვალოს სიჩქარე
        if self.fired == True:
            self.speed = 0.7
        #მოძრაობის ფუნქციონალი
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "right":
            self.x += self.speed
        else:
            self.x -= self.speed

        #ტყვიის დაბრუნება
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            self.fired = False


b1 = Bullet(bullet_image, player1.x, player1.y)
b1_bullet_group = pygame.sprite.Group()
b1_bullet_group.add(b1)
b2 = Bullet(bullet_image, player2.x, player2.y)
b2_bullet_group = pygame.sprite.Group()
b2_bullet_group.add(b2)

font = pygame.font.Font(None, 80)
def game_over(font):
    text = font.render("Game Over!", True, (255, 255, 255))
    text_rect = text.get_rect(center=[width/2, height/2])
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

run = True
while run:
    clock.tick(fps)
    screen.blit(background, (0, 0))
    if b1.fired == False:
        b1.x = player1.x
        b1.y = player1.y

    if b2.fired == False:
        b2.x = player2.x
        b2.y = player2.y

    if b1.fired == True:
        b1_bullet_group.draw(screen)
        b1_bullet_group.update()

    if b2.fired == True:
        b2_bullet_group.draw(screen)
        b2_bullet_group.update()


    if player1.alive == False or player2.alive == False:
        run = False

    player1_group.draw(screen)
    player1_group.update()
    player2_group.draw(screen)
    player2_group.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            #პირველი მოთამაშე
            if event.key == pygame.K_RIGHT:
                player1.image = pygame.transform.rotate(player1.image, -90)
                player1.angle += -90
                if abs(player1.angle) == 360:
                    player1.angle = 0
            if event.key == pygame.K_LEFT:
                player1.image = pygame.transform.rotate(player1.image, 90)
                player1.angle += 90
                if abs(player1.angle) == 360:
                    player1.angle = 0
            if event.key == pygame.K_UP:
                player1.speed = 0.3
            if event.key == pygame.K_DOWN:
                player1.speed = -0.3
            # მეორე მოთამაშე
            if event.key == pygame.K_d:
                player2.image = pygame.transform.rotate(player2.image, -90)
                player2.angle += -90
                if abs(player2.angle) == 360:
                    player2.angle = 0
            if event.key == pygame.K_a:
                player2.image = pygame.transform.rotate(player2.image, 90)
                player2.angle += 90
                if abs(player2.angle) == 360:
                    player2.angle = 0
            if event.key == pygame.K_w:
                player2.speed = 0.3
            if event.key == pygame.K_s:
                player2.speed = -0.3


            #გასროლილია თუ არა ტყვია
            if event.key == pygame.K_SPACE and b1.fired == False:
                shooting.play()
                b1.direction = player1.direction
                b1.speed = 0.5
                b1.fired = True

            if event.key == pygame.K_z and b2.fired == False:
                shooting.play()
                b2.direction = player2.direction
                b2.speed = 0.5
                b2.fired = True

        if event.type == pygame.KEYUP:
            # პირველი მოთამაშე
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1.speed = 0
            # მეორე მოთამაშე
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player2.speed = 0

    #ტყვიის მოხვედრის ფუნქციონალი
    if player1.rect.colliderect(b2.rect):
        player1.image = pygame.transform.rotate(destroyed_tank, player1.angle)
        player1.alive = False
        b2.fired = False

    if player2.rect.colliderect(b1.rect):
        player2.image = pygame.transform.rotate(destroyed_tank, player2.angle)
        player2.alive = False
        b1.fired = False

    if player1.rect.colliderect(player2.rect):
        player1.image = pygame.transform.rotate(destroyed_tank, player1.angle)
        player2.image = pygame.transform.rotate(destroyed_tank, player2.angle)
        player1.alive = False
        player2.alive = False



    pygame.display.update()

game_over(font)



