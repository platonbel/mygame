
import pygame
import math
from modules import gameentity

class Bullet(gameentity.defaultentity.Entity):
    instances = set()

    def __init__(self, player, targets, vector, range=0, damage=0, layer=1):
        Bullet.instances.add(self)
        super().__init__()
        self.add(gameentity.entitygroup.bulletgroup)
        gameentity.entitylayer.defaultlayer.add(self, layer=layer)
        
        #realize here import png sprites
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

        #render options
        self.hided = False
        self._layer = layer
        #set self and target coordinates
        self.rect.center = player.rect.center
        self.firstplace = player.rect.center

        #characteristics
        self.targets = targets
        self.vector = vector
        self.range = range
        self.damage = damage
    
    def movement(self, dtime, TARGET_FPS):
        dxvector = self.vector[0] - self.rect.center[0]
        dyvector = self.vector[1] - self.rect.center[1]
        distancecurrent = math.sqrt(dxvector**2 + dyvector**2)

        dx1vector = self.vector[0] - self.firstplace[0]
        dy1vector = self.vector[1] - self.firstplace[1]
        distancestart = math.sqrt(dx1vector**2 + dy1vector**2)

        kxvector = (dxvector / distancecurrent) if distancecurrent != 0 else 0
        kyvector = (dyvector / distancecurrent) if distancecurrent != 0 else 0
        self.speedx = (20 if abs(dxvector) >= 20 else 1) * kxvector
        self.speedy = (20 if abs(dyvector) >= 20 else 1) * kyvector
        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        
        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

        self.goal(distancestart, distancecurrent)

    def goal(self, distancestart, distancecurrent):
        hit = pygame.sprite.spritecollideany(self, self.targets)
        if hit:
            hit.health -= self.damage
            self.__del__()
        elif distancecurrent == 0 or (distancestart - distancecurrent) >= self.range:
            self.__del__()
        
    def visible(self):
        #displaying the sprite if not hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

    def update(self, dtime, TARGET_FPS):
        self.movement(dtime, TARGET_FPS)
        self.visible()
        
    def __del__(self):
        self.kill()
