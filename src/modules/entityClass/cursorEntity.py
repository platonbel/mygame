
import pygame
from modules import entityClass

class Cursor(entityClass.privateEntity.Entity):

    def __init__(self, layer=0, private=None):
        super().__init__(layer, private)
        self.add(entityClass.instances.entityGroup.cursorGroup)
        
        self.image = pygame.Surface((10, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

        self._layer = layer

    def moving(self, position):
        self.rect.center = position
    
    def update(self, position):
        self.moving(position)
    