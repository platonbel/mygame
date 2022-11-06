
import pygame
import math
from modules import entityClass, textClass, shapeClass

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
        self.hided = False
        self._layer = layer
        #realize here import spawnpoint info 
        self.rect.center = position

        #characteristics
        self.health = 200
        self.maxhealth = 200

        #name binding
        self.name = textClass.defaultText.Text(name, side='center', position=(position[0], position[1]-30))

        #bars binding
        self.healthbarback = shapeClass.defaultShape.Shape(size=(100, 8), side='center', color=(192, 192, 192))
        self.healthbar = shapeClass.defaultShape.Shape(size=(100, 8), side='center', color=(0, 255, 0))

    def movement(self, target, dtime, TARGET_FPS):
        if target:
            #set the movement vector
            dxvector = target.rect.x - self.rect.x
            dyvector = target.rect.y - self.rect.y
            movementvector = math.sqrt(dxvector **2 + dyvector**2)
            kxvector = (dxvector / movementvector) if movementvector != 0 else 0
            kyvector = (dyvector / movementvector) if movementvector != 0 else 0
            
            #set the speed 
            self.speedx = (6 if abs(dxvector) >= 6 else 1) * kxvector
            self.speedy = (6 if abs(dyvector) >= 6 else 1) * kyvector
            self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
            self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        else:
            #realise here random moving system
            self.speedx, self.speedy = 0, 0

        #stopping if no press
        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

    def namerender(self):
        #giving to connected text label the position
        self.name.position = (self.rect.center[0], self.rect.center[1]-40)

    def characteristicsBarRender(self):
        healthratio = self.health / self.maxhealth
        self.healthbar.sizeedit((round(100*healthratio), 8))
        self.healthbar.rect = self.healthbarback.image.get_rect()

        self.healthbarback.position = (self.rect.center[0], self.rect.center[1]+30)
        self.healthbar.position = (self.rect.center[0], self.rect.center[1]+30)

    def visible(self):
        #displaying the sprite if not hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

    def healthupdate(self):
        if self.health <= 0:
            self.health = 0
            self.__del__()

    def update(self, target, screen, dtime, TARGET_FPS):
        self.healthupdate()
        self.movement(target, dtime, TARGET_FPS)
        self.borders(screen)
        self.characteristicsBarRender()
        self.namerender()
        self.visible()

    def __del__(self):
        self.kill()
        self.name.kill()
        self.healthbar.kill()
        self.healthbarback.kill()