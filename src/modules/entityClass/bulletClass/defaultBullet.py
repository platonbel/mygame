import pygame
import math
import random
from modules.entityClass import defaultEntity, instances

class Bullet(defaultEntity.Entity):

    def __init__(self, owner, targets, mouse, spreadangle=0, shotrange=0, damage=0, layer=1):
        super().__init__()
        self.add(instances.entityGroup.bulletGroup)
        instances.entityLayer.defaultLayer.add(self, layer=layer)
        
        #realize here import png sprites
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()

        #render options
        self.hided = False
        self._layer = layer

        #characteristics
        self.owner = owner
        self.targets = targets
        self.shotrange = shotrange
        self.damage = damage
        self.speed = 20

        #set self and target coordinates
        #spread
        angle = random.randint(-spreadangle//2, spreadangle//2+1)
        rad_alfa = angle * (math.pi/180)

        self.position = pygame.math.Vector2(self.owner.rect.center)
        self.rect.center = self.position
        self.direction = (pygame.math.Vector2(mouse) - pygame.math.Vector2(self.rect.center)).normalize()

        self.direction[0] = self.direction[0] * math.cos(rad_alfa) - self.direction[1] * math.sin(rad_alfa)
        self.direction[1] = self.direction[0] * math.sin(rad_alfa) + self.direction[1] * math.cos(rad_alfa)
        if self.direction == (0, 0):
            a = random.random() 
            self.direction = (a, 1-a)
    
    def movement(self, dtime, TARGET_FPS):

        self.speedx = self.speed * self.direction[0]
        self.speedy = self.speed * self.direction[1]
        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        
        self.rect.centerx += self.speedx * dtime * TARGET_FPS
        self.rect.centery += self.speedy * dtime * TARGET_FPS

        dxvector = self.rect.center[0] - self.owner.rect.center[0]
        dyvector = self.rect.center[1] - self.owner.rect.center[1]

        distancecurrent = math.hypot(dxvector, dyvector)

        self.goal(distancecurrent)

    def goal(self, distancecurrent):
        hit = pygame.sprite.spritecollideany(self, self.targets)
        if hit:
            hit.health -= self.damage
            speedx = self.speed * self.direction[0]
            speedy = self.speed * self.direction[1]
            print(speedx, speedy)
            hit.position[0] += speedx
            hit.position[1] += speedy
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
