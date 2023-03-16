
import pygame
from gameCode import entityClass

class Entity(pygame.sprite.Sprite):
    instances = set()
    
    def __init__(self, size=(10, 10), color=(0, 0, 0), layer=0, privateLayer=entityClass.instances.entityLayer.defaultLayer, privateGroup=entityClass.instances.entityGroup.defaultGroup):
        Entity.instances.add(self)
        super().__init__()
        if privateLayer:
            privateLayer.add(self, layer=layer)
        if privateGroup:
            self.add(privateGroup)

        #creating sprite
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()

        #render options
        self.hided = False
        self._layer = layer

        #general characteristics
        self.speedx = 0
        self.speedy = 0

    def borders(self, screen):
        if self.rect.right > screen.get_width(): self.rect.right = screen.get_width()
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.bottom > screen.get_height(): self.rect.bottom = screen.get_height()
        if self.rect.top < 0: self.rect.top = 0

    def update(self):
        None

    def __del__(self):
        self.kill()