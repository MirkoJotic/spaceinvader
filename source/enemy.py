import pygame
WHITE = (255, 255, 255)

class Enemy(pygame.sprite.Sprite):
    _move = -10

    def __init__(self, row, color, width, height):
        # Call the parent class (Sprite) constructor
        super(Enemy, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        if row == 'first':
            self.image = pygame.image.load("resources/BottomRow.png").convert_alpha()
            self.points = 10
            self.row = row
        if row == 'second':
            self.image = pygame.image.load("resources/MidleRow.png").convert_alpha()
            self.points = 20
            self.row = row
        if row == 'third':
            self.image = pygame.image.load("resources/TopRow.png").convert_alpha()
            self.points = 40
            self.row = row

        self.width = width
        self.height = height


        self.rect = self.image.get_rect()

        self.move = -10

    @property
    def speed(self):
        return self.__class__._move
    @speed.setter
    def speed(self, value):
        self.__class__._move = value

    def setDirection(self, windowSize):
        if self.rect.x + 20 >= windowSize[0]:
            self.speed = -10
            return True
        if self.rect.x <= 10:
            self.speed = 10
            return True

        return False

    def update(self):
        self.rect.x += self._move
