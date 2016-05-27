import pygame
import time
import random
from random import randint
from enemy import Enemy
from bullet import Bullet
from bullet import MyBullet
from ship import Ship

pygame.init()

display_width = 500
display_height = 300

black = (0,0,0)
white = (255, 255, 255)
block_color = (53, 115, 255)
green = (0, 200, 0)
red = (200, 0, 0)
bright_red = (255, 0,0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invader Clone')
clock = pygame.time.Clock()


all_sprites_list = pygame.sprite.Group()
our_bullet_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()






start_x = 50
start_y = 50
for en in range(0, 9):
    en = Enemy('third', white, 15, 15)
    en.rect.x = start_x
    en.rect.y = start_y
    all_sprites_list.add(en)
    start_y += 20


    en = Enemy('second', white, 15, 15)
    en.rect.x = start_x
    en.rect.y = start_y
    all_sprites_list.add(en)
    start_y += 20

    en = Enemy('second', white, 15, 15)
    en.rect.x = start_x
    en.rect.y = start_y
    all_sprites_list.add(en)
    start_y += 20

    en = Enemy('first', white, 15, 15)
    en.rect.x = start_x
    en.rect.y = start_y
    all_sprites_list.add(en)
    start_y += 20

    en = Enemy('first', white, 15, 15)
    en.rect.x = start_x
    en.rect.y = start_y
    start_y = 50

    all_sprites_list.add(en)
    start_x += 30

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def printScore(current):
    largeText = pygame.font.Font(None, 25)
    TextSurf, TextRect = text_objects(current, largeText)
    TextRect.center = (40, 30)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def printLives(current):
    largeText = pygame.font.Font(None, 25)
    TextSurf, TextRect = text_objects(current, largeText)
    TextRect.center = (display_width - 40, 30)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def quitgame():
    pygame.quit()
    quit()

def game_loop():
# Used for score
    score = 0
# Used for the position of our ship
    x = (display_width * 0.45)
    y = (display_height * 0.9)
# Initiate ship
    ship = Ship(22, 16)
    ship.rect.x = x
    ship.rect.y = y
    our_ship = pygame.sprite.GroupSingle(ship)
    print ship.rect.x
    print ship.rect.y

# Used to move our space ship
    x_change = 0
# Keeps the game running
    gameExit = False
# Used to allow one shot per screen
    noBullet = True
    middle_enemy_list = []

# Define user events
    move_side_event = pygame.USEREVENT + 1
    pygame.time.set_timer(move_side_event, 3000)

    fire_top_row = pygame.USEREVENT + 2
    pygame.time.set_timer(fire_top_row, 7000)

    fire_midle_row = pygame.USEREVENT + 3
    pygame.time.set_timer(fire_midle_row, 5000)

    while not gameExit:
# All events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == move_side_event:
                for edir in all_sprites_list:
                    if edir.setDirection((display_width, display_height)) == True:
                        break
                all_sprites_list.update()

            if event.type == fire_top_row:
                middle_enemy_list = []
                for enemy in all_sprites_list:
                    if enemy.row == 'second':
                        middle_enemy_list.append(enemy)
                if len(middle_enemy_list) > 0:
                    _second = middle_enemy_list[randint(0,len(middle_enemy_list) - 1)]
                    ebullet = Bullet()
                    ebullet.rect.x = _second.rect.x + 7
                    ebullet.rect.y = _second.rect.y + 7
                    our_bullet_list.add(ebullet)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_SPACE:
                    if noBullet == True:
                        fbullet = MyBullet()
                        fbullet.rect.x = ship.rect.x + ship.image.get_width() / 2
                        fbullet.rect.y = ship.rect.y - 10
                        bullet_list.add(fbullet)
                        noBullet = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

# Used for changing the position of our ship
        x += x_change
        # pritn x_change

        if x_change is not 0:
            our_ship.update(x, display_width)

        if len(our_bullet_list) > 0:
            our_bullet_list.update()


        gameDisplay.fill(black)

        our_ship.draw(gameDisplay)
        our_bullet_list.draw(gameDisplay)
        bullet_list.draw(gameDisplay)
        all_sprites_list.draw(gameDisplay)

        printScore("Score: " + str(score))
        printLives("Lives: " + str(ship.lives))

        collided = None
        if noBullet == False:
            bullet_list.update()
            for b in bullet_list:
                if b.rect.y < 10:
                    b.kill()
                    noBullet = True
            collided = pygame.sprite.groupcollide(all_sprites_list, bullet_list, False, False)
            if collided:
                for killed in collided:
                    killed_with_list = collided[killed]
                    for k in killed_with_list:
                        k.kill()
                        noBullet = True
                    score += killed.points
                    killed.kill()

        if pygame.sprite.groupcollide(our_ship, our_bullet_list, False, True):
            ship.lives -= 1




        pygame.display.flip()
        clock.tick(60)

##game_intro()
game_loop()
pygame.quit()
quit()
