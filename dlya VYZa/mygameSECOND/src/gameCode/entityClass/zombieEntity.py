
import pygame
import math
from gameCode import entityClass, textClass, shapeClass, functions

class Zombie(entityClass.defaultEntity.Entity):
    instances = set()

    def __init__(self, position=(0, 0), image=None, name=None, layer=0):
        Zombie.instances.add(self)
        super().__init__()
        self.add(entityClass.instances.entityGroup.zombieGroup)
        entityClass.instances.entityLayer.defaultLayer.add(self, layer=layer)
        
        #realize here import png sprites
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 75))
        self.rect = self.image.get_rect()

        #render options
        self.position = pygame.math.Vector2(position)
        self.hided = False
        self.rect.center = position

        #characteristics
        self.health = 200
        self.maxhealth = 200
        self.speed = 6

        #targets binding
        self.targets = entityClass.instances.entityGroup.playerGroup
        self.target = None

        #gui binding
        self.name = textClass.defaultText.Text(text=name, side='center', position=(position[0], position[1]-30))
        self.healthbarback = shapeClass.defaultShape.Shape(size=(100, 8), side='center', color=(192, 192, 192))
        self.healthbar = shapeClass.defaultShape.Shape(size=(100, 8), side='center', color=(0, 255, 0))

    def movement(self, dtime, TARGET_FPS):
        if self.target:
            distance = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
            if distance:
                direction = distance.normalize()
                self.speedx = (self.speed * direction[0]) if abs(distance[0]) >= self.speed else 1 * direction[0]
                self.speedy = (self.speed * direction[1]) if abs(distance[1]) >= self.speed else 1 * direction[1]
                self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
                self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
                self.position[0] += self.speedx * dtime * TARGET_FPS
                self.position[1] += self.speedy * dtime * TARGET_FPS
            self.rect.center = (round(self.position[0]), round(self.position[1]))
        else:
            #realise here random moving system
            self.speedx, self.speedy = 0, 0
            self.rect.center = (round(self.position[0]), round(self.position[1]))

    def targetdetect(self):
        for target in self.targets:
            if functions.distanceСalculation(self, target) <= 400:
                if not self.target:
                    self.target = target
            else:
                self.target = None

    def GUIRender(self):
        healthratio = self.health / self.maxhealth
        self.healthbar.sizeedit((round(100*healthratio), 8))
        self.healthbar.rect = self.healthbarback.image.get_rect()

        self.name.moving((self.rect.center[0], self.rect.center[1]-40))
        self.healthbarback.moving((self.rect.center[0], self.rect.center[1]+30))
        self.healthbar.moving((self.rect.center[0], self.rect.center[1]+30))

    def visible(self, hided):
        self.hided = hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

    def statiscticsUpdate(self):
        if self.health <= 0:
            self.health = 0
            self.__del__()
        if self.health > self.maxhealth:
            self.health = self.maxhealth

    def update(self, screen, dtime, TARGET_FPS):
        self.statiscticsUpdate()
        self.movement(dtime, TARGET_FPS)
        self.targetdetect()
        self.borders(screen)
        self.GUIRender()

    def __del__(self):
        self.kill()
        self.name.kill()
        self.healthbar.kill()
        self.healthbarback.kill()