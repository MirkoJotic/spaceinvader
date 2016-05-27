import pygame
WHITE = (255, 255, 255)

class Ship(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super(Ship, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.image = pygame.image.load("resources/Ship.png").convert_alpha()


        self.lives = 3

        self.rect = self.image.get_rect()

    def update(self, x, screen):
        print screen
        if x > 0 and x + self.image.get_width() < screen: 
            self.rect.x = x
        else:
            pass
