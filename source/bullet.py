import pygame
WHITE = (255, 255, 255)        

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet, self).__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        self.rect.y += 3
    

class MyBullet(pygame.sprite.Sprite):
	""" Just the hero bullet """
	def __init__(self):
		super(MyBullet, self).__init__()

		self.image = pygame.Surface([4, 10])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y -= 3


