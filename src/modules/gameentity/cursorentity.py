
import pygame
import math
from modules import gameentity

class Cursor(gameentity.defaultentity.Entity):

    def __init__(self, layer=0):
        super().__init__()
        self.add(gameentity.entitygroup.cursorgroup)
        gameentity.entitylayer.cursorlayer.add(self, layer=layer)
        
        self.image = pygame.Surface((10, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

        self._layer = layer

    def moving(self, position):
        self.rect.center = position
    
    def update(self, position):
        self.moving(position)
    