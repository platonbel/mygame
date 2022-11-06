import pygame
import math
import random
from modules import entityClass

class Bullet(entityClass.defaultEntity.Entity):

    def __init__(self, owner, targets, mouse, spreadangle=0, shotrange=0, damage=0, layer=1):
        super().__init__()
        self.add(entityClass.instances.entityGroup.bulletGroup)
        entityClass.instances.entityLayer.defaultLayer.add(self, layer=layer)
        
        #realize here import png sprites
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

        #render options
        self.hided = False
        self._layer = layer

        #set self and target coordinates
        self.rect.center = owner.rect.center
        self.firstplace =  owner.rect.center

        #spread
        angle = random.randint(-spreadangle//2, spreadangle//2+1)
        rad_alfa = angle * (math.pi/180)

        dxvector = mouse[0] - owner.rect.center[0]
        dyvector = mouse[1] - owner.rect.center[1]
        distancestart = math.sqrt(dxvector**2 + dyvector**2)

        kxvector = (dxvector / distancestart) if distancestart != 0 else 0
        kyvector = (dyvector / distancestart) if distancestart != 0 else 0

        kxvector = kxvector * math.cos(rad_alfa) - kyvector * math.sin(rad_alfa)
        kyvector = kxvector * math.sin(rad_alfa) + kyvector * math.cos(rad_alfa)

        #characteristics
        self.shooter = owner
        self.targets = targets
        if kxvector and kyvector:
            self.mouse = (kxvector, kyvector)
        else:
            a = random.random()
            self.mouse = (a, 1-a)
        self.shotrange = shotrange
        self.damage = damage
        self.speed = 20
    
    def movement(self, dtime, TARGET_FPS):

        self.speedx = self.speed * self.mouse[0]
        self.speedy = self.speed * self.mouse[1]
        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        
        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

        dxvector = self.rect.center[0] - self.firstplace[0]
        dyvector = self.rect.center[1] - self.firstplace[1]

        distancecurrent = math.sqrt(dxvector**2 + dyvector**2)

        self.goal(distancecurrent, dtime, TARGET_FPS)

    def goal(self, distancecurrent, dtime, TARGET_FPS):
        hit = pygame.sprite.spritecollideany(self, self.targets)
        if hit:
            hit.health -= self.damage
            speedx1 = self.speed * self.mouse[0]
            speedy1 = self.speed * self.mouse[1]
            hit.rect.x += speedx1 
            hit.rect.y += speedy1 
            self.__del__()
        elif distancecurrent >= self.shotrange:
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
